#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame

class Engineer(Core.Personaje.Personaje):
    """ Clase que representa al personaje del ingeniero """

    def __init__(self, player,initPos):
        super(Engineer, self).__init__(player)
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Engineer/Engineer.anim")
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])
        self.commands=Tools.FastMethods.load_commands("Chars/Engineer/Engineer.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Engineer/Engineer.snd")
        self.pos=initPos
        self.rect.center = (self.pos)
        
        


