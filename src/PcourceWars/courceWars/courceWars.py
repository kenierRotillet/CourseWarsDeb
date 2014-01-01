#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
Módulo principal, se encarga de llevar el control y flujo del juego, además de conectar el núcleo con la visualización"""

import Core
import Tools

print "start"

gak = Core.Personaje.Personaje(1)
print("fin")
raw_input()



comandos = Tools.FastMethods.LoadAnimData("chars/Medic/Medic.anim")
raw_input()
print comandos
raw_input()