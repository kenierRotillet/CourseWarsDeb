#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core
import Sound
import random
screen_w = 1024
screen_h = 768


def main(seleccion):
    pygame.init()
    

    pantalla = pygame.display.set_mode((screen_w,screen_h))
    if seleccion[0] == 3:

        personaje = Core.Medic.Medic(1,(-50,200))
    elif seleccion[0] == 1:
        personaje = Core.Engineer.Engineer(1,(-50,200))
    else:
        print ("error en la selección de personajes. no existe el index "+str(seleccion[0]))
        
        Sound.soundPlayer.simpleplay("sfx/error.wav")
        raw_input()
        return


    if seleccion[1] == 3:

        p2 = Core.Medic.Medic(2,(400,200))
    elif seleccion[1] == 1:
        p2 = Core.Engineer.Engineer(2,(400,200))
    else:
        print ("error en la selección de personajes. no existe el index "+str(seleccion[1]))
        Sound.soundPlayer.simpleplay("sfx/error.wav")
        raw_input()
        return

    

    
    #Tools.Logger.escribir(str(personaje.sounds))

    pygame.display.set_caption("CourseWars: 40 fps")
    relojito = pygame.time.Clock()
    tiempo = 0
    teclastotales = []
    teclastotalesp2=[]
    mapa = random.randint(1,9)
    fondo,rect = Tools.FastMethods.load_image("Screens/imgs/BG_0"+str(mapa)+".jpg")
    #fondo,rect = Tools.FastMethods.load_image("Screens/imgs/BG_09.jpg")
    Salida = False
    fps = 40
    Sound.soundPlayer.bgmPlay("bgm/battle"+str(mapa)+".mp3")
    while Salida==False:
        #print("posp1" + str(personaje.pos[0]) + ", " + str(personaje.pos[1]))
        #print("posp2" + str(p2.pos[0]) + ", " + str(p2.pos[1]))
        pantalla.blit(fondo,(0,0))
        teclas= []
        teclup = []
        relojito.tick_busy_loop(fps)
        pygame.display.set_caption("course wars: " + str(fps) +  " fps")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Salida=True


            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Salida=True
                elif event.key == K_F1:
                    fps+=5
                elif event.key == K_F2:
                    fps-=5
                    if fps <1:
                        fps=5

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
        personaje.setHitboxes()
        p2.setHitboxes()


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

                
                
                













