#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase base que define aspectos bÃ¡sicos y funciones estÃ¡ndar para cada personaje"""
import pygame
from pygame.locals import *
import State
import Tools
#import Colisiones


class Personaje(pygame.sprite.Sprite):
    """ Clase de personaje. Recibe nÃºmero de jugador """
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        """constructor de la clase del personaje. maneja y tiene todas las funcionalidades en comÃºn para cada personaje, como reconocimiento de convinaciÃ³n de teclas, actualizaciÃ³n de frames, interpretaciÃ³n de sonidos y programaciÃ³n de movimientos comunes."""

        self.currentState = State.State(0,True) #estado en el que se encuentra el personaje actualmente #estado en el que se encuentra actualmente, se inicializa como estado 0 y con control.
        self.maxHP = 100
        self.currentHP = self.maxHP #cantidad mÃ¡xima de hp y cantidad actual de hp
        self.atk = 100 #poder de ataque, para cÃ¡lculo de daÃ±o futuro
        self.deff= 100 #valor de defensa  para cÃ¡lculo de daÃ±o futuro
        self.power=0 #cantidad de carga inicial
        self.maxpower=100 #cantidad de poder mÃ¡ximo

        self.anims = {} #diccionario de animaciones
        self.sounds = {} #diccionario de sonidos por animaciÃ³n 
        self.currentSounds = [] #stack de sonidos encadenados para un frame en especÃ­fico
        self.currentAnim = "Stand" #Estado por defecto en el cual se inicia la animaciÃ³n, y esta variable muestra la animaciÃ³n correspondiente a un frame
        self.staticAnim = "Stand" #Nombre de la animaciÃ³n al estar quieto, default Stand
        self.maxSpeed = 0 #velocidad a la cual el personaje se mueve
        self.dashspeed = 0 #velocidad de dash del personaje
        self.jumpSpeed =0 #velocidad de salto
        self.player = player #nÃºmero de jugador
        self.commands = {}        #diccionario de comandos 
        self.framecount =0 #nÃºmero de frame que lleva la animaciÃ³n actual
        self.image = "" #surface representante del sprite
        self.rect = "" #rect representante del sprite
        self.mask = "" #mÃ¡scara reprecentante de la imagen del sprite
        self.currentAnimFrame=0 #nÃºmero de imagen actual de la animaciÃ³n actual
        self.pos = (0,100) #posiciÃ³n por defecto de inicio
        self.flip = False #flag que indica si es necesario o no voltear la imagen
        if self.player == 2:
            self.flip=True #si se es jugador dos, habilitar el flip 

        



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
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1],None,True, self.flip)
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.center=self.pos
        #Tools.Logger.escribir("animacion " + self.currentAnim + ", en su imagen " + str(self.currentAnimFrame) + ", y el frame de tiempo " + str(self.framecount))



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
                kk = keys.pop()
                keystroke.append(kk)
                

            match = False
            if((int(currentTime) - int(keystroke[-1][0])) <= int(cmd[1][0])):
                #Tools.Logger.escribir("el resultado de la resta de tiempo entre " + str(currentTime) + " " + str(keystroke[-1][0]) + " es:" + str(currentTime - keystroke[-1][0] ) + " menor que " + str(cmd[1][0]))
                match = True
                for k in range(0,len(keystroke)):
                    keypress=""
                    keypress = cmd[1][1][-1 - k]
                    
                    if self.flip==True and keypress.__contains__('B')==True:
                        keypress = keypress.replace('B','F')
                    elif self.flip==True and keypress.__contains__('F')==True:
                        keypress=keypress.replace('F','B')

                    if keystroke[k][1] != keypress:
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

        # return 1 es daÃ±o nulo
        # return 2 es daÃ±o completo
        # return 0 es daÃ±o reducido por defensa

        def Golpe_Superior(colision, altura_1, altura_2, defensa):
            Tools.Logger.escribir("verificando coliciones en método")
            if defensa == True:
                if colision == None:
                    return 1
                else:
                    for x in range((altura_1 + 200)/3, (altura_1 + 200)*2/3):
                        for y in range(altura_2, altura_2 + 200):
                            if x == y:
                                return 0
            else:
                if colision == None:
                    return 1
                else:
                    for x in range((altura_1 + 200)/3, (altura_1 + 200)*2/3):
                        for y in range(altura_2, altura_2 + 200):
                            if x == y:
                                return 2
                    return 1

        def Golpe_Inferior(colision, altura_1, altura_2, defensa):
            if defensa == True:
                if colision == None:
                    return 1
                else:
                    for x in range((altura_1 + 200)*2/3, (altura_1 + 200)):
                        for y in range(altura_2, altura_2 + 200):
                            if x == y:
                                return 0
            else:
                if colision == None:
                    return 1
                else:
                    for x in range((altura_1 + 200)*2/3, (altura_1 + 200)):
                        for y in range(altura_2, altura_2 + 200):
                            if x == y:
                                return 2
                    return 1

        """mÃ©todo en el cual se programan cada uno de los movimientos de los ataques y acciones bÃ¡sicas de un personaje, movimiento, golpes bÃ¡sicos, y coliciones. El mÃ©todo recibe al oponente, siendo capaz de alterar su posiciÃ³n y estado, e incluso animaciÃ³n."""

        if oponent.pos[0] < self.pos[0]:
            self.flip=True
        else:
            self.flip=False
        Tools.Logger.escribir("actual estado es " + self.currentAnim)
        if self.currentAnim=='Stand':
            self.currentState=State.State(0,True)

        if self.currentAnim == 'LightPunch':
            self.currentState.control = False
            Tools.Logger.escribir("comprovando golpes")
            if Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                self.currentState.flags['Hit']=True
                Tools.Logger.escribir("hubo colición de golpe bloqueado")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                Tools.Logger.escribir("falló el golpe")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                self.currentState.flags['Hit']=True
                oponent.currentAnim='Hit'
                oponent.currentAnimFrame=0
                oponent.framecount=0
                Tools.Logger.escribir("le achuntó")

        if self.currentAnim == 'MediumPunch':
            self.currentState.control = False
            Tools.Logger.escribir("comprovando golpes")
            if Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                self.currentState.flags['Hit']=True
                Tools.Logger.escribir("hubo colición de golpe bloqueado")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                Tools.Logger.escribir("falló el golpe")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                self.currentState.flags['Hit']=True
                oponent.currentAnim='Hit'
                oponent.currentAnimFrame=0
                oponent.framecount=0
                Tools.Logger.escribir("le achuntó")

        if self.currentAnim == 'HighPunch':
            self.currentState.control = False
            Tools.Logger.escribir("comprovando golpes")
            if Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                self.currentState.flags['Hit']=True
                Tools.Logger.escribir("hubo colición de golpe bloqueado")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                Tools.Logger.escribir("falló el golpe")
            elif Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                self.currentState.flags['Hit']=True
                oponent.currentAnim='Hit'
                oponent.currentAnimFrame=0
                oponent.framecount=0
                Tools.Logger.escribir("le achuntó")

        if self.currentAnim== 'Down_LightPunch':
            self.currentState.control = False
            if Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                self.currentState.flags['Hit']=True
                Tools.Logger.escribir("hubo colición de golpe bloqueado")
            elif Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                Tools.Logger.escribir("falló el golpe")
            elif Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                self.currentState.flags['hit']=True
                oponent.currentAnim='Hit'
                oponent.currentAnimFrame=0
                oponent.framecount=0
                Tools.Logger.escribir("le achuntó")

        if self.currentAnim== 'Down_HighPunch':
            self.currentState.control = False
            if Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                self.currentState.flags['Hit']=True
                Tools.Logger.escribir("hubo colición de golpe bloqueado")
            elif Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                Tools.Logger.escribir("falló el golpe")
            elif Golpe_Inferior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                self.currentState.flags['hit']=True
                oponent.currentAnim='Hit'
                oponent.currentAnimFrame=0
                oponent.framecount=0
                Tools.Logger.escribir("le achuntó")

                

        if self.currentAnim=='Walk':
            self.currentState.control=False
            if pygame.sprite.collide_mask(self,oponent) != None:
                #Tools.Logger.escribir("ubo coliciÃ³n! no se puede avanzar")
                #Tools.Logger.escribir(str(pygame.sprite.collide_mask(self,oponent)))
                #Tools.Logger.escribir("datos de los rectÃ¡ngulos: " + str(self.mask) + " y " + str(oponent.mask))
                #Tools.Logger.escribir("sus posisiones son " + str(self.pos) + " y " + str(oponent.pos) + " y segÃºn rectÃ¡ngulos: " + str(self.rect.center) + " y " + str(oponent.rect.center))



                self.currentState.control=True
                self.currentAnim=self.staticAnim
                self.framecount=0
                self.currentAnimFrame=0
            else:

                for i in range(0,self.maxSpeed):
                    oldpos=self.pos
                    oldrect=self.rect
                    oldmask = self.mask
                    if self.flip==True:
                        self.pos=(self.pos[0]-1,self.pos[1])
                    else:

                        self.pos=(self.pos[0]+1,self.pos[1])
                    self.rect.center=self.pos
                    self.mask=pygame.mask.from_surface(self.image)

                    if pygame.sprite.collide_mask(self,oponent) != None:
                        self.pos=oldpos
                        self.rect=oldrect
                        self.mask=oldmask
                        self.currentAnim=self.staticAnim
                        self.framecount=0
                        self.currentAnimFrame=0
                        self.currentState.control=True
                        self.framecount=0
                        break

                


        if self.currentAnim=="BWalk":
            self.currentState.control=False
            self.currentState.block=True
            
            if  self.flip:
                for i in range(0,self.maxSpeed):
                    oldpos=self.pos
                    oldrect=self.rect
                    oldmask = self.mask
                    self.pos=(self.pos[0]+1,self.pos[1])
                    self.rect.center=self.pos
                    self.mask=pygame.mask.from_surface(self.image)

                    if self.pos[0] >= 1020:
                        self.pos=oldpos
                        self.rect=oldrect
                        self.mask=oldmask
                        self.currentAnim=self.staticAnim
                        self.framecount=0
                        self.currentAnimFrame=0
                        self.currentState.control=True
                        self.framecount=0
                        self.currentState.block=False
                        break

            else:
                for i in range(0,self.maxSpeed):
                    oldpos=self.pos
                    oldrect=self.rect
                    oldmask = self.mask
                    self.pos=(self.pos[0]-1,self.pos[1])
                    self.rect.center=self.pos
                    self.mask=pygame.mask.from_surface(self.image)

                    if self.pos[0] <= 0:
                        self.pos=oldpos
                        self.rect=oldrect
                        self.mask=oldmask
                        self.currentAnim=self.staticAnim
                        self.framecount=0
                        self.currentAnimFrame=0
                        self.currentState.control=True
                        self.framecount=0
                        self.currentState.block=False
                        break



        #if self.currentAnim == 'FrontDash':
            #print "wac"

            


    def setSounds(self):
        if self.sounds.has_key(self.currentAnim):
            for snditem in self.sounds[self.currentAnim]:
                if int(snditem[0]) == self.framecount:
                    self.currentSounds.append(snditem[1])
                    if self.currentState.flags.has_key('Hit'):
                        self.currentSounds.append(snditem[2])




