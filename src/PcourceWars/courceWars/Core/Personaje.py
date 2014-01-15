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
        self.power=0
        self.maxpower=100

        self.anims = {}
        self.sounds = {}
        self.currentSounds = []
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
        self.pos = (0,100)
        



    def move(self, x,y):
        self.pos=(self.pos[0]+x,self.pos[1]+y)
        
        
        


    def update(self):
        
        if (self.currentAnimFrame > len(self.anims[self.currentAnim])-1):
            self.framecount=0
            self.currentAnim=self.staticAnim
            self.currentAnimFrame=0

        else:
            if (self.framecount == int(self.anims[self.currentAnim][self.currentAnimFrame][0])):
                self.currentAnimFrame+=1
                self.framecount+=1
                if self.currentAnimFrame >= len(self.anims[self.currentAnim]):
                    self.currentAnim=self.staticAnim
                    self.currentAnimFrame=0
                    self.framecount=0


            else:
                self.framecount+=1
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1],None,True)
        self.rect.center=self.pos
        Tools.Logger.escribir("animacion " + self.currentAnim + ", en su imagen " + str(self.currentAnimFrame) + ", y el frame de tiempo " + str(self.framecount))



    def lookCommand(self, keys,currentTime):
        #Tools.Logger.escribir("teclas ingresadas en el tiempo: " + str(currentTime))
        #Tools.Logger.escribir(str(keys))
        if (self.currentState.control == False):
            return
        tolerancy = 0
        for cmd in self.commands.items():
            keystroke = []
            
            
            if (len(cmd[1][1]) > len(keys)) or len(cmd[1][1]) <= tolerancy:
                continue
            lencmd = len(cmd[1][1])


            for k in range(0,lencmd):
                keystroke.append(keys.pop())

            match = False
            if((int(currentTime) - int(keystroke[-1][0])) <= int(cmd[1][0])):
                #Tools.Logger.escribir("el resultado de la resta de tiempo entre " + str(currentTime) + " " + str(keystroke[-1][0]) + " es:" + str(currentTime - keystroke[-1][0] ) + " menor que " + str(cmd[1][0]))
                match = True
                for k in range(0,len(keystroke)):
                    if keystroke[k][1] != cmd[1][1][-1 - k]:
                        match=False
                        #print "no hay tecla"

            if match == True:
                self.currentAnim = cmd[0]
                self.currentAnimFrame=0
                self.framecount=0
                tolerancy=len(cmd[1][1])
                    #print "hay tecla"
                #else:
            for k in range(0,len(keystroke)):
                keys.append(keystroke[-1 - k])










                









    def DoAction(self,oponent):
        Tools.Logger.escribir("actual estado es " + self.currentAnim)
        if self.currentAnim=='LightPunch':
            Tools.FastMethods.PlayAux()
            #self.currentAnim='Stand'
        if self.currentAnim =='md':
            Tools.FastMethods.PlayAux(1)
            #self.currentAnim='Stand'
        if self.currentAnim == 'FrontDash':
            Tools.FastMethods.PlayAux(2)
            #self.currentAnim='Stand'


    def setSounds(self):
        if self.sounds.has_key(self.currentAnim):
            for snditem in self.sounds[self.currentAnim]:
                if int(snditem[0]) == self.framecount:
                    self.currentSounds.append(snditem[1])
                    if self.currentState.flags.has_key('Hit'):
                        self.currentSounds.append(snditem[2])




