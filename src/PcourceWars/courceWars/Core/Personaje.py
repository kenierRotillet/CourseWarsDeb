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
        self.currentState = State.State(0,True) #estado en el que se encuentra el personaje actualmente
        self.maxHP = 100
        self.currentHP = self.maxHP
        self.atk = 100
        self.deff= 100

        self.anims = {}
        self.currentAnim = "Stand" #Estado por defecto en el cual se inicia
        self.staticAnim = "Stand" #Nombre de la animación al estar quieto, default Stand
        self.maxSpeed = 0
        self.jumpSpeed =0
        self.player = player
        self.commands = {}        
        self.framecount =0
        self.image = ""
        self.rect = ""
        self.currentAnimFrame=0
        



    def move(self, x,y):
        self.rect.move_ip((x, y))
        
        


    def update(self):
        if (self.currentAnimFrame >= len(self.anims[self.currentAnim])):
            self.framecount=0
            self.currentAnim=self.staticAnim
            self.currentAnimFrame=0

        else:
            if (self.framecount == self.anims[self.currentAnim][self.currentAnimFrame][0]):
                self.currentAnimFrame+=1
                self.framecount=0
            else:
                self.framecount+=1
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])


    def lookCommand(self, keys,currentTime):
        if (self.currentState.control == False):
            return

        for cmd in self.commands.items():
            keystroke = []
            if (len(cmd[1][1]) > len(keys)):
                continue

            for k in range(0..len(cmd[1][1])):
                keystroke.append(keys.pop())

            if(currentTime - keystroke[-1][0] <= cmd[1][0]):
                match = True
                for k in range(0..len(keystroke)):
                    if keystroke[k][1] != cmd[1][1][-1 - k]:
                        match=False

                if match == True:
                    self.currentAnim = cmd[0]






                









    def DoAction(self,oponent):
        if self.currentAnim=='LightPunch':
            Tools.FastMethods.PlayAux()



