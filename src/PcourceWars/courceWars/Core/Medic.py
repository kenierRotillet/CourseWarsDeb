#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame

class Medic(Core.Personaje.Personaje):
    """ Clase que reprecenta al personaje del médico. """

    def __init__(self, player,initPos):
        Core.Personaje.Personaje.__init__(self,player)
        """constructor de la clase del médico, recibe por entrada el número de jugador que le corresponde y su posición inicial"""
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Medic/Medic.anim")
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])
        self.masc = pygame.mask.from_surface(self.image)
        self.commands=Tools.FastMethods.load_commands("Chars/Medic/Medic.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Medic/Medic.snd")

        self.pos=initPos
        self.rect.center = (self.pos)
        self.maxSpeed = 3
        self.dashspeed=8
        
        
        






