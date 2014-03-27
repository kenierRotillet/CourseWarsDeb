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

pygame.mixer.music.load("bgm/ale.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

print("fin")
#raw_input()




Tools.FastMethods.loadKeys()

Screens.Start_Menu.main()
seleccion = Screens.Sel_PJ.main()
Screens.PlayWindow.main(seleccion)
