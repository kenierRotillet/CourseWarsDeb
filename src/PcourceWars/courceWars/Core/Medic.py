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

        if oponent.pos[0] < self.pos[0]:
            self.flip=True
        else:
            self.flip=False
        
        if self.currentAnim=='Stand':
            self.currentState.control = True
            self.currentState.typenumber=0

        if self.currentAnim != 'Stand' and self.currentAnim != 'Block' and self.currentAnim != 'BackDash' and self.currentAnim != 'BWalk':
            self.currentState.block=False

        
        if self.currentAnim == 'MediumPunch':
            self.currentState.control = False
            Tools.Logger.escribir("comprovando golpes")
            if self.framecount==2 or self.framecount == 5:

                if Collicion.Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 0:
                    oponent.currentState.flags['Hit'] = True
                    oponent.currentAnim = 'Block'
                    oponent.framecount=0
                    oponent.currentAnimFrame=0
                    oponent.currentState.control=False

                    Tools.Logger.escribir("hubo colición de golpe bloqueado")
                elif Collicion.Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 1:
                    Tools.Logger.escribir("falló el golpe")
                elif Collicion.Golpe_Superior(pygame.sprite.collide_mask(self,oponent), self.pos[1], oponent.pos[1], oponent.currentState.block) == 2:
                    self.currentState.flags['Hit']=True
                    oponent.currentAnim='Hit'
                    oponent.currentAnimFrame=0
                    oponent.framecount=0
                    Tools.Logger.escribir("le achuntó")

        else:
            super(Medic, self).DoAction(oponent)





