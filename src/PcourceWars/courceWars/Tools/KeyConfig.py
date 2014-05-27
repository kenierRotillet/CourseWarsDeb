#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Pequeño programa independiente que sirve para crear de manera rápida el archivo de configuración de teclas"""
import pygame
import os
from pygame.locals import *

p1 =[
    ("a", K_z),
    ("b",K_x),
    ("c",K_c),
    ("x",K_s),
    ("s",K_RETURN),
    ("U",K_t),
    ("B",K_f),
    ("F",K_h),
    ("D",K_g)]
p2 =[
    ("a", K_i),
    ("b",K_o),
    ("c",K_p),
    ("x",K_l),
    ("s",K_BACKSPACE),
    ("U",K_UP),
    ("B",K_LEFT),
    ("F",K_RIGHT),
    ("D",K_DOWN)]



def main():

    print "advertencia, este archivo borrará la configuración de teclas actual y la reemplasará por la inscrita en él! Si se desea concerbar, respaldar de antemano el archivo keys.ini"

    #en el siguiente lista, van tuplas en las cuales se asosia comando, tecla. Agregue / modifique las teclas a su gusto, son lista para el jugador 1, y el jugador 2.

    print "las configuraciones a guardar son:"
    print p1
    print p2
    print "presione enter para proseder"
    raw_input()

    print os.path.exists("../cfg/keis.ini")

    if os.path.exists("../cfg/keis.ini")==True:
        os.remove("../cfg/keis.ini")
        print "borrado original"

    arch = open("../cfg/keis.ini",'a')
    arch.write("p1:")
    for gak in p1:
        arch.write("\n" + gak[0] + "," + str(gak[1]))
    arch.write(";\np2:")
    for gak in p2:
        arch.write("\n"+gak[0] + "," + str(gak[1]))
    arch.write(";")

    arch.close()



    print "hecho!"
    raw_input()


def setManual(ip1,ip2):
    
    
    if os.path.exists("cfg/keis.ini")==True:
        os.remove("cfg/keis.ini")
        

    arch = open("cfg/keis.ini",'a')
    arch.write("p1:")
    for gak in ip1:
        arch.write("\n" + gak[0] + "," + str(gak[1]))
    arch.write(";\np2:")
    for gak in ip2:
        arch.write("\n"+gak[0] + "," + str(gak[1]))
    arch.write(";")

    arch.close()




if __name__=="__main__":
    main()
