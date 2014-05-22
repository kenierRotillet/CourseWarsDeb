#!/usr/bin/python
# -*- coding: latin-1 -*-
"""modulo que representa a la pantalla principal del juego"""
import pygame
from pygame.locals import *
import Tools
import Core
import Sound
import random
import pygame.draw
import HealthBars

screen_w = 1024
screen_h = 768


def main(seleccion):
    pygame.init()
    Sound.soundPlayer.bgmPlay("bgm/battle8.mp3")

    pantalla = pygame.display.set_mode((screen_w,screen_h))
    posInicialP1= (-100,220)
    posInicialP2=(450,220)
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

    pygame.display.set_caption("CourseWars: 50 fps")
    relojito = pygame.time.Clock()
    tiempo = 0
    personaje.setTop(screen_w,screen_h)
    p2.setTop(screen_w,screen_h)
    teclastotales = []
    teclastotalesp2=[]
    hitboxesDebug=False
    mapa = random.randint(1,9)
    fondo= Tools.FastMethods.load_image("Screens/imgs/BG_0"+str(mapa)+".png")
    #fondo= Tools.FastMethods.load_image("Screens/imgs/BG_09.png")

    Salida = False
    fps = 50
    Sound.soundPlayer.bgmPlay("bgm/battle"+str(mapa)+".mp3")
    Barra1=HealthBars.HP_Bar(pantalla,1)
    Barra2=HealthBars.HP_Bar(pantalla,2)
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
                    if fps == 6:
                        fps=5
                elif event.key == K_F2:
                    fps-=5
                    if fps <1:
                        fps=1

                elif event.key == K_F10:
                    hitboxesDebug= not hitboxesDebug
                    print("modo debug = " + str(hitboxesDebug))
                else:
                    teclas.append(event.key)
            if event.type == KEYUP:
                teclup.append(event.key)


        personaje.checkStatus(p2)
        p2.checkStatus(personaje)
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

        
        personaje.DoAction(p2)
        p2.DoAction(personaje)
        personaje.setHitboxes()
        p2.setHitboxes()

        personaje.setSounds()
        p2.setSounds()
        

        personaje.update()
        p2.update()
        rc1 = pantalla.blit(personaje.image,personaje.rect)
        
        rc2 = pantalla.blit(p2.image,p2.rect)
        
        Sound.soundPlayer.playSounds(personaje)
        Sound.soundPlayer.playSounds(p2)





        
        if hitboxesDebug==True:
            Tools.Logger.escribir("Debug zone \n rect orijinal p1 " + str(personaje.rect) + " y el centro: " + str(personaje.rect.center) + "\n rect de imagen p1" + str(rc1) + " centro " + str(rc1.center))
            Tools.Logger.escribir("rect original p2"+ str(p2.rect) + " y centro: " + str(p2.rect.center) + "\n rect imagen p2 " + str(rc2) + " y el centro " + str(rc2.center))
            pygame.draw.circle(pantalla, (0,255,255),personaje.pos,5,0)
            pygame.draw.circle(pantalla, (255,255,0),p2.pos,5,0)
             

            putHitboxes(pantalla, personaje.currentHitboxes,personaje.bodyRect,True)
            putHitboxes(pantalla,p2.currentHitboxes,p2.bodyRect,True)

        Barra1.draw(personaje.currentHP)
        Barra2.draw(p2.currentHP)
        
        pygame.display.flip()

        tiempo+=1        



def putHitboxes(screen,cajas,rect,originalRect=False):
    if originalRect == True:
        rectcolor =(0,255,0)
        centerRect = pygame.draw.rect(screen,rectcolor,rect,1)
        Tools.Logger.escribir("Rect del cuerpo dibujado: " + str(rect) + "y su centro: " + str(rect.center) +  "\n  resultado del dibujo: " + str(centerRect) + ", centro: " + str(centerRect.center))


    for h in cajas:
        hitbox = pygame.rect.Rect(rect.left,rect.top,h[3],h[4])
        
        
        hitbox.center = (h[1]+rect.centerx,h[2]+rect.centery)
        if h[0] == 'd':
            rgb = [255,0,0]
        else:
            rgb = [0,0,255]
        Tools.Logger.escribir(str(hitbox)+", centro " + str(rect.center) + "  y original" + str(rect) + ", centro " + str(rect.center))
        fin = pygame.draw.rect(screen,rgb,hitbox,2)
        Tools.Logger.escribir("resultante " + str(fin) + ", centro " + str(fin.center))
        

