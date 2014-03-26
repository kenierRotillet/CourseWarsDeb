#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame
import Collicion

class Medic(Core.Personaje.Personaje):
    """ Clase que reprecenta al personaje del m�dico. """

    def __init__(self, player,initPos):
        Core.Personaje.Personaje.__init__(self,player)
        """constructor de la clase del m�dico, recibe por entrada el n�mero de jugador que le corresponde y su posici�n inicial"""
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Medic/Medic.anim")
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])
        self.mask = pygame.mask.from_surface(self.image)
        self.commands=Tools.FastMethods.load_commands("Chars/Medic/Medic.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Medic/Medic.snd")

        self.pos=initPos
        self.rect.center = (self.pos)
        self.maxSpeed = 5
        self.dashspeed=7
        
        
        
        
    def DoAction(self, oponent):
        """m�todo heredado para especificar los comandos / t�cnicas propias del m�dico"""

        
        if (self.currentAnim == 'MediumPunch'):
            self.currentState.control = False
            Tools.Logger.escribir("comprovando golpes")
            if self.framecount==2 or self.framecount == 5:
                Collicion.ejecutarHit(self,oponent)



        else:
            super(Medic, self).DoAction(oponent)





