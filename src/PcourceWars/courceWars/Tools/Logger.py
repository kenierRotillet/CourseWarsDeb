#!/usr/bin/python
# -*- coding: latin-1 -*-
"""módulo de control de loggin, para reportar errores o acciones durante el debug"""

import time

flag = False

def escribir(texto):
    """método para escribir un mensaje en el log. Simple, y sensillo, recibe la cadena a escribir."""
    if flag==True:

        arch = open("log.log", 'a')
        arch.write(texto+"\n")
        arch.close()



