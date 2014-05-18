import pygame
from pygame.locals import *
import sys
from pygame import time
import random
import Sound

screen_w = 1024
screen_h = 768

def main():
    pygame.mixer.init()
    Sound.soundPlayer.bgmPlay("bgm/BGM_0007.mp3")
    

    pygame.init()
    pygame.mouse.set_visible(False)
    estado_pj1 = 0
    estado_pj2 = 0
    final_pj1 = 0
    final_pj2 = 0
    v = 1
    w = 1
    n = 35
    ID_pj1 = 1 
    ID_pj2 = 3
    screen = pygame.display.set_mode((screen_w,screen_h),FULLSCREEN)
    pygame.display.set_caption("Course_Wars")
    fondo=pygame.image.load("Screens/Sel_pj/Fondo_MenuStart.jpg").convert()
    screen.blit((fondo),(0,0))
    pygame.display.flip()

    Medic=pygame.image.load("Screens/Sel_pj/Sel_Medic.png").convert_alpha()
    Engineer=pygame.image.load("Screens/Sel_pj/Sel_Engineer.png").convert_alpha()
    Pysco=pygame.image.load("Screens/Sel_pj/Sel_Psyco.png").convert_alpha()
    Musician=pygame.image.load("Screens/Sel_pj/Sel_Musician.png").convert_alpha()
    IDK=pygame.image.load("Screens/Sel_pj/Sel_IDK.png").convert_alpha()

    sel_pj1=pygame.image.load("Screens/Sel_pj/Sel_pj1.png").convert_alpha()
    sel_pj2=pygame.image.load("Screens/Sel_pj/Sel_pj2.png").convert_alpha()

    sel_name1=pygame.image.load("Screens/Sel_pj/Sel_name1.png").convert_alpha()
    sel_name2=pygame.image.load("Screens/Sel_pj/Sel_name2.png").convert_alpha()

    vs = pygame.image.load("Screens/Sel_pj/VS.png").convert_alpha()
    
    Cuadro={}
    Cuadro[0]=("Screens/Sel_pj/Psyco_Sel.png")
    Cuadro[1]=("Screens/Sel_pj/Engineer_Sel.png")
    Cuadro[2]=("Screens/Sel_pj/IDK_Sel.png")
    Cuadro[3]=("Screens/Sel_pj/Medic_Sel.png")
    Cuadro[4]=("Screens/Sel_pj/Musician_Sel.png")

    pj1=pygame.image.load("Screens/Sel_pj/1p.png").convert_alpha()
    pj2=pygame.image.load("Screens/Sel_pj/2p.png").convert_alpha()
    
    Nombre={}
    Nombre[0]=(pygame.image.load("Screens/Sel_pj/Psyco.png").convert_alpha())
    Nombre[1]=(pygame.image.load("Screens/Sel_pj/Engineer.png").convert_alpha())
    Nombre[2]=(pygame.image.load("Screens/Sel_pj/IDK.png").convert_alpha())
    Nombre[3]=(pygame.image.load("Screens/Sel_pj/Medic.png").convert_alpha())
    Nombre[4]=(pygame.image.load("Screens/Sel_pj/Musician.png").convert_alpha())
    Salida=False
    while Salida==False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    estado_pj1 = 1
                    Sound.soundPlayer.simpleplay("sfx/Corredor.wav")

                elif event.key == K_LEFT:
                    estado_pj1 = 2          
                    Sound.soundPlayer.simpleplay("sfx/Corredor.wav")

                if event.key == K_d:
                    estado_pj2 = 1
                    Sound.soundPlayer.simpleplay("sfx/Corredor.wav")

                elif event.key == K_a:
                    estado_pj2 = 2
                    Sound.soundPlayer.simpleplay("sfx/Corredor.wav")

                if event.key == K_RETURN:
                    final_pj1 = 1
                    Sound.soundPlayer.simpleplay("sfx/select.wav")

                if event.key == K_BACKSPACE:
                    final_pj1 = 0
                    Sound.soundPlayer.simpleplay("sfx/backdash.wav")
                if event.key == K_SPACE:
                    final_pj2 = 1
                    Sound.soundPlayer.simpleplay("sfx/select.wav")

                if event.key == K_TAB:
                    final_pj2 = 0
                    Sound.soundPlayer.simpleplay("sfx/backdash.wav")

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == KEYUP:
                if estado_pj1 == 1 or 2:
                    estado_pj1 = 0
                    
                if estado_pj2 == 1 or 2:
                    estado_pj2 = 0
                
        if not final_pj1 == 1: 
            if estado_pj1 == 1:
                v += 1
                ID_pj1 += 1
                if v == 4:
                    v = 1
                if ID_pj1 == 4:
                    ID_pj1 = 1
                #if v == 5:
                 #   v = 0
                #if ID_pj1 == 5:
                 #   ID_pj1 = 0
            if estado_pj1 == 2:
                v -= 1
                ID_pj1 -= 1
                if v == 0:
                    v = 3
                if ID_pj1 == 0:
                    ID_pj1 = 3
            #if estado_pj1 == 2:
             #   v -= 1
              #  ID_pj1 -= 1
               # if v == -1:
                #    v = 4
                #if ID_pj1 == -1:
                 #   ID_pj1 = 4
                    
        if not final_pj2 == 1:
            if estado_pj2 == 1:
                w += 1
                ID_pj2 += 1
                if w == 4:
                    w = 1
                if ID_pj2 == 4:
                    ID_pj2 = 1
            #if estado_pj2 == 1:
             #   w += 1
              #  ID_pj2 += 1
               # if w == 5:
                #    w = 0
                #if ID_pj2 == 5:
                 #   ID_pj2 = 0
            if estado_pj2 == 2:
                w -= 1
                ID_pj2 -= 1
                if w == 0:
                    w = 3
                if ID_pj2 == 0:
                    ID_pj2 = 3
            #if estado_pj2 == 2:
             #   w -= 1
              #  ID_pj2 -= 1
               # if w == -1:
                #    w = 4
                #if ID_pj2 == -1:
                 #   ID_pj2 = 4       

        if final_pj1 == 1  and final_pj2 == 1:
            Salida=True                
        
        screen.blit((fondo),(0,0))
        screen.blit((vs),(436,300))
        
        cuadro1 = pygame.image.load(Cuadro[v]).convert_alpha()
        #print (str(Cuadro[w]))
        cuadro2 = pygame.image.load(Cuadro[w]).convert_alpha()
        screen.blit(cuadro1,(142,100))
        screen.blit(sel_name1,(120,370))
        screen.blit(Nombre[v],(120,350))
        screen.blit(cuadro2,(682,100))
        screen.blit(sel_name2,(648,370))
        screen.blit(Nombre[w],(650,350))
        screen.blit(pj1,(112,415))
        screen.blit(pj2,(882,415))
        
        screen.blit(Pysco,(142,550))
        screen.blit(Engineer,(302,550))
        screen.blit(IDK,(462,550))
        screen.blit(Medic,(622,550))
        screen.blit(Musician,(782,550))

        x=142
        y=142
        x = x + v*160
        screen.blit(sel_pj1,(x,550))
        y = y + w*160
        screen.blit(sel_pj2,(y,550))
      
        
        pygame.display.flip()
        pygame.time.wait(50)
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()            
    if ID_pj1 == 2:                                        
        while  ID_pj1 == 2:                         
            #ID_pj1 = random.randint(0,4)
            ID_pj1 = random.randint(1,3)
    if ID_pj2 == 2:                           
        while ID_pj2 == 2:
            #ID_pj2 = random.randint(0,4)
            ID_pj2 = random.randint(1,3)

    return (ID_pj1,ID_pj2)
        # 0->Pysco
        # 1->Engineer
        # 2->IDK
        # 3->Medic
        # 4->Musician

if __name__== "__main__":
    main()

             
