#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase en la cual se incluyen diferentes métodos para detectar coliciones entre golpes de los personajes. En un futuro aquí se implementará de manera más óptima la utilización de hitboxes"""
import pygame
import Tools

# return 1 es daÃ?Â±o nulo
# return 2 es daÃ?Â±o completo
# return 0 es daÃ?Â±o reducido por defensa

def Golpe_Superior(colision, altura_1, altura_2, defensa):
    Tools.Logger.escribir("verificando coliciones en mÃ©todo")
    if defensa == True:
        if colision == None:
            return 1
        else:
            for x in range((altura_1 + 200)/3, (altura_1 + 200)*2/3):
                for y in range(altura_2, altura_2 + 200):
                    if x == y:
                        return 0
    else:
        if colision == None:
            return 1
        else:
            for x in range((altura_1 + 200)/3, (altura_1 + 200)*2/3):
                for y in range(altura_2, altura_2 + 200):
                    if x == y:
                        return 2
            return 1

def Golpe_Inferior(colision, altura_1, altura_2, defensa):
    if defensa == True:
        if colision == None:
            return 1
        else:
            for x in range((altura_1 + 200)*2/3, (altura_1 + 200)):
                for y in range(altura_2, altura_2 + 200):
                    if x == y:
                        return 0
    else:
        if colision == None:
            return 1
        else:
            for x in range((altura_1 + 200)*2/3, (altura_1 + 200)):
                for y in range(altura_2, altura_2 + 200):
                    if x == y:
                        return 2
            return 1

