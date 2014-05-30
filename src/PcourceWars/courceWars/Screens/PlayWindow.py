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
import PowerBars
import Timer
import RoundBars
screen_w = 1024
screen_h = 768


def main(seleccion):
    pygame.init()
    Sound.soundPlayer.bgmPlay("bgm/loading.mp3")

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
    
    
    
    fps=50 
    round = 1
    waitTime = fps*2
    p1win =0
    p2win=0
    fighting = False





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
    
    Sound.soundPlayer.bgmPlay("bgm/battle"+str(mapa)+".mp3")
    Barra1=HealthBars.HP_Bar(pantalla,1)
    Barra2=HealthBars.HP_Bar(pantalla,2)
    Power1=PowerBars.Power_Bar(pantalla,1)
    Power2=PowerBars.Power_Bar(pantalla,2)
    BarraVida1=Tools.FastMethods.load_image("Screens/imgs/MarcoVida1.png")
    BarraVida2=Tools.FastMethods.load_image("Screens/imgs/MarcoVida2.png")
    BarraRound1=RoundBars.Round_Bar(pantalla,1)
    BarraRound2=RoundBars.Round_Bar(pantalla,2)
    Fight=Tools.FastMethods.load_image("Screens/imgs/Fight.png")
    P1WIN=Tools.FastMethods.load_image("Screens/imgs/P1win.png")
    P2WIN=Tools.FastMethods.load_image("Screens/imgs/P2win.png")
    tempo = 50
    Contador=Timer.Time(tempo,439,2,481,55,512)#(tiempo,x.reloj,y.reloj,x.num1,y.num,z.num2)
    endType=0

    while Salida==False:
        #print("posp1" + str(personaje.pos[0]) + ", " + str(personaje.pos[1]))
        #print("posp2" + str(p2.pos[0]) + ", " + str(p2.pos[1]))
        pantalla.blit(fondo,(0,0))
        teclas= []
        teclup = []
        joyax=[]
        joyhats=[]
        joybtdown=[]
        joybtup=[]

        relojito.tick_busy_loop(fps)
        pygame.display.set_caption("course wars: " + str(fps) +  " fps")
        if fighting==False:
            if p1win<2 and p2win<2:
                contador = 0
                pantalla.blit(Fight,(100,100))
                while contador < waitTime:
                    
                    relojito.tick_busy_loop(fps)
                    pantalla.blit(fondo,(0,0))
                    personaje.update()
                    p2.update()
                    Sound.soundPlayer.playSounds(personaje)
                    Sound.soundPlayer.playSounds(p2)
                    
                    pantalla.blit(personaje.image,personaje.rect)
                    pantalla.blit(p2.image,p2.rect)
                    pygame.display.flip()
                    

                    
                    if contador ==0:
                        Sound.soundPlayer.playSysSound('Round'+str(round))

                       
                    if contador==waitTime-1:
                        Sound.soundPlayer.playSysSound('Fight')

    
                        
                    contador+=1 
                fighting=True
                personaje.totalControl=True
                p2.totalControl=True
                pygame.event.clear()
            else:
                if p1win==2:
                    personaje.setAnim('Taunt')
                else:
                    p2.setAnim('Taunt')
                contador = 0
                while contador < waitTime:
                    relojito.tick_busy_loop(fps)
                    pantalla.blit(fondo,(0,0))
                    personaje.update()
                    p2.update()
                    Sound.soundPlayer.playSounds(personaje)
                    Sound.soundPlayer.playSounds(p2)
                    
                    pantalla.blit(personaje.image,personaje.rect)
                    pantalla.blit(p2.image,p2.rect)

                    pygame.display.flip()
                    contador+=1
                pygame.event.clear()
                return



                    











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
                    teclas.append(event)
            if event.type == KEYUP:
                teclup.append(event)
            if event.type == JOYBUTTONDOWN:
                joybtdown.append(event)
            if event.type == JOYBUTTONUP:
                joybtup.append(event)
            if event.type == JOYAXISMOTION:
                joyax.append(event)
            if event.type == JOYHATMOTION:
                joyhats.append(event)





        p1liv = personaje.checkStatus(p2)
        p2liv = p2.checkStatus(personaje)
        if p1liv == False or p2liv == False or Contador.Tiempo()==0:
            Contador.detener()
            personaje.totalControl=False
            p2.totalControl=False
            fps=10
            if endType==0:
                if Contador.Tiempo()==0:
                    endType='TimeUp'
                
                elif round<3 and (personaje.currentAnim=='Special' or p2.currentAnim=='Special'):
                    endType='SuperEnd'
                elif round==3 and (personaje.currentAnim=='Special' or p2.currentAnim=='Special'):
                    endType='HiperEnd'
                else:
                    endType='End'
                Sound.soundPlayer.playSysSound(endType)



            
            if p1liv==False and p2.currentAnim !='Stand' and personaje.currentAnim!='Death':
                personaje.setAnim('Death',img=1)
            if p2liv==False and personaje.currentAnim!='Stand' and p2.currentAnim!='Death':
                p2.setAnim('Death',img=1)


            if personaje.currentAnim=='Stand' and p2.currentAnim=='Stand':

                fighting=False
                fps=50
                round+=1
                endType=0
                if p2liv==False or (personaje.currentHP>p2.currentHP):
                    p1win+=1
                    personaje.setAnim('Taunt')


                elif p1liv==False or (p2.currentHP > personaje.currentHP):
                    p2win+=1
                    p2.setAnim('Taunt')
                else:
                    round-=1

                contador=-25
                while contador <= waitTime:
                    relojito.tick_busy_loop(fps)
                
                    pantalla.blit(fondo,(0,0))    
                    personaje.update()
                    p2.update()
                    Sound.soundPlayer.playSounds(personaje)
                    Sound.soundPlayer.playSounds(p2)
                    contador+=1
                    pantalla.blit(personaje.image,personaje.rect)        
                    pantalla.blit(p2.image,p2.rect)
                    Barra1.draw(personaje.currentHP)
                    Barra2.draw(p2.currentHP)
                    Power1.draw(personaje.power)
                    Power2.draw(p2.power)
                    BarraRound1.draw(p1win)
                    BarraRound2.draw(p2win)
                    #pantalla.blit(BarraVida1,(27,30))
                    #pantalla.blit(BarraVida2,(592,28))
        
                    Contador.update(pantalla)
                    pygame.display.flip()

        



                personaje.recetPersonaje()
                p2.recetPersonaje()
                Contador.Reset(tempo)








        
        k1 = Tools.FastMethods.detectKeys(teclas,buttons=joybtdown,hats=joyhats,axis=joyax)
        k2 =Tools.FastMethods.detectKeys(teclas,player=2,buttons=joybtdown,hats=joyhats,axis=joyax)
        if k1 != "":

            teclastotales.append((tiempo,k1))
            personaje.lookCommand(teclastotales,tiempo)
        if k2 != "":
            teclastotalesp2.append((tiempo, k2))
            
            p2.lookCommand(teclastotalesp2,tiempo)
        
        keyup1 = Tools.FastMethods.detectKeys(teclup,release=True,buttons=joybtup,hats=joyhats,axis=joyax)
        keyup2 = Tools.FastMethods.detectKeys(teclup,player=2,release=True,buttons=joybtup,hats=joyhats,axis=joyax)
        personaje.lookCommand(keyup1,tiempo,True)
        p2.lookCommand(keyup2,tiempo,True)

        
        personaje.setHitboxes()
        p2.setHitboxes()

        personaje.DoAction(p2)
        p2.DoAction(personaje)

        

        personaje.update()
        p2.update()
        Sound.soundPlayer.playSounds(personaje)
        Sound.soundPlayer.playSounds(p2)
        rc1 = pantalla.blit(personaje.image,personaje.rect)
        
        rc2 = pantalla.blit(p2.image,p2.rect)
        
        





        
        if hitboxesDebug==True:
            Tools.Logger.escribir("Debug zone \n rect orijinal p1 " + str(personaje.rect) + " y el centro: " + str(personaje.rect.center) + "\n rect de imagen p1" + str(rc1) + " centro " + str(rc1.center))
            Tools.Logger.escribir("rect original p2"+ str(p2.rect) + " y centro: " + str(p2.rect.center) + "\n rect imagen p2 " + str(rc2) + " y el centro " + str(rc2.center))
            pygame.draw.circle(pantalla, (0,255,255),personaje.pos,5,0)
            pygame.draw.circle(pantalla, (255,255,0),p2.pos,5,0)
             

            putHitboxes(pantalla, personaje.currentHitboxes,personaje.bodyRect,True)
            putHitboxes(pantalla,p2.currentHitboxes,p2.bodyRect,True)

        Barra1.draw(personaje.currentHP)
        Barra2.draw(p2.currentHP)
        Power1.draw(personaje.power)
        Power2.draw(p2.power)
        BarraRound1.draw(p1win)
        BarraRound2.draw(p2win)
        #pantalla.blit(BarraVida1,(27,30))
        #pantalla.blit(BarraVida2,(592,28))
        
        Contador.update(pantalla)

        #print(Contador.Tiempo())

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
        

