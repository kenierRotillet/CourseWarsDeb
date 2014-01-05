#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame
from pygame.locals import *
import Tools
import Core

screen_w = 1024
screen_h = 768


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((screen_w,screen_h))
    personaje = Core.Medic.Medic(1)
    pygame.display.set_caption("lalalal test")
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                personaje.lookCommand(Tools.FastMethods.convertKeys(pygame.key.get_pressed()),5)
                personaje.DoAction(personaje)
                if pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.quit()














