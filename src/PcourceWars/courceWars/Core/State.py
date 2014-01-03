#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase que sirve para definir los estados en los cuales se encuentra un personaje"""
import pygame
class State(object):
    """Clase que define un estado posible y sus características para cada personaje e instancia de la pelea"""
    def __init__(self, typenumber, control=True, jump=False,Block=False,crouch=False, *flags):
        object.__init__(self)
        self.control = control
        self.typenumber = typenumber
        self.flags = flags
        self.jump = jump
        self.crouch = crouch
        self.block = Block




