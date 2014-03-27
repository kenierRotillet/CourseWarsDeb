#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core
import Sound
screen_w = 1024
screen_h = 768


def main(seleccion):
    pygame.init()
    

    pantalla = pygame.display.set_mode((screen_w,screen_h))
    if seleccion[0] == 1:

        personaje = Core.Medic.Medic(1,(0,100))
    elif seleccion[0] == 3:
        personaje = Core.Engineer.Engineer(1,(0,100))


    if seleccion[1] == 1:

        p2 = Core.Medic.Medic(2,(500,100))
    elif seleccion[1] == 3:
        p2 = Core.Engineer.Engineer(2,(500,100))

    

    
    #Tools.Logger.escribir(str(personaje.sounds))

    pygame.display.set_caption("lalalal test")
    relojito = pygame.time.Clock()
    tiempo = 0
    teclastotales = []
    teclastotalesp2=[]
    fondo,rect = Tools.FastMethods.load_image("Screens/imgs/Fondo.jpg")
    while True:
        #print("posp1" + str(personaje.pos[0]) + ", " + str(personaje.pos[1]))
        #print("posp2" + str(p2.pos[0]) + ", " + str(p2.pos[1]))
        pantalla.blit(fondo,(0,0))
        teclas= []
        teclup = []
        relojito.tick_busy_loop(40)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                else:
                    teclas.append(event.key)
            if event.type == KEYUP:
                teclup.append(event.key)


        if len(teclas)>0:

            teclastotales.append((tiempo,Tools.FastMethods.convertKeys(teclas)))
            teclastotalesp2.append((tiempo, Tools.FastMethods.convertKeys(teclas,2)))
            personaje.lookCommand(teclastotales,tiempo)
            p2.lookCommand(teclastotalesp2,tiempo)
        elif len(teclup) > 0:
            keyup1 = Tools.FastMethods.convertKeys(teclup)
            keyup2 = Tools.FastMethods.convertKeys(teclup,2)
            personaje.lookCommand(keyup1,tiempo,True)
            p2.lookCommand(keyup2,tiempo,True)




        personaje.checkStatus(p2)
        p2.checkStatus(personaje)
        personaje.setSounds()
        p2.setSounds()


        personaje.update()
        p2.update()
        pantalla.blit(personaje.image,personaje.rect.center)
        pantalla.blit(p2.image,p2.rect.center)
        personaje.DoAction(p2)
        p2.DoAction(personaje)

        Sound.soundPlayer.playSounds(personaje)
        Sound.soundPlayer.playSounds(p2)





        

        pygame.display.flip()

        tiempo+=1

                
                
                













