import pygame
from pygame.locals import *
import sys
from pygame import time
import random
import time
screen_w = 1024
screen_h = 768

def main():
    pygame.init()
    estado_pj1 = 0
    estado_pj2 = 0
    final_pj1 = 0 #este genera la condicion para que no siga moviendo las animacion y detemina finalmente quien es el personaje a ocupar
    final_pj2 = 0
    v = 0
    w = 4
    n = 35
    time = 75  #milisegundos (en estapa de prueba para decir el mejor tiempo de espera)
    ID_pj1 = 0 #ID pj va de 1-4, representa al personaje para despues cargarlo, esto cuenta el caso random
    ID_pj2 = 4
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

    Tiempo = {}
    Tiempo[0] = pygame.image.load("t0.png").convert()
    Tiempo[1] = pygame.image.load("t1.png").convert()
    Tiempo[2] = pygame.image.load("t2.png").convert()
    Tiempo[3] = pygame.image.load("t3.png").convert()
    Tiempo[4] = pygame.image.load("t4.png").convert()
    Tiempo[5] = pygame.image.load("t5.png").convert()
    Tiempo[6] = pygame.image.load("t6.png").convert()
    Tiempo[7] = pygame.image.load("t7.png").convert()
    Tiempo[8] = pygame.image.load("t8.png").convert()
    Tiempo[9] = pygame.image.load("t9.png").convert()

    Reloj = pygame.image.load("Reloj.png").convert()
    Fondo_reloj = pygame.image.load("Fondo_reloj.jpg").convert()
    reloj = int(time.time())
    while True:         
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_RIGHT]:
                    estado_pj1 = 1
                elif pygame.key.get_pressed()[K_LEFT]:
                    estado_pj1 = 2           
                if pygame.key.get_pressed()[K_d]:
                    estado_pj2 = 1
                elif pygame.key.get_pressed()[K_a]:
                    estado_pj2 = 2
                if pygame.key.get_pressed()[K_RETURN]:
                    final_pj1 = 1
                if pygame.key.get_pressed()[K_BACKSPACE]:
                    final_pj1 = 0
                if pygame.key.get_pressed()[K_SPACE]:
                    final_pj2 = 1
                if pygame.key.get_pressed()[K_TAB]:
                    final_pj2 = 0
                if pygame.key.get_pressed()[K_ESCAPE]:
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
                if v == 5:
                    v = 0
                if ID_pj1 == 5:
                    ID_pj1 = 0
            if estado_pj1 == 2:
                v -= 1
                ID_pj1 -= 1
                if v == -1:
                    v = 4
                if ID_pj1 == -1:
                    ID_pj1 = 4
                    
        if not final_pj2 == 1:
            if estado_pj2 == 1:
                w += 1
                ID_pj2 += 1
                if w == 5:
                    w = 0
                if ID_pj2 == 5:
                    ID_pj2 = 0
            if estado_pj2 == 2:
                w -= 1
                ID_pj2 -= 1
                if w == -1:
                    w = 4
                if ID_pj2 == -1:
                    ID_pj2 = 4            
        a=0
        b=0
        c=0
        d=0
        e=0
        x=(0,1,2,3,4)  #casos que corresponden para poder actualizar las imagenes de los cuadros de los personajes ha seleccionar + una lista auxiliar :)
        if ID_pj1==0:
            a=1          
        if ID_pj1==1:
            b=1            
        if ID_pj1==2:
            c=1           
        if ID_pj1==3:
            d=1          
        if ID_pj1==4:
            e=1        
        if ID_pj2==0:
            a=2
        if ID_pj2==1:
            b=2          
        if ID_pj2==2:
            c=2          
        if ID_pj2==3:
            d=2         
        if ID_pj2==4:
            e=2
        if ID_pj1==ID_pj2:
            X=x[ID_pj1]
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
       
        Bloque = {} #las imagenes de los cuadros de personajes se tienen que resetear cada vez que se cambia la posicion para que se pueda actualizar la imagen a mostrar
        Bloque[0]=pygame.image.load(Imagen[a]).convert()
        Bloque[1]=pygame.image.load(Imagen[b]).convert()
        Bloque[2]=pygame.image.load(Imagen[c]).convert()
        Bloque[3]=pygame.image.load(Imagen[d]).convert()
        Bloque[4]=pygame.image.load(Imagen[e]).convert()
        
        cuadro1 = pygame.image.load(Cuadro[v]).convert()
        cuadro2 = pygame.image.load(Cuadro[w]).convert()
        screen.blit(cuadro1,(50,40))
        screen.blit(cuadro2,(718,40))
            
        screen.blit(Bloque[0],(30,510))
        screen.blit(Bloque[1],(234,580))
        screen.blit(Bloque[2],(435,620))
        screen.blit(Bloque[3],(640,580))
        screen.blit(Bloque[4],(845,510))       
        pygame.display.flip()
        pygame.time.wait(time)
        

        if final_pj1 == 1  and final_pj2 == 1:                ##Observacion## (Estas corresponden a los numeros asigados a ellos para que el nucleo, sepa cual cargar)
            if ID_pj1 == 2:                                     #1-Musician    
                while not ID_pj1 == 2:                          #2-Medic
                    ID_pj1 = random.randint(0,4)                #3-Enginner
            if ID_pj2 == 2:                                     #4-Psyco
                while not ID_pj2 == 2:
                    ID_pj2 = random.randint(0,4)
            if ID_pj1 == 0:
                ID_pj1 = 1
            if ID_pj1 == 1:
                ID_pj1 = 2
            if ID_pj2 == 0:
                ID_pj2 = 1
            if ID_pj2 == 1:
                ID_pj2 = 2

            return ID_pj1,ID_pj2
                    

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
if __name__== "__main__":
    main()
               
