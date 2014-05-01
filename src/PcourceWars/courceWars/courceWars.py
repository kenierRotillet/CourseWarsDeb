#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
Módulo principal, se encarga de llevar el control y flujo del juego, además de conectar el núcleo con la visualización"""
import pygame
pygame.init()

import Core
import Tools

import Screens
import Sound

pygame.init()


pygame.display.init()

print "start"

print("fin")
#raw_input()




Tools.FastMethods.loadKeys()

player = Screens.Start_Menu.main()
pygame.init()

seleccion = Screens.Sel_PJ.main()
print seleccion
#raw_input()
pygame.mixer.music.load("bgm/Mighty Wind.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

Screens.PlayWindow.main(seleccion)



