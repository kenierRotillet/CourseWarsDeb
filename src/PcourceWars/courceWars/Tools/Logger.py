#!/usr/bin/python
# -*- coding: latin-1 -*-
"""m�dulo de control de loggin, para reportar errores o acciones durante el debug"""

import time
import logging
import os
import pygame
import sys
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
        recet=False
        


log = logging.getLogger("theLogger")
log.setLevel(logging.DEBUG)
try:

    h1 = logging.FileHandler("log.log")
    f = logging.Formatter("%(levelname)s %(asctime)s %(lineno)d %(message)s")
    h1.setFormatter(f)
    h1.setLevel(logging.DEBUG)
    log.addHandler(h1)
except Exception:
    
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=64)
    soc= pygame.mixer.Sound("sfx/error.wav")
    soc.play()

    
    logging.exception("No se puede crear el log. Por favor cierre el archivo log.log que est� en uso")
    raw_input()
    
    sys.exit()
    






def escribir(texto):
    """m�todo para escribir un mensaje en el log. Simple, y sensillo, recibe la cadena a escribir."""
    

    if flag==True:
        log.debug(texto)

        


def excepcion():
    log.exception("rerror cr�tico: ")
    s= pygame.mixer.Sound("sfx/error.wav")
    s.play()
        
