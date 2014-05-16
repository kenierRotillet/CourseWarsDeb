#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
Módulo principal, se encarga de llevar el control y flujo del juego, además de conectar el núcleo con la visualización"""
import pygame
pygame.init()
import logging
import Core
import Tools

import Screens
import Sound

log = logging.getLogger("theLogger")
log.setLevel(logging.DEBUG)
h1 = logging.FileHandler("log.log")
f = logging.Formatter("%(levelname)s %(asctime)s %(funcName)s %(lineno)d %(message)s")
h1.setFormatter(f)
h1.setLevel(logging.DEBUG)
log.addHandler(h1)



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
    print "error en la ejecución. Traceback en el log"
    Sound.soundPlayer.simpleplay("sfx/error.wav")
    Tools.Logger.escribir("error: " + str(mes))
    log.exception("datos del error")

