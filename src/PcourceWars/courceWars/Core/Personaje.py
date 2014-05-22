#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase base que define aspectos bÃ¡sicos y funciones estÃ¡ndar para cada personaje"""
import pygame
from pygame.locals import *
import State
import Tools
import Collicion


class Personaje(pygame.sprite.Sprite):
    """ Clase de personaje. Recibe nÃºmero de jugador """
    def __init__(self, player,initPos):
        pygame.sprite.Sprite.__init__(self)
        """constructor de la clase del personaje. maneja y tiene todas las funcionalidades en comÃºn para cada personaje, como reconocimiento de convinaciÃ³n de teclas, actualizaciÃ³n de frames, interpretaciÃ³n de sonidos y programaciÃ³n de movimientos comunes."""

        self.currentState = State.State(0,True) #estado en el que se encuentra el personaje actualmente #estado en el que se encuentra actualmente, se inicializa como estado 0 y con control.
        self.maxHP = 100
        self.currentHP = self.maxHP #cantidad mÃ¡xima de hp y cantidad actual de hp
        self.atk = 10 #poder de ataque, para cÃ¡lculo de daÃ±o futuro
        self.deff= 10 #valor de defensa  para cÃ¡lculo de daÃ±o futuro
        self.power=0 #cantidad de carga inicial
        self.maxpower=100 #cantidad de poder mÃ¡ximo
        self.topWidth = 1024
        self.topHeight = 768

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
        self.currentAnimImage=0 #Indice del sprite actual en la animaci�n actual.
        self.pos = (0,0) #posiciÃ³n por defecto de inicio
        self.flip = False #flag que indica si es necesario o no voltear la imagen
        self.hold = False #flag que se sabe si es un comando que requiere mantener tecla
        self.hitboxes = {} #diccionario que almasena todos los hitboxes y damageboxes para cada frame de cada animacion
        self.currentHitboxes = [] #lista que almacena los hitboxes del frame actual
        self.bodyRect = pygame.rect.Rect(0,0,125,200) #rect que funciona como el cuerpo del personaje

        
        if self.player == 2:
            self.flip=True #si se es jugador dos, habilitar el flip 

        Tools.Logger.escribir("inicializando jugador " + str(self.player) + " con datos por defecto " + str(self) + " con posici�n " + str(initPos))



    def move(self, xmove,ymove, tope):
        """m�todo para mover la posici�n del personaje. Retorna true si el movimiento fue completo, retorna False en el caso de que el movimiento se interrumpiese."""
        Tools.Logger.escribir("moviendo en el vector: " + str(xmove) + ", " + str(ymove)) 
        malo=False
        val = self.bodyRect
        xfactor = 1
        yfactor = 1
        if xmove < 0:
            xfactor=-1
        if ymove < 0:
            yfactor=-1
        for x in range(0,abs(xmove)):
            val.centerx = val.centerx+xfactor
            if val.left < 0 or val.right > self.topWidth or val.colliderect(tope) == True:
                Tools.Logger.escribir("Rechasado avance, valor actual" + str(val) + ", con valor de colici�n" + str(val.colliderect(tope)) + " y el tope: " + str(tope))
                val.centerx = val.centerx - xfactor
                malo=True
                break
        for y in range(0,abs(ymove)):
            val.centery = val.centery+yfactor
            if val.centery > self.topHeight or val.centery < 0 or val.colliderect(tope) == True:
                Tools.Logger.escribir("Rechasado avance, valor actual" + str(val) + ", con valor de colici�n" + str(val.colliderect(tope)) + " y el tope: " + str(tope))
                val.centery = val.centery - yfactor
                malo=True
                break

            
        self.bodyRect= val
        self.rect.center=self.bodyRect.center
        self.pos = self.rect.center
        return malo

    def update(self):
        """m�todo que actualiza frame a frame el sprite de la animaci�n actual."""
        Tools.Logger.escribir(" actualizando imagen: \n animaci�n: " + self.currentAnim + ", n�mero de imagen: " + str(self.currentAnimImage) + " y n�mero de frame: " + str(self.framecount))
        Tools.Logger.escribir(" datos actuales: " + str(self.anims[self.currentAnim][self.currentAnimImage])+ "\n los datos siguientes: " + str(self.anims[self.currentAnim][self.currentAnimImage+1]))

        #se asume que toda animaci�n se inicia en el frame 0 por lo que nunca se verifica si framecount es igual al n�mero de frame de inicio de la primera imagen. y cuando en vez de tener un objeto imagen contiene un -1 significa fin de la animaci�n y retorno a stand
        if self.framecount==self.anims[self.currentAnim][self.currentAnimImage+1][0]:
            if self.anims[self.currentAnim][self.currentAnimImage+1][1] == -1:
                Tools.Logger.escribir("retornando a Stand: \n" + str(self.anims[self.currentAnim][self.currentAnimImage+1]))
                self.currentAnim='Stand'
                self.currentAnimImage=0
                self.framecount=0
            else:
                self.currentAnimImage=self.currentAnimImage+1
                self.framecount+=1
        else:
            self.framecount+=1

        if self.flip==False:
            self.image=self.anims[self.currentAnim][self.currentAnimImage][1]
        else:
            self.image=Tools.FastMethods.flipImage(self.anims[self.currentAnim][self.currentAnimImage][1])

        self.rect=self.image.get_rect()
        self.rect.center=self.pos

        
        self.mask=pygame.mask.from_surface(self.image)

        

    def lookCommand(self, keys,currentTime,KeyUP = False):
        #Tools.Logger.escribir("teclas ingresadas en el tiempo: " + str(currentTime))
        #Tools.Logger.escribir(str(keys))
        if KeyUP==True:
            for k in keys:
                if self.currentAnim=='Walk' or self.currentAnim == 'FrontDash':
                    if k == 'F' or (k == 'B' and self.flip == True):
                        self.currentAnim='Stand'
                        self.currentAnimImage=0
                        self.framecount=0
                elif self.currentAnim=='BWalk' or self.currentAnim=='BackDash' or self.currentAnim=='Block':
                    if k == 'B' or (k == 'F' and self.flip == True):
                        self.currentAnim='Stand'
                        self.currentAnimImage=0
                        self.framecount=0
                        self.currentState.block=False
                elif self.currentAnim=='Down':
                    if k == 'D':
                        self.currentAnim='Stand'
                        self.currentAnimImage=0
                        self.framecount=0
                        self.currentState.crouch = False
                elif self.currentAnim=='Down_LightPunch' or self.currentAnim=='Down_HighPunch':
                    if k == 'D':
                        self.currentState.crouch=False

            self.currentState.control=True

            return

        
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
                self.currentAnimImage=0
                self.framecount=0
                tolerancy=len(cmd[1][1])
                    #print "hay tecla"
                
            for k in range(0,len(keystroke)):
                keys.append(keystroke[-1 - k])



    def DoAction(self,oponent):
        """M�todo que registra y revisa los diferentes comandos para los personajes """

        """mÃ©todo en el cual se programan cada uno de los movimientos de los ataques y acciones bÃ¡sicas de un personaje, movimiento, golpes bÃ¡sicos, y coliciones. El mÃ©todo recibe al oponente, siendo capaz de alterar su posiciÃ³n y estado, e incluso animaciÃ³n."""

        
        
        if self.currentAnim == 'LightPunch':
            if self.currentState.crouch==True:
                self.currentAnim = 'Down_LightPunch'
                return
            self.currentState.control = False
            #Tools.Logger.escribir("comprovando golpes")
            if self.framecount>=3:
                print("ejecuntando colision")
                Collicion.ejecutarHit(self,oponent)
                    

        if self.currentAnim == 'MediumPunch':
            if self.currentState.crouch==True:
                self.currentAnim = 'Down_LightPunch'
                return
            self.currentState.control = False
            #Tools.Logger.escribir("comprovando golpes")
            if self.framecount==2:
                Collicion.ejecutarHit(self,oponent)

        if self.currentAnim == 'HighPunch':
            if self.currentState.crouch==True:
                self.currentAnim = 'Down_HighPunch'
                return
            self.currentState.control = False
            #Tools.Logger.escribir("comprovando golpes")
            if self.framecount>=2:
                Collicion.ejecutarHit(self,oponent)


        if self.currentAnim== 'Down_LightPunch' and (self.currentState.crouch==True):
            self.currentState.control = False
            if self.framecount==2:
                Collicion.ejecutarDownHit(self,oponent)
            if  self.currentAnimImage==len(self.anims[self.currentAnim])-2 and (self.framecount == int(self.anims[self.currentAnim][-1][0])):
                Tools.Logger.escribir("actual estado es golpe agachado debil" + self.currentAnim)
                if self.currentState.crouch==True:
                    self.AnimFrame=2
                    self.framecount=5
                    self.currentAnim='Down'                
                    self.currentState.crouch=True
                Tools.Logger.escribir(" estado abajo")

        if self.currentAnim== 'Down_HighPunch' and (self.currentState.crouch==True):
            self.currentState.control = False
            if self.framecount==3:
                Collicion.ejecutarDownHit(self,oponent)
            if  self.currentAnimImage==len(self.anims[self.currentAnim])-2 and (self.framecount == int(self.anims[self.currentAnim][-1][0])):
                Tools.Logger.escribir("actual estado es golpe agachado " + self.currentAnim + " " +str(self.currentAnimImage) + " "+ str(self.framecount))
                if self.currentState.crouch==True:

                    self.currentAnimImage=2
                    self.framecount=5
                    self.currentAnim='Down'
                    self.currentState.crouch=True
                Tools.Logger.escribir("actual estado es debe quedarse abajo" + self.currentAnim + self.currentAnim + " " +str(self.currentAnimImage) + " "+ str(self.framecount))
                

        if self.currentAnim=='Walk':
            fin = False
            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 0
                self.framecount=0
            if self.flip==True:
                fin = self.move(-1*self.maxSpeed,0,oponent.bodyRect)
            else:
                fin = self.move(self.maxSpeed,0,oponent.bodyRect)
            if fin == True:
                self.currentAnim='Stand'
                self.currentState.control=True





        if self.currentAnim=="BWalk":
            
            self.currentState.block=True
            fin = False
            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 0
                self.framecount=0
            if self.flip==True:
                fin = self.move(self.maxSpeed,0,oponent.bodyRect)
            else:
                fin = self.move(-1*self.maxSpeed,0,oponent.bodyRect)
            if fin == True:
                self.currentState.control=True
                self.currentAnim='Stand'





        if self.currentAnim == 'FrontDash':
            fin = False
            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 0
                self.framecount=0
            if self.flip==True:
                fin = self.move(-1*self.dashspeed,0,oponent.bodyRect)
            else:
                fin = self.move(self.dashspeed,0,oponent.bodyRect)
            if fin == True:
                self.currentAnim='Stand'
                self.currentState.control=True


        if self.currentAnim=="BackDash":           
            

            self.currentState.block=True
            fin = False
            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 0
                self.framecount=0
            if self.flip==True:
                fin = self.move(self.dashspeed,0,oponent.bodyRect)
            else:
                fin = self.move(-1*self.dashspeed,0,oponent.bodyRect)
            if fin == True:
                self.currentAnim='Stand'
                self.currentState.control=True 

        if self.currentAnim=="Down":
            self.currentState.crouch = True
            self.currentState.control=True

            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 2
                self.framecount=5

        if self.currentAnim=='Jump':
            self.currentState.jump=True            
            if self.currentAnimImage == len(self.anims[self.currentAnim])-2:
                self.currentAnimImage= 0
                self.framecount=0


    def setSounds(self):
        if self.sounds.has_key(self.currentAnim):
            for snditem in self.sounds[self.currentAnim]:
                if int(snditem[0]) == self.framecount:
                    self.currentSounds.append(snditem[1])
                    if self.currentState.flags.has_key('Hit'):
                        self.currentSounds.append(snditem[2])
                        del self.currentState.flags['Hit']
        #Tools.Logger.escribir(", seteados los sonidos")





    def checkStatus(self, oponent):
        """M�todo que chequea el estado del personaje (observando al oponente) tanto en t�rminos de flip, estados de par�lisis, t�rmino de defensa, etc."""
        Tools.Logger.escribir(self.statusText())

        if oponent.pos[0] < self.pos[0]:
            self.flip=True
        else:
            self.flip=False
        
        if self.currentAnim=='Stand':
            self.currentState.control = True
            self.currentState.typenumber=0
            self.currentState.crouch = False

        if self.currentAnim != 'Stand' and self.currentAnim != 'Block' and self.currentAnim != 'BackDash' and self.currentAnim != 'BWalk':
            self.currentState.block=False

        

    def setHitboxes(self):
        """ m�todo que setea las hitboxes del frame actual"""
        
        if self.hitboxes.has_key(self.currentAnim):
            frames = self.hitboxes[self.currentAnim]
            for f in frames:
                if self.framecount==f[0]:
                    self.currentHitboxes=[]
                    #Tools.Logger.escribir("se cambiaron los hitboxes. hitboxes actuales son: \n" + str(self.currentHitboxes))
                    if self.flip==True:
                        for h in f[1]:
                            self.currentHitboxes.append(h[:])
                            self.currentHitboxes[-1][1]= -1*h[1]
                            Tools.Logger.escribir(str(h) + ", Est� al lado contrario, hitbox volteado: " + str(self.currentHitboxes[-1]))
                    else:
                        self.currentHitboxes=f[1][:]
                    Tools.Logger.escribir("se cambiaron los hitboxes. hitboxes actuales son: \n" + str(self.currentHitboxes))

                    break

            
        else:
            self.currentHitboxes=[]




    def setTop(self,w,h):
        self.topHeight=h
        self.topWidth=w
        Tools.Logger.escribir("cambiados los bordes a: " + str(self.topWidth) + ", " + str(self.topHeight))

    def statusText(self):
        return("jugador: " + str(self.player) + ", en estado " + self.currentAnim + ", en posici�n " + str(self.pos) + " y rect: " + str(self.rect)+", rect del cuerpo: " + str(self.bodyRect) +"\n")
