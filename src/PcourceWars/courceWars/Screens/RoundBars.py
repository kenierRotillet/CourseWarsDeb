#!/usr/bin/python
# -*- coding: latin-1 -*-
"""módulo que representa a las barras de vida de cada uno de los personajes"""

import sys, pygame

width, height = 1024, 768
red=(255,0,0)
grey=(150,150,150)
black=(0,0,0)

class Round_Bar(object):
    
    def __init__(self, Screen,NumJug):
        self.screen = Screen
        self.numJug = NumJug
    
    def draw(self, win):
        color1=grey
        color2=grey
        if win==1:
            color1=red
        if win==2:
            color1=red
            color2=red

        if(self.numJug == 1):
            pygame.draw.rect(self.screen,black,(30,61,19,14),0)
            pygame.draw.rect(self.screen,black,(55,61,19,14),0)
            pygame.draw.rect(self.screen,color1,(32,63,15,10),0)
            pygame.draw.rect(self.screen,color2,(57,63,15,10),0)
        else:
            pygame.draw.rect(self.screen,black,(width - 49,61,19,14),0)
            pygame.draw.rect(self.screen,black,(width - 74,61,19,14),0)
            pygame.draw.rect(self.screen,color2,(width - 47,63,15,10),0)
            pygame.draw.rect(self.screen,color2,(width - 72,63,15,10),0)
