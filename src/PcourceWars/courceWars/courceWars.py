#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
Módulo principal, se encarga de llevar el control y flujo del juego, además de conectar el núcleo con la visualización"""
import pygame
pygame.init()

import Core
import Tools

import Screens

pygame.init()
pygame.mixer.init(frequency=22050, size=16, channels=2, buffer=32)

pygame.display.init()

print "start"




print("fin")
#raw_input()




Tools.FastMethods.loadKeys()

Screens.PlayWindow.main()
