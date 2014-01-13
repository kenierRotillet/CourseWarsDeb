#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core

screen_w = 1024
screen_h = 768


def main():
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=64)

    pantalla = pygame.display.set_mode((screen_w,screen_h))
    personaje = Core.Medic.Medic(1)
    pygame.display.set_caption("lalalal test")
    relojito = pygame.time.Clock()
    tiempo = 0
    teclastotales = []
    while True:
        teclas= []
        relojito.tick_busy_loop(40)
        
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return


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

        personaje.update()
        pantalla.blit(personaje.image,personaje.rect.center)



        personaje.DoAction(personaje)

        tiempo+=1

                
                
                













