#!/usr/bin/python
# -*- coding: latin-1 -*-
"""m�dulo de control de loggin, para reportar errores o acciones durante el debug"""

import time
def escribir(texto):
    """m�todo para escribir un mensaje en el log. Simple, y sensillo, recibe la cadena a escribir."""
    arch = open("log.log", 'a')
    arch.write(texto+"\n")
    arch.close()



