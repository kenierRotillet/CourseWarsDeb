import pygame
from pygame.locals import *
import sys
import time
import random
import Sound
import Tools
screen_w = 1024
screen_h = 768

def main():
    pygame.mixer.init(frequency= 22050, size=-16, channels=2, buffer=64)

    
    
    pygame.init()
    pygame.mouse.set_visible(False)
    print "crash"
    estado_pj1 = 0
    estado_pj2 = 0
    ID_pj1 = False
    ID_pj2 = False
    contador = 0
    print "precrash?"
    screen = pygame.display.set_mode((screen_w,screen_h),FULLSCREEN)
    #screen = pygame.display.set_mode((screen_w,screen_h))
    v = 0
    print "todabia no crash"
    pygame.display.set_caption("Course_Wars")
    print "ya cago"
    Fondo={}
    Fondo[0]=("screens/start_menu/Fondo_Start1.jpg")
    Fondo[1]=("screens/start_menu/Fondo_Start2.jpg")     
    Salida = False
    Sound.soundPlayer.bgmPlay("bgm/Title.mp3")
    while Salida==False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_F5:
                    Sound.soundPlayer.playSysSound("Enter")
                    return "KeyConfig"


                    
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    t1 = Tools.FastMethods.detectKeys([event])
                    t2 = Tools.FastMethods.detectKeys([event],player=2)
                    if t1=='s':
                        estado_pj1 = 1
                        ID_pj1 = True
                    
                        Salida=True
                

                    if t2 == 's':
                        estado_pj2 = 1
                        ID_pj2 = True
                        
                        Salida=True







        contador +=1
        if contador == 10:
            v+=1
            if v == 2:
                v = 0
            contador = 0
                   
        fondo=pygame.image.load(Fondo[v]).convert()
        screen.blit((fondo),(0,0))
        pygame.display.flip()
        #print(v)
        #print(contador)
       
        #time.sleep(1)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()           
    if estado_pj1 == 1 or estado_pj2 == 1:
        #print "saliendo"

        #pygame.quit()
        Sound.soundPlayer.simpleplay("sfx/explode2.wav")

        return [ID_pj1,ID_pj2]

if __name__== "__main__":
    main()
             
