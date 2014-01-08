#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import sys
import os
from pygame.locals import *
import Tools.Logger

snd1 = pygame.mixer.Sound("sfx/out-0001.wav")
snd2 = pygame.mixer.Sound("sfx/out-0003.wav")
snd3 = pygame.mixer.Sound("sfx/out-0005.wav")
#Better image loading
def load_image(name, colorkey=None):
    
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        print message
        raw_input()

        raise SystemExit, message
    #image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def LoadAnimData(name):
    anims = {}
    arch = open(name,'r')
    data = ""
    for i in arch:
        data+=i
        #print i
    animsdata = data.split(';')
    #raw_input()

    for an in animsdata:
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
            if(len(lin) >= 2):
                animdata.append((lin[0],lin[1]))
                #print animdata

        anims[animname] = animdata
        #print anims[animname]
    arch.close()
    #print anims
    return anims


def detectKeys(keys):
    return

def convertKeys(keys):
    Tools.Logger.escribir("llegaron las teclas")
    Tools.Logger.escribir(str(keys))

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













def PlayAux(pl = 0 ):
    if pl == 0 :

        snd1.play()
    elif pl == 1:
        snd2.play()
    elif pl == 2:
        snd3.play()




