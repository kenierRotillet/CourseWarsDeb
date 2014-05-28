#!/usr/bin/python
# -*- coding: latin-1 -*-
""" m�dulo con herramientas de carga, converci�n, y revici�n r�pidas para el juego,adem�s de elementos de configuraci�n."""

import pygame
import sys
import os
from pygame.locals import *
import Tools.Logger


#teclas para cada jugador:
p1keys = []
p2keys = []
deadZone=0.3
joysticks =[]
activeJoysticksAxis=[]
activeJoysticksHats=[]

#m�todo de inicializaci�n de controles:
def initJoysticks():
    global joysticks
    global activeJoysticksAxis
    global activeJoysticksHats
    activeJoysticksAxis=[]
    activeJoysticksHats=[]
    joysticks=[]
    for j in range(0,pygame.joystick.get_count()):
        J = pygame.joystick.Joystick(j)
        J.init()
        joysticks.append(J)
        activeJoysticksAxis.append([])
        activeJoysticksHats.append([])
        for a in range(0,J.get_numaxes()):
            activeJoysticksAxis[j].append(0)
        for h in range(0,J.get_numhats()):
            activeJoysticksHats[j].append((0,0))


        Tools.Logger.escribir("inicializado " + J.get_name())




#carga de teclas
def loadKeys():
    
    try:

        data = loadFile("cfg/keis.ini")
        players = data.split(';')
        for p in players:
            plist = []
            #Tools.Logger.escribir("l�nea dividida por ; " + p)
        
            if p.startswith('\n') == True:
                p = p[1:]


            if p.split(':')[0] == 'p1':
                plist = p1keys
                #Tools.Logger.escribir("analizando teclas del p1")
            elif p.split(':')[0] == 'p2':
                plist = p2keys
                #Tools.Logger.escribir("cargando teclas del p2")
            else:
                #Tools.Logger.escribir("no es jugador")
                continue
            for k in p.split(':')[1].split('\n'):
                #Tools.Logger.escribir("analizando la l�nea " + k)
                if len(k) < 2:
                    continue
                plist.append((k.split('=')[0],k.split('=')[1]))

        Tools.Logger.escribir("teclas p1: " + str(p1keys))
        Tools.Logger.escribir("teclas p2: " + str(p2keys))
    except Exception:
        Tools.Logger.escribir("No est� el archivo de teclas, por favor iniciar KeyConfig.py en la carpeta Tools")
        Tools.Logger.excepcion()
        

#Better image loading

def load_image(name, colorkey=None,resize=False,flip=False):
    """ m�todo de carga de im�genes. Recibe los argumentos name, path de la imagen, colorkey de la imagen, recize si necesita ser aumentado su tama�o, y flip, si necesita ser volteada."""
    if name == '-1':
        return -1


    #intento de carga de la imagen
    try:
        
        image = pygame.image.load(name)
    except pygame.error, message:
        Tools.Logger.escribir('Cannot load image:' +  str(name))
        Tools.Logger.escribir(str(message))
        #raw_input()

        
    #converci�n de alphas de la imagen
    image = image.convert_alpha()
    if resize == True:
        #Aumento de tama�o de la imagen
        image = pygame.transform.scale(image,(700,700))

    if colorkey is not None:
        #Aplicaci�n del colorkey
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    if flip == True:
        #En caso de ser indicado, la imagen se voltea
        image = pygame.transform.flip(image,1,0)

    return image

def load_sound(name):
    try:
        if len(name) > 2:
            sonido = pygame.mixer.Sound(name)
            return sonido
        else:
            return ""
    except Exception, mes:
        Tools.Logger.escribir("Error en carga de sonido: " + str(mes))



