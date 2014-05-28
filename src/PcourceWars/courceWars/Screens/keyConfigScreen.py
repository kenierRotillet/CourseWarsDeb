#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase que representa y maneja la ventana de configuración de teclas"""
import pygame
import Tools
import Sound
from pygame.locals import *

class keyConfigScreen(object):
    """Clase que maneja la ventana de configuración de teclas"""


    def __init__(self):
        self.width=1024
        self.height=768
        self.p1=Tools.FastMethods.p1keys
        self.p2=Tools.FastMethods.p2keys
        self.textKeys = ['a']
        self.textKeys.append('b')
        self.textKeys.append('c')
        self.textKeys.append('x')
        self.textKeys.append('s')
        self.textKeys.append('U')
        self.textKeys.append('F')
        self.textKeys.append('D')
        self.textKeys.append('B')
        self.font=pygame.font.SysFont('times',14)
        self.textPos=(250,150)






    def mainLoop(self):
        Sound.soundPlayer.bgmPlay("bgm/optionsmenu.mp3")
        self.pantalla = pygame.display.set_mode((self.width,self.height), FULLSCREEN)
        pygame.display.set_caption("Pantalla de configuración")
        self.salida=False
        while self.salida == False:
            self.setFondo()
            letra = self.font.render("Bienvenido a la pantalla de configuración de teclas. ¿Desea configurar las teclas del jugador 1?",True,(0,0,255))
            self.pantalla.blit(letra,self.textPos)
            pygame.display.flip()
            iniciar = self.confirmLoop()
            if iniciar==True:
                
                for i in range(0,len(self.textKeys)):
                    self.setKeyLoop(1,i)

                    letra = self.font.render("¿Desea configurar las teclas del jugador 2?",True,(0,0,255))
                    self.setFondo()
            self.pantalla.blit(letra,self.textPos)
            pygame.display.flip()
            iniciar = self.confirmLoop()
            if iniciar == True:

            

                for i in range(0,len(self.textKeys)):
                    self.setKeyLoop(2,i)

            letra = self.font.render("¿Desea guardar los cambios realizados?",True,(0,0,255))
            self.setFondo()
            self.pantalla.blit(letra,self.textPos)
            pygame.display.flip()
            iniciar = self.confirmLoop()
            if iniciar == True:
                Tools.KeyConfig.setManual(self.p1,self.p2)
                self.alertLoop("¡Éxito, cambios guardados!",True)



            self.salida=True 






    def confirmLoop(self,text=""):
        letras = ""
        while True:
            if text != "":
                letras=self.font.render(text,True,(0,0,255))
                self.setFondo()
                self.pantalla.blit(letras,self.textPos)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Sound.soundPlayer.playSysSound("Warn")
                        return False
                    elif event.key == K_RETURN:
                        Sound.soundPlayer.playSysSound("Accept")
                        return True








    def setKeyLoop(self,player,keyNum):
        currentKey = ""
        if player==1:

            currentKey = self.p1[keyNum][1]
        else:
            currentKey = self.p2[keyNum][1]

        letras = self.font.render("¿Desea cambiar la tecla \"" + self.textKeys[keyNum] + "\" que actualmente es " + str(currentKey) +"?",True,(0,0,255))
        self.setFondo()
        self.pantalla.blit(letras,self.textPos)
        pygame.display.flip()
        ok = self.confirmLoop()
        if ok == False:
            return
        pygame.event.clear()

        while True:
            letras = self.font.render("Presione el botón que desea para la tecla \""+self.textKeys[keyNum]+"\"",True,(0,0,255))
            self.setFondo()
            self.pantalla.blit(letras,self.textPos)
            pygame.display.flip()
            tkey = ""
            ok=False
            for e in pygame.event.get():
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        Sound.soundPlayer.playSysSound('Change')
                        return
                    else:
                        tkey=e.key
                elif e.type == JOYBUTTONDOWN:
                    tkey=str(e.joy)+"/b"+str(e.button)
                elif e.type == JOYAXISMOTION:
                    if e.value>=Tools.FastMethods.deadZone:

                        tkey=str(e.joy)+"/a"+str(e.axis)+"/+"
                    elif e.value <= -1*Tools.FastMethods.deadZone:
                        tkey=str(e.joy)+"/a"+str(e.axis)+"/-"

                elif      e.type == JOYHATMOTION:
                        tkey =str(e.joy)+"/h"+str(e.hat)+"/"+str(e.value)

            if tkey!="":
                Sound.soundPlayer.playSysSound('Move')

                ok = self.confirmLoop("¿Confirma a " + str(tkey) + " para \"" + self.textKeys[keyNum] + "\"? ")
            if ok == True:
                if player==1:
                    for t in range(0,len(self.p1)):
                        if self.p1[t][0]==self.textKeys[keyNum]:
                            self.p1.pop(t)
                            break



                    self.p1.append((self.textKeys[keyNum],tkey))
                    return

                else:
                    for t in range(0,len(self.p2)):
                        if self.p2[t][0]==self.textKeys[keyNum]:
                            self.p2.pop(t)
                            break



                    self.p2.append((self.textKeys[keyNum],tkey))
                    return

                    











    def alertLoop(self,text="",success=False):
        letras = ""
        if success == False:

            Sound.soundPlayer.playSysSound("Warn")
        else:
            Sound.soundPlayer.playSysSound("Confirm")

        while True:
            if text != "":
                letras=self.font.render(text,True,(0,0,255))
                self.setFondo()
                self.pantalla.blit(letras,self.textPos)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        Sound.soundPlayer.playSysSound("Accept")
                        return

    def setFondo(self):
        rect = pygame.rect.Rect(0,0,self.width,self.height)
        pygame.draw.rect(self.pantalla,(100,100,100),rect,0)