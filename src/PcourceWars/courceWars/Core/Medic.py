#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame
import Collicion

class Medic(Core.Personaje.Personaje):
    """ Clase que reprecenta al personaje del médico. """

    def __init__(self, player,initPos):
        Core.Personaje.Personaje.__init__(self,player,initPos)
        """constructor de la clase del médico, recibe por entrada el número de jugador que le corresponde y su posición inicial"""
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Medic/Medic.anim")
        if self.flip==True:
            self.image=Tools.FastMethods.flipImage(self.anims['Stand'][0][1])
        else:
            self.image=self.anims['Stand'][0][1]
        self.rect=self.image.get_rect()

        
        self.mask = pygame.mask.from_surface(self.image)
        self.commands=Tools.FastMethods.load_commands("Chars/Medic/Medic.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Medic/Medic.snd")
        self.hitboxes=Tools.FastMethods.LoadHitboxesData("Chars/Medic/Medic.hbx")

        
        self.maxSpeed = 5
        self.dashspeed=9
        self.rect.left=initPos[0]
        self.rect.top=initPos[1]
        
        self.pos=(self.rect.centerx,self.rect.centery)
        self.bodyRect.center = self.rect.center


        Tools.Logger.escribir("inicializando al jugador " + str(self.player) + " como médico. Datos específicos " + str(self) + " posisión, y rect: " + str(self.pos) + ", " + str(self.rect))
        
        
        
    def DoAction(self, oponent):
        """método heredado para especificar los comandos / técnicas propias del médico"""

        
        if (self.currentAnim == 'MediumPunch'):
            self.currentState.control = False
            if self.currentState.crouch == True:
                super(Medic, self).DoAction(oponent)
                
            Tools.Logger.escribir("comprovando golpes")
            if self.framecount==2 or self.framecount == 5:
                Collicion.ejecutarHit(self,oponent)



        else:
            super(Medic, self).DoAction(oponent)





