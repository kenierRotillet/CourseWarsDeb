#!/usr/bin/python
# -*- coding: latin-1 -*-
"""m�dulo que se encarga de la reproducci�n de sonidos"""
import pygame
import Tools.Logger as log
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=64)

def playSounds(personaje):
    """m�todo qque reproduce la cola de sonidos del personaje entregado, en el frame actual."""
    log.escribir("en cola hay " + str(len(personaje.currentSounds)))

    if len(personaje.currentSounds) >= 0:
        for snd in personaje.currentSounds:
            log.escribir(str(snd))

            sonido = pygame.mixer.Sound(snd)
            sonido.play()


    personaje.currentSounds = []




