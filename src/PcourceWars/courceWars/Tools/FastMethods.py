#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
import sys
import os
from pygame.locals import *

#Better image loading
def load_image(name, colorkey=None):
    
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
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
        if (len(an) < 2):
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
