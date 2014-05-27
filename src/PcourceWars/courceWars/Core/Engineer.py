#!/usr/bin/python
# -*- coding: latin-1 -*-
import Core.Personaje
import Tools
import pygame
import Collicion

class Engineer(Core.Personaje.Personaje):
    """ Clase que representa al personaje del ingeniero """

    def __init__(self, player,initPos):
        super(Engineer, self).__init__(player,initPos)
        """constructor del ingeniero, setea y carga sus archivos necesarios. Recibe el número de jugador que le corresponde, y su posición inicial."""
        self.anims = Core.Personaje.Tools.FastMethods.LoadAnimData("chars/Engineer/Engineer.anim")
        if self.flip==True:
            self.image=Tools.FastMethods.flipImage(self.anims['Stand'][0][1])
        else:
            self.image=self.anims['Stand'][0][1]
        Tools.Logger.escribir("imagen cargada: " + str(self.image))
        self.rect=self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.commands=Tools.FastMethods.load_commands("Chars/Engineer/Engineer.cmd")
        self.sounds = Tools.FastMethods.LoadSounds("Chars/Engineer/Engineer.snd")
        self.hitboxes=Tools.FastMethods.LoadHitboxesData("Chars/Engineer/Engineer.hbx")
        
        
        self.maxSpeed=6
        self.dashspeed=15
        self.rect.left=initPos[0]
        self.rect.top=initPos[1]
        
        
        self.pos=(self.rect.centerx,self.rect.centery)
        self.bodyRect.center = self.rect.center
        self.posinicial=self.rect.center


        Tools.Logger.escribir("inicializando al jugador " + str(self.player) + " como ingeniero. Datos específicos " + str(self) + ", posición y rect " + str(self.pos) + ", " + str(self.rect))

        
        


    def DoAction(self, oponent):
        if self.currentAnim=='Special':
            if self.power<self.maxpower:
                self.currentAnim=self.staticAnim
                return
            touch = Collicion.ejecutarHit(self,oponent)
            self.currentState.control=False
            if touch==True:
                oponent.currentState.control=False
                oponent.setDamage(5)


            if self.framecount==self.anims[self.currentAnim][-1][0]:
                self.power=0
                if self.currentState.flags.has_key('MaxPower'):

                    del self.currentState.flags['MaxPower']
                self.currentState.control=True
        else:
            super(Engineer, self).DoAction(oponent)
    

