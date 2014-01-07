import pygame
from pygame import *
import Engineer
               
pygame.init()
fondo='Fondo.jpg' 
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Engineer_Test")
clock = pygame.time.Clock()
player = Engineer.Engineer_class(1)
game_over = False 
while game_over == False:
    clock.tick_busy_loop(40) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
    player.handle_event(event)
    background=pygame.image.load(fondo).convert()
    screen.blit(background,(0,0))
##    print(player.image)
    surf = pygame.image.load(player.image).convert_alpha()
    surf=pygame.transform.scale(surf,(700,700))
##    print(player.estado)
    screen.blit(surf,(player.x,player.y))
    print(clock.get_fps())
    pygame.display.flip()
    
    
pygame.quit ()
