#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame

class Engineer(Core.Personaje.Personaje):
    """ Clase que representa al personaje del ingeniero """

    def __init__(self, player,initPos):
        super(Engineer, self).__init__(player,initPos)
        """constructor del ingeniero, setea y carga sus archivos necesarios. Recibe el número de jugador que le corresponde, y su posición inicial."""
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Engineer/Engineer.anim")
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1],None,True,self.flip)
        self.mask = pygame.mask.from_surface(self.image)
        self.commands=Tools.FastMethods.load_commands("Chars/Engineer/Engineer.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Engineer/Engineer.snd")
        self.hitboxes=Tools.FastMethods.LoadHitboxesData("Chars/Engineer/Engineer.hbx")
        
        
        self.maxSpeed=4
        self.dashspeed=6
        self.rect.left=initPos[0]
        self.rect.top=initPos[1]
        
        
        self.pos=(self.rect.centerx,self.rect.centery)
        self.bodyRect.center = self.rect.center


        Tools.Logger.escribir("inicializando al jugador " + str(self.player) + " como ingeniero. Datos específicos " + str(self) + ", posición y rect " + str(self.pos) + ", " + str(self.rect))

        
        