def LoadAnimData(name):
    """m�todo para cargar el diccionario de im�genes a partir de un archivo *.anim"""
    #anims, diccionario base a retornar con las im�genes
    Tools.Logger.escribir("cargando im�genes en memoria de " + name)

    anims = {}
    #carga del archivo
    
    data = loadFile(name)
    #Separaci�n de cada movimiento en una entrada de animsdata
    animsdata = data.split(';')
    #raw_input()

    for an in animsdata:
        #en caso de ser l�nea bac�a se salta
        if (len(an.split(':')) < 2):
            continue

        #extraci�n del nombre de la animaci�n
        animname = an.split(':')[0].replace('\n', "")
        
        #print animname
        animdata = []
        #raw_input()
        #print an.split(':')
        #print " su tama�o es: " + str(len(an.split(':')))
        for line in an.split(':')[1].split('\n'):
            #print line
            #raw_input()
            lin = line.split(',')
            #print lin
            if(len(lin) >= 2):
                animdata.append((int(lin[0]), load_image(lin[1],resize=True)))
                #print animdata

        #se a�ade la informaci�n optenida
        anims[animname] = animdata
        Tools.Logger.escribir("cargada la animaci�n " + str(animname) + ": \n " + str(anims[animname]))
    
    #print anims
    return anims


def detectKeys(keys=[],player=1,release=False,buttons=[],axis=[],hats=[]):
    """m�todo de detecci�n y separaci�n de teclas de jugador 1, y de jugador dos. no implementado a�n"""
    teclas=[]
    for k in keys:
        teclas.append(str(k.key))

    for b in buttons:
        t=str(b.joy)+"/b"+str(b.button)
        teclas.append(t)

    for a in axis:
        if release==False:

            if a.value >= deadZone:
                t=str(a.joy)+"/a"+str(a.axis)+"/+"
                Tools.Logger.escribir("movimiento entrante de eje: "+t)
                teclas.append(t)

            elif a.value <= -1*deadZone:
                t=str(a.joy)+"/a"+str(a.axis)+"/-"
                Tools.Logger.escribir("movimiento entrante de eje: "+t)
                teclas.append(t)
        else:
            t=activeJoysticksAxis[a.joy][a.axis]
            Tools.Logger.escribir("movimiento saliente de eje. Se solt� "+str(t))
            
            activeJoysticksAxis[a.joy][a.axis]=a.value
            Tools.Logger.escribir("Nuevo movimiento escrito: "+str(activeJoysticksAxis[a.joy][a.axis]))

            if t >= deadZone:
                tep = str(a.joy)+"/a"+str(a.axis)+"/+"
                Tools.Logger.escribir("Comprovando "+tep)
                teclas.append(tep)
            elif t <= -1*deadZone:
                tep = str(a.joy)+"/a"+str(a.axis)+"/-"
                Tools.Logger.escribir("Comprovando "+tep)
                teclas.append(tep)
            








    for h in hats:
        if release==False:

            t=str(h.joy)+"/h"+str(h.hat)+"/"+str(h.value)
            Tools.Logger.escribir("movimiento entrante de hats: "+t)
            teclas.append(t)
        else:
            t = activeJoysticksHats[h.joy][h.hat]
            Tools.Logger.escribir("movimiento saliente de hats. Se solt� "+str(t))


            activeJoysticksHats[h.joy][h.hat]=h.value
            Tools.Logger.escribir("Nuevo movimiento escrito: "+str(activeJoysticksHats[h.joy][h.hat]))

            tep = str(h.joy)+"/h"+str(h.hat)+"/"+str(t)
            Tools.Logger.escribir("Comprovando "+tep)

            teclas.append(tep)




    return(convertKeys(teclas,player))


def convertKeys(keys,p=1):
    """converci�n de teclas del formato pygame, al formato cws. Sirve para configurar cualquier tecla"""
    #Tools.Logger.escribir("llegaron las teclas")
    #Tools.Logger.escribir(str(keys))
    #El m�todo se  ejecuta recursivamente en caso de recibir m�s de una tecla. es para poder escribirlas en el formato x+y en el caso de ser presionadas m�s de una tecla en el mismo frame, y conciderarse como presi�n simult�nea.

    #if para tomar en cuenta las teclas que se presionan al mismo tiempo
    if len(keys) > 1:
        recat = ""
        for k in keys:
            kkp = []
            kkp.append(k)
            if convertKeys(kkp,p) != "":


                recat += convertKeys(kkp,p) + "+"

        if len(recat) > 1 and  recat[-1] == '+':
            recat=recat[:-1]
            return recat
        
            



    key = ""
    if len(keys) > 0:

        key = keys[0]
    else:
        key = keys

    #la detecci�n ahora es mediante el recorrido de los for, correspondientes al personaje del cual se busquen teclas.
    selectP = p1keys
    if p == 2:
        selectP = p2keys
        #Tools.Logger.escribir("buscando comando de p2")


    for k in selectP:
        #Tools.Logger.escribir("comparando tecla ingresada " + str(key) + " con la tecla actual " + str(k))

        if k[1] == key:
            return k[0]

    return ""
        


