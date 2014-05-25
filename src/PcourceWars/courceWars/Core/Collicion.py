#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase en la cual se incluyen diferentes métodos para detectar coliciones entre golpes de los personajes. En un futuro aquí se implementará de manera más óptima la utilización de hitboxes"""
import pygame
import Tools
import Core.Personaje

# return 1 es daÃ?Â±o nulo
# return 2 es daÃ?Â±o completo
# return 0 es daÃ?Â±o reducido por defensa

def Golpe_Superior(colision, altura_1, altura_2, defensa):
    Tools.Logger.escribir("verificando coliciones en mÃ©todo")
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

def ejecutarHit(ataca,oponent):
    #print("Impacto")
    if Golpe_Superior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
        oponent.currentState.flags['Hit'] = True
        oponent.currentAnim = 'Block'
        oponent.framecount=0
        oponent.currentAnimImage=0
        oponent.currentState.control=False

        #Tools.Logger.escribir("hubo coliciÃ³n de golpe bloqueado")
    #elif Golpe_Superior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
        #Tools.Logger.escribir("fallÃ³ el golpe")
    elif Golpe_Superior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
        ataca.currentState.flags['Hit']=True
        oponent.currentAnim='Hit'
        oponent.currentAnimImage=0
        oponent.framecount=0
        #Tools.Logger.escribir("le achuntÃ³")
    listaATK=[]
    listaIMP=[]
    Impact = False
    for d in ataca.currentHitboxes:
        if d[0]=="d":
            rect=pygame.rect.Rect(0,0,d[3],d[4])
            rect.centerx=ataca.rect.centerx + d[1]
            rect.centery=ataca.rect.centery + d[2]
            listaATK.append(rect)
    for h in oponent.currentHitboxes:
        if h[0]=="h":
            rect=pygame.rect.Rect(0,0,h[3],h[4])
            rect.centerx=oponent.rect.centerx + h[1]
            rect.centery=oponent.rect.centery + h[2]
            listaIMP.append(rect)
    #print(listaATK)
    #print(listaIMP)
    #print("listas")

    for d in listaATK:
        print("hubieron:"+str(d.collidelist(listaIMP)))
        print(str(d))
        print(listaIMP)
        if d.collidelist(listaIMP)>=0:
            Impact = True
            break
    if Impact == True and oponent.currentState.block== True:
        oponent.currentAnim='Block'
        oponent.framecount=0
        oponent.currentAnimImage=0
        oponent.currentState.flags['Hit'] = True
    elif Impact == True:
        oponent.currentAnim='Hit'
        oponent.framecount=0
        oponent.currentAnimImage=0
        oponent.currentState.control=False        
        ataca.currentState.flags['Hit'] = True
    return Impact            

def ejecutarDownHit(ataca,oponent):
    if Golpe_Inferior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
        oponent.currentState.flags['Hit'] = True
        oponent.currentAnim = 'Block'
        oponent.framecount=0
        oponent.currentAnimImage=0
        oponent.currentState.control=False

        #Tools.Logger.escribir("hubo coliciÃ³n de golpe bloqueado")
    #elif Golpe_Superior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
        #Tools.Logger.escribir("fallÃ³ el golpe")
    elif Golpe_Inferior(pygame.sprite.collide_mask(ataca,oponent), ataca.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
        ataca.currentState.flags['Hit']=True
        oponent.currentAnim='Hit'
        oponent.currentAnimImage=0
        oponent.framecount=0
        #Tools.Logger.escribir("le achuntÃ³")

