import pygame
from pygame.locals import *
import sys
from pygame import time as pytime #no lo ocupe pero igual no esta de mas
screen_w = 1024
screen_h = 768

def main():
    estado_pj1 = 0
    estado_pj2 = 4
    ID_pj1 = 0 #ID pj va de 1-4, representa al personaje para despues cargarlo
    ID_pj2 = 0
    screen = pygame.display.set_mode((screen_w,screen_h))
    pygame.display.set_caption("Seleccion de Personaje") #nombre de la ventana
    fondo = pygame.image.load("Fondo.jpg").convert()# permite cargar imagenes
    screen.blit(fondo,(0,0))
    pygame.display.flip()
    
    Imagen = {}#bibliotecas con las imagenes
    Imagen[0]=("Sel_pj.jpg")
    Imagen[1]=("Sel_pj1.jpg")
    Imagen[2]=("Sel_pj2.jpg")
    Imagen[3]=("Sel_pj1pj2.jpg")
    
    Cuadro = {}
    Cuadro[0]=("Fondo_pj0.jpg")
    Cuadro[1]=("Fondo_pj1.jpg")
    Cuadro[2]=("Fondo_pj2.jpg")
    Cuadro[3]=("Fondo_pj3.jpg")
    Cuadro[4]=("Fondo_pj4.jpg")

    while True: # hay q solucionar el problema de cuando me mantiene presionada una de las teclas y se empieza la presionar la otra sucesivamente, estas se mueven juntas
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_RIGHT]:
                    estado_pj1 +=1
                    if estado_pj1 == 5:
                        estado_pj1 = 0
                elif pygame.key.get_pressed()[K_LEFT]:
                    estado_pj1 -=1
                    if estado_pj1 == -1:
                        estado_pj1 = 4                        
                if pygame.key.get_pressed()[K_d]:
                    estado_pj2 +=1
                    if estado_pj2 == 5:
                        estado_pj2 = 0
                elif pygame.key.get_pressed()[K_a]:
                    estado_pj2 -=1
                    if estado_pj2 == -1:
                        estado_pj2 = 4
                if pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
        a=0
        b=0
        c=0
        d=0
        e=0
        x=(0,1,2,3,4)
        if estado_pj1==0:
            a=1          
        if estado_pj1==1:
            b=1            
        if estado_pj1==2:
            c=1           
        if estado_pj1==3:
            d=1          
        if estado_pj1==4:
            e=1        
        if estado_pj2==0:
            a=2
        if estado_pj2==1:
            b=2          
        if estado_pj2==2:
            c=2          
        if estado_pj2==3:
            d=2         
        if estado_pj2==4:
            e=2
        if estado_pj1==estado_pj2:
            X=x[estado_pj1]
            if X==0:
                a=3
            if X==1:
                b=3
            if X==2:
                c=3
            if X==3:
                d=3
            if X==4:
                e=3            
        
        Bloque = {}
        Bloque[0]=pygame.image.load(Imagen[a]).convert()
        Bloque[1]=pygame.image.load(Imagen[b]).convert()
        Bloque[2]=pygame.image.load(Imagen[c]).convert()
        Bloque[3]=pygame.image.load(Imagen[d]).convert()
        Bloque[4]=pygame.image.load(Imagen[e]).convert()
       
        cuadro1 = pygame.image.load(Cuadro[estado_pj1]).convert()
        cuadro2 = pygame.image.load(Cuadro[estado_pj2]).convert()
        screen.blit(cuadro1,(50,40))
        screen.blit(cuadro2,(718,40))
        screen.blit(Bloque[0],(30,510))
        screen.blit(Bloque[1],(234,580))
        screen.blit(Bloque[2],(435,620))
        screen.blit(Bloque[3],(640,580))
        screen.blit(Bloque[4],(845,510))       
        pygame.display.flip()

    if event.typt == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
if __name__== "__main__":
    main()
               
