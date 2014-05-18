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

#carga de teclas
def loadKeys():
    
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
            plist.append((k.split(',')[0],int(k.split(',')[1])))

    #Tools.Logger.escribir(str(p1keys))
    #Tools.Logger.escribir(str(p2keys))

#Better image loading

def load_image(name, colorkey=None,resize=False,flip=False):
    """ m�todo de carga de im�genes. Recibe los argumentos name, path de la imagen, colorkey de la imagen, recize si necesita ser aumentado su tama�o, y flip, si necesita ser volteada."""

    #intento de carga de la imagen
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        Tools.Logger.escribir('Cannot load image:' +  str(name))
        Tools.Logger.escribir(str(message))
        #raw_input()

        raise SystemExit, message
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

    return image, image.get_rect()

def LoadAnimData(name):
    """m�todo para cargar el diccionario de im�genes a partir de un archivo *.anim"""
    #anims, diccionario base a retornar con las im�genes 

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
                animdata.append((lin[0],lin[1]))
                #print animdata

        #se a�ade la informaci�n optenida
        anims[animname] = animdata
        #print anims[animname]
    
    #print anims
    return anims


def detectKeys(keys):
    """m�todo de detecci�n y separaci�n de teclas de jugador 1, y de jugador dos. no implementado a�n """
    return

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
                animdata.append((lin[0],lin[1],lin[2]))
                #print animdata

        sounds[animname] = animdata
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
