#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools

class Medic(Core.Personaje.Personaje):
    """ Clase que reprecenta al personaje del médico """

    def __init__(self, player):
        Core.Personaje.Personaje.__init__(self,player)
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Medic/Medic.anim")
        self.image, self.rect=Tools.FastMethods.load_image(self.anims[self.currentAnim][self.currentAnimFrame][1])
        self.commands=Tools.FastMethods.load_commands("Chars/Medic/Medic.cmd")
        self.rect.x = 0
        self.rect.y = 300