def load_commands(name):
    """m�todo para la carga de comandos de los movimientos, a partir de los archivos *.cmd . Los nombres de movimientos deben de coincidir con los de las animaciones para funcionar todo bien. La secuencia de teclas se cargan utilizando los nombres empleados en convertKeys."""
    all = loadFile(name)
    
    cmds = all.split('\n')
    commands = {}
    for cmd in cmds:
        if (len(cmd.split(':')) != 3):
            continue
        cmdname = cmd.split(':')[0]
        cmdtime=cmd.split(':')[1]
        cmdkeys = []
        for k in cmd.split(':')[2].split(','):
            cmdkeys.append(k)
        commands[cmdname] = (cmdtime,cmdkeys)
    return commands

def LoadSounds(name):
    """m�todo de carga de sonidos, a trav�s de los archivos *.snd. cada sonido se asocia con una animaci�n a trav�s de los nombres."""
    sounds = {}
    Tools.Logger.escribir("cargando sonidos en memoria")
    data = loadFile(name)

    soundsdata = data.split(';')
    #raw_input()

    for an in soundsdata:
        if (len(an.split(':')) < 2):
            continue

        animname = an.split(':')[0].replace('\n', "")
        
        #print animname
        animdata = []
        #raw_input()
        #print an.split(':')
        #print " su tama�o es: " + str(len(an.split(':')))
        for line in an.split(':')[1].split('\n'):
            #print line
            #raw_input()
            lin = line.split(',')
            #print lin
            if(len(lin) >= 3):
                animdata.append((lin[0], load_sound(lin[1]), load_sound(lin[2])))
                #print animdata

        sounds[animname] = animdata
        Tools.Logger.escribir("cargados los sonidos de la animaci�n: " + animname + ": \n " + str(sounds[animname]))
        #print anims[animname]
    
    #print anims
    return sounds



def LoadHitboxesData(name):
    """Metodo que carga la informaci�n de las cajas de colicion y de da�o para cada una de las diferentes animaciones. Son los archivos *.hbx"""
    #anims, diccionario base a retornar con los hitboxes

    anims = {}
    #carga del archivo
    
    data = loadFile(name)
    #Separaci�n de cada movimiento en una entrada de animsdata
    animsdata = data.split(';')
    #raw_input()

    for an in animsdata:
        #en caso de ser l�nea bac�a se salta
        if (len(an.split(':')) < 2):
            continue

        #extraci�n del nombre de la animaci�n
        animname = an.split(':')[0].replace('\n', "")
        
        #print animname
        animdata = []
        
        #raw_input()
        #print an.split(':')
        #print " su tama�o es: " + str(len(an.split(':')))
        for line in an.split(':')[1].split('}'):
            #print line
            datos = line.split('{')
            #print "datos " + str(datos)
            if len(datos) < 2:
                continue

            frame = int(datos[0].replace('\n',''))
            #print "frame: " + str(frame)
            boxes = []
            for k in datos[1].split('\n'):
                #print "el k " +str(k)
                deita = k.split(',')
                if len(deita) > 3:
                    boxes.append([deita[0],int(deita[1]),int(deita[2]),int(deita[3]),int(deita[4])])
            animdata.append((frame,boxes))
        #se a�ade la informaci�n optenida
        anims[animname] = animdata
        #print anims[animname]
    
    #print anims
    return anims



def loadFile(name):
    """M�otodo generalizado para cargas de archivo. rechasa las l�neas que inician con #"""
    arch = open(name,'r')
    data = ""
    for i in arch:
        if(i.startswith("#") == False and len(i) > 0):

            data+=i
        #print i
        
    arch.close()
    return data

def flipImage(img):
    image = pygame.transform.flip(img,1,0)
    return image