#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core
import Sound
screen_w = 1024
screen_h = 768


def main():
    pygame.init()
    

    pantalla = pygame.display.set_mode((screen_w,screen_h))
    personaje = Core.Medic.Medic(1,(0,100))
    p2 = Core.Engineer.Engineer(2,(500,100))
    Tools.Logger.escribir(str(personaje.sounds))

    pygame.display.set_caption("lalalal test")
    relojito = pygame.time.Clock()
    tiempo = 0
    teclastotales = []
    fondo,rect = Tools.FastMethods.load_image("Screens/imgs/Fondo.jpg")
    while True:
        pantalla.blit(fondo,(0,0))
        teclas= []
        relojito.tick_busy_loop(40)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                else:
                    teclas.append(event.key)

        if len(teclas)>0:

            teclastotales.append((tiempo,Tools.FastMethods.convertKeys(teclas)))
            personaje.lookCommand(teclastotales,tiempo)
        #else:
            #Tools.Logger.escribir("no hay teclas en este loop")

        personaje.setSounds()
        p2.setSounds()


        personaje.update()
        p2.update()
        pantalla.blit(personaje.image,personaje.rect.center)
        pantalla.blit(p2.image,p2.rect.center)
        Sound.soundPlayer.playSounds(personaje)




        personaje.DoAction(personaje)
        pygame.display.flip()

        tiempo+=1

                
                
                













