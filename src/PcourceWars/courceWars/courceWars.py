#!/usr/bin/python
# -*        - coding: latin-1 -*-
""" CourceWars: fighter en desarrollo para el proyecto recistencia arcade.
Módulo principal, se encarga de llevar el control y flujo del juego, además de conectar el núcleo con la visualización"""
import os
import pygame
import Tools
import Sound
Sound.soundPlayer.simpleplay("sfx/start.wav")
    

pygame.init()
import logging
import Core


import Screens
import Sound


log = logging.getLogger("theLogger")

try:

    pygame.init()


    pygame.display.init()

    print "start"   
    Tools.FastMethods.initJoysticks()
    Tools.FastMethods.loadKeys()
    while True:

        player = Screens.Start_Menu.main()
        pygame.init()
        if player =='KeyConfig':
            conf = Screens.keyConfigScreen.keyConfigScreen()
            conf.mainLoop()
            Tools.FastMethods.loadKeys()
            continue





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

