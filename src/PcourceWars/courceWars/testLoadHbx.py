#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Sound

pygame.init()
print pygame.joystick.get_count()

joysticks =[]
for j in range(0,pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(j))
    joysticks[-1].init()
    print str(joysticks[-1].get_id()) + " y " + str(joysticks[-1].get_name())

    pantalla = pygame.display.set_mode((1024,768))

while True:
    for e in pygame.event.get():
        if e.type == JOYBUTTONDOWN:
            Sound.soundPlayer.simpleplay("sfx/f.wav")
            print "boton"
        if e.type == JOYAXISMOTION:
            Sound.soundPlayer.simpleplay("sfx/accept.wav")
            print("movimiento de eje: " + str(e.joy) + ", " + str(e.axis) + ", " + str(e.value))
        if e.type == JOYHATMOTION:
            Sound.soundPlayer.simpleplay("sfx/unable.wav")
            print("presionado un hat: " + str(e.joy) + ", " + str(e.hat) + ", " + str(e.value))



