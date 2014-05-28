#!/usr/bin/python
# -*- coding: latin-1 -*-
"""módulo de control de loggin, para reportar errores o acciones durante el debug"""

import time
import logging
import os
import pygame
flag = True
recet = True
if recet==True:
    try:
        os.remove("log.log")
        Recet=False
    except:
        #s= pygame.mixer.Sound("sfx/error.wav")
        #s.play()
        recet=False



log = logging.getLogger("theLogger")
log.setLevel(logging.DEBUG)
h1 = logging.FileHandler("log.log")
f = logging.Formatter("%(levelname)s %(asctime)s %(lineno)d %(message)s")
h1.setFormatter(f)
h1.setLevel(logging.DEBUG)
log.addHandler(h1)




def escribir(texto):
    """método para escribir un mensaje en el log. Simple, y sensillo, recibe la cadena a escribir."""
    

    if flag==True:
        log.debug(texto)

        


def excepcion():
    log.exception("rerror crítico: ")
    s= pygame.mixer.Sound("sfx/error.wav")
    s.play()
        
