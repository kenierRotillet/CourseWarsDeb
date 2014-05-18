#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
M�dulo principal, se encarga de llevar el control y flujo del juego, adem�s de conectar el n�cleo con la visualizaci�n"""
import os

recetLog=True
if recetLog==True:
    try:
        os.remove("log.log")
    except:
        pass


import pygame
pygame.init()
import logging
import Core
import Tools

import Screens
import Sound


log = logging.getLogger("theLogger")

try:

    pygame.init()


    pygame.display.init()

    print "start"


    #raw_input()




    Tools.FastMethods.loadKeys()

    player = Screens.Start_Menu.main()
    pygame.init()

    seleccion = Screens.Sel_PJ.main()
    #print seleccion
    #raw_input()

    Screens.PlayWindow.main(seleccion)



    print("fin")
except Exception, mes:
    print "error en la ejecuci�n. Traceback en el log"
    Sound.soundPlayer.simpleplay("sfx/error.wav")
    Tools.Logger.escribir("error: " + str(mes))
    log.exception("datos del error")

