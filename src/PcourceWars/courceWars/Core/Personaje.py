#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase base que define aspectos básicos y funciones estándar para cada personaje"""
import pygame
from pygame.locals import *
import State
import Tools


class Personaje(pygame.sprite.Sprite):
    """ Clase de personaje. Recibe número de jugador """
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.currentState = State.State() #estado en el que se encuentra el personaje actualmente
        self.anims = {}
        self.currentAnim = "Stand"
        self.staticAnim = ""
        self.maxSpeed = 0
        self.jumpSpeed =0
        self.player = player
        self.currentAnimFrame = 0
        self.image = pygame.Surface((10,10))
        self.rect=self.image.get_rect()
        self.framecount =0



    def move(self, x,y):
        self.rect.move_ip((x, y))
        
       


    def update(self):
        if (self.currentAnimFrame >= len(self.anims[self.currentAnim])):
            if (self.framecount == self.anims[self.currentAnim][self.currentAnimFrame][0]):
                self.framecount=0
                self.currentAnim=self.staticAnim
                self.currentAnimFrame=0
            else:
                self.framecount+=1
        else:
            if (self.framecount == self.anims[self.currentAnim][self.currentAnimFrame][0]):
                self.currentAnimFrame+=1
                self.framecount=0
            else:
                self.framecount+=1
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])

