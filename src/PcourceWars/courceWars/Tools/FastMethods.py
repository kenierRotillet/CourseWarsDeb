#!/usr/bin/python
# -*- coding: latin-1 -*-
""" módulo con herramientas de carga, converción, y revición rápidas para el juego."""

import pygame
import sys
import os
from pygame.locals import *
import Tools.Logger


snd1 = pygame.mixer.Sound("sfx/out-0001.wav")
snd2 = pygame.mixer.Sound("sfx/out-0003.wav")
snd3 = pygame.mixer.Sound("sfx/out-0005.wav")
#Better image loading

def load_image(name, colorkey=None,resize=False,flip=False):
    """ método de carga de imágenes. Recibe los argumentos name, path de la imagen, colorkey de la imagen, recize si necesita ser aumentado su tamaño, y flip, si necesita ser volteada."""

    #intento de carga de la imagen
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        Tools.Logger.escribir('Cannot load image:' +  str(name))
        Tools.Logger.escribir(str(message))
        #raw_input()

        raise SystemExit, message
    #converción de alphas de la imagen
    image = image.convert_alpha()
    if resize == True:
        #Aumento de tamaño de la imagen
        image = pygame.transform.scale(image,(700,700))

    if colorkey is not None:
        #Aplicación del colorkey
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    if flip == True:
        #En caso de ser indicado, la imagen se voltea
        image = pygame.transform.flip(image,1,0)

    return image, image.get_rect()

def LoadAnimData(name):
    """método para cargar el diccionario de imágenes a partir de un archivo *.anim"""
    #anims, diccionario base a retornar con las imágenes 

    anims = {}
    #carga del archivo
    arch = open(name,'r')
    data = ""
    for i in arch:
        data+=i
        #print i
        
    arch.close()
    #Separación de cada movimiento en una entrada de animsdata
    animsdata = data.split(';')
    #raw_input()

    for an in animsdata:
        #en caso de ser línea bacía se salta
        if (len(an.split(':')) < 2):
            continue

        #extración del nombre de la animación
        animname = an.split(':')[0].replace('\n', "")
        
        #print animname
        animdata = []
        #raw_input()
        #print an.split(':')
        #print " su tamaño es: " + str(len(an.split(':')))
        for line in an.split(':')[1].split('\n'):
            #print line
            #raw_input()
            lin = line.split(',')
            #print lin
            if(len(lin) >= 2):
                animdata.append((lin[0],lin[1]))
                #print animdata

        #se añade la información optenida
        anims[animname] = animdata
        #print anims[animname]
    
    #print anims
    return anims


def detectKeys(keys):
    """método de detección y separación de teclas de jugador 1, y de jugador dos. no implementado aún """
    return

def convertKeys(keys):
    """converción de teclas del formato pygame, al formato cws. Sirve para configurar cualquier tecla"""
    Tools.Logger.escribir("llegaron las teclas")
    Tools.Logger.escribir(str(keys))
    #El método se  ejecuta recursivamente en caso de recibir más de una tecla. es para poder escribirlas en el formato x+y en el caso de ser presionadas más de una tecla en el mismo frame, y conciderarse como presión simultánea.


    if len(keys) > 1:
        recat = ""
        for k in keys:
            kkp = []
            kkp.append(k)
            if convertKeys(kkp) != "":


                recat += convertKeys(kkp) + "+"

        if len(recat) > 1 and  recat[-1] == '+':
            recat=recat[:-1]
            return recat
        
            



    key = ""
    if len(keys) > 0:

        key = keys[0]
    else:
        key = keys

    #En caso de querer alterar una tecla o la configuración de estas, simplemente cambiar los if subsiguientes
    if (key == K_LEFT):
        return "B"
    elif(key == K_RIGHT):
        return "F"
    elif(key == K_DOWN):
        return "D"
    elif(key == K_UP):
        return "U"
    elif(key == K_z):
        return "a"
    elif(key == K_x):
        return "b"
    elif(key == K_c):
        return "c"
    elif(key == K_s):
        return "x"
    elif(key == K_RETURN):
        return "s"
    else:
        return ""








def load_commands(name):
    """método para la carga de comandos de los movimientos, a partir de los archivos *.cmd . Los nombres de movimientos deben de coincidir con los de las animaciones para funcionar todo bien. La secuencia de teclas se cargan utilizando los nombres empleados en convertKeys."""
    all = ""
    arch = open(name,'r')
    for line in arch:
        all+=line

    arch.close()
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













def PlayAux(pl = 0):
    """método para acciones auxiliares de debug"""

    lala="lala"
    #if pl == 0 :

        #snd1.play()
    #elif pl == 1:
        #snd2.play()
    #elif pl == 2:
        #snd3.play()





def LoadSounds(name):
    """método de carga de sonidos, a través de los archivos *.snd. cada sonido se asocia con una animación a través de los nombres."""
    sounds = {}
    arch = open(name,'r')
    data = ""
    for i in arch:
        data+=i
        #print i
    arch.close()
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
        #print " su tamaño es: " + str(len(an.split(':')))
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


