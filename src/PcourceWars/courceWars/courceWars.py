#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
M�dulo principal, se encarga de llevar el control y flujo del juego, adem�s de conectar el n�cleo con la visualizaci�n"""

import Core
import Tools
import pygame
import Screens

pygame.init()
pygame.display.init()

print "start"
Tools.FastMethods.PlayAux()


gak = Core.Medic.Medic(1)

print("fin")
raw_input()




print gak.commands
raw_input()

Screens.PlayWindow.main()
