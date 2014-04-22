import pygame
from pygame import *
import Medic
import Engineer

pygame.init()
fondo='Fondo.jpg' 
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Medic_Test")
clock = pygame.time.Clock()
player1 = Medic.Medic_class(2)
player2 = Engineer.Engineer_class(1)
game_over = False
background=pygame.image.load(fondo).convert()
while game_over == False:
    clock.tick_busy_loop(40) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
    player1.handle_event(event)
    player2.handle_event(event)
    screen.blit(background,(0,0))
##    print(player.image)
    surf1 = pygame.image.load(player1.image).convert_alpha()
    if player1.player==2:
        surf1=pygame.transform.flip(surf1,1,0)
    surf1=pygame.transform.scale(surf1,(700,700))
    surf2 = pygame.image.load(player2.image).convert_alpha()
    if player2.player==2:
        surf2=pygame.transform.flip(surf2,1,0)
    surf2=pygame.transform.scale(surf2,(700,700))
##    print(player.estado)
    screen.blit(surf1,(player1.x,player1.y))
    screen.blit(surf2,(player2.x,player2.y))
    
    #print(clock.get_fps())
    pygame.display.flip()
    
    
pygame.quit ()
