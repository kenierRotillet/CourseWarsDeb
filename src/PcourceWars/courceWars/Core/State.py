#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Clase que sirve para definir los estados en los cuales se encuentra un personaje"""
import pygame
class State(object):
    """Clase que define un estado posible y sus características para cada personaje e instancia de la pelea"""
    def __init__(self, typenumber, control=True, jump=False,Block=False,crouch=False, **flags):
        """clase que representa un estado; un estado contiene todas las condiciones y definiciones que muestran el cómo está, o qué hace un personaje en cada frame."""
        object.__init__(self)
        self.control = control #Flag que indica si en este frame el jugador tiene o no control del personaje
        self.typenumber = typenumber #Identificador numérico del estado, sirve para desencadenar kombos o identificar estados específicos
        self.flags = flags #diccionario de flags extras que se pueden crear dinámicamente, según la programación del personaje lo requiera
        self.jump = jump #flag que indica si el personaje está en el aire o en tierra 
        self.crouch = crouch #flag que indica si el personaje está agachado  o no 
        self.block = Block #flag que indica si el personaje está defendiéndose
        



