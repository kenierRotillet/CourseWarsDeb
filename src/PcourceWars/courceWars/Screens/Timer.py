# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
import time
import Tools
#pygame.time.Clock
class Time(object):

    def __init__ (self,time):
        self.time=time
        self.reloj=pygame.time.Clock()
        self.t= self.reloj.tick(50)
        self.counter = 0
        self.listaImg=[]#lista que contiene a las imagenes cargadas
        self.listaNum=[]#lista que contiene a los numeros señalar con imagenes
        self.Clock=Tools.FastMethods.load_image("Screens/imgs/Reloj.png")
        for t in range(0,self.time+1):
            self.listaNum.append(str(t))
        for n in range(0,10):
            num=Tools.FastMethods.load_image("Screens/imgs/t"+str(n)+".png")
            self.listaImg.append(num)
            
    def update(self,pantalla):
        time=self.reloj.get_time()
        self.counter= self.counter+time
        pantalla.blit(self.Clock,(439,2))
        x=481
        y=55
        z=512
        
        if self.counter >= 1000 and not self.time == 0:
            if self.time>=10:
                a=self.listaNum[self.time][0]
                b=self.listaNum[self.time][1]
                pantalla.blit(self.listaImg[int(a)],(x,y))
                pantalla.blit(self.listaImg[int(b)],(z,y))
            else:
                a=self.listaNum[self.time]
                pantalla.blit(self.listaImg[0],(x,y))
                pantalla.blit(self.listaImg[int(a)],(z,y))
            self.time-=1
            self.counter=0
        else:
            if self.time >= 10:
                a=self.listaNum[self.time][0]
                b=self.listaNum[self.time][1]
                pantalla.blit(self.listaImg[int(a)],(x,y))
                pantalla.blit(self.listaImg[int(b)],(z,y))
            else:
                a=self.listaNum[self.time]
                pantalla.blit(self.listaImg[0],(x,y))
                pantalla.blit(self.listaImg[int(a)],(z,y))
                
            if self.time==0:
                pantalla.blit(self.listaImg[0],(x,y))
                pantalla.blit(self.listaImg[0],(z,y))

    def Tiempo(self):
        return self.time

        

    
