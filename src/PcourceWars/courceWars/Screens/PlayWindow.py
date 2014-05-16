#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core
import Sound
import random
import pygame.draw

screen_w = 1024
screen_h = 768


def main(seleccion):
    pygame.init()
    

    pantalla = pygame.display.set_mode((screen_w,screen_h), FULLSCREEN)
    posInicialP1= (100,420)
    posInicialP2=(600,420)
    if seleccion[0] == 3:

        personaje = Core.Medic.Medic(1,posInicialP1)
    elif seleccion[0] == 1:
        personaje = Core.Engineer.Engineer(1,posInicialP1)
    else:
        print ("error en la selección de personajes. no existe el index "+str(seleccion[0]))
        
        Sound.soundPlayer.simpleplay("sfx/error.wav")
        raw_input()
        return


    if seleccion[1] == 3:

        p2 = Core.Medic.Medic(2,posInicialP2)
    elif seleccion[1] == 1:
        p2 = Core.Engineer.Engineer(2,posInicialP2)
    else:
        print ("error en la selección de personajes. no existe el index "+str(seleccion[1]))
        Sound.soundPlayer.simpleplay("sfx/error.wav")
        raw_input()
        return

    

    
    #Tools.Logger.escribir(str(personaje.sounds))

    pygame.display.set_caption("CourseWars: 40 fps")
    relojito = pygame.time.Clock()
    tiempo = 0
    personaje.setTop(screen_w,screen_h)
    p2.setTop(screen_w,screen_h)
    teclastotales = []
    teclastotalesp2=[]
    hitboxesDebug=True
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

                elif event.key == K_F10:
                    hitboxesDebug= not hitboxesDebug
                    print("modo debug = " + str(hitboxesDebug))
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
        rc1 = pantalla.blit(personaje.image,personaje.rect)
        rc2 = pantalla.blit(p2.image,p2.rect)
        personaje.DoAction(p2)
        p2.DoAction(personaje)

        Sound.soundPlayer.playSounds(personaje)
        Sound.soundPlayer.playSounds(p2)





        
        if hitboxesDebug==True:
            Tools.Logger.escribir("rect orijinal p1 " + str(personaje.rect) + " y el centro: " + str(personaje.rect.center) + "rect de imagen p1" + str(rc1) + " centro " + str(rc1.center))
            Tools.Logger.escribir("rect original p2"+ str(p2.rect) + " y centro: " + str(p2.rect.center) + "rect p2 " + str(rc2) + " y el centro " + str(rc2.center))
            Tools.Logger.escribir("posisiones p1: " + str(personaje.pos) + " posicion p2 " + str(p2.pos))

            putHitboxes(pantalla, personaje.currentHitboxes,personaje.rect)
            putHitboxes(pantalla,p2.currentHitboxes,p2.rect)

        pygame.display.flip()

        tiempo+=1

                
                
                














def putHitboxes(screen,cajas,rect):
    for h in cajas:
        hitbox = pygame.rect.Rect(rect.left,rect.top,h[3],h[4])
        
        
        hitbox.center = (h[1]+rect.centerx,h[2]+rect.centery)
        if h[0] == 'd':
            rgb = [255,0,0]
        else:
            rgb = [0,0,255]
        print (str(hitbox)+", centro " + str(rect.center) + "  y original" + str(rect) + ", centro " + str(rect.center))
        fin = pygame.draw.rect(screen,rgb,hitbox,2)
        print("resultante " + str(fin) + ", centro " + str(fin.center))
        

