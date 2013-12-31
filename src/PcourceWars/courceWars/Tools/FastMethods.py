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
    return
