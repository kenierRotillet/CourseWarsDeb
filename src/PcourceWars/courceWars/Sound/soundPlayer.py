#!/usr/bin/python
# -*- coding: latin-1 -*-
"""módulo que se encarga de la reproducción de sonidos"""
import pygame
import Tools
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=64)
pygame.mixer.set_num_channels(64)

bgVolume =0.3
comonSounds = Tools.FastMethods.LoadSounds("cfg/sfx.snd")

def playSounds(personaje):
    """método qque reproduce la cola de sonidos del personaje entregado, en el frame actual."""
    #log.escribir("en cola hay " + str(len(personaje.currentSounds)))

    if len(personaje.currentSounds) >= 0:
        for snd in personaje.currentSounds:
            #log.escribir(str(snd))
            if snd == "":
                continue

            snd.play()
            


    personaje.currentSounds = []




def simpleplay(sfx):
    sonido = pygame.mixer.Sound(sfx)
    sonido.play()

def bgmPlay(bgm,vol=bgVolume):
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1)


def stopbgm():
    pygame.mixer.music.stop()

def playSysSound(sound):
    if comonSounds.has_key(sound):
        comonSounds[sound][0][1].play()

