import pygame
import Medic
               
pygame.init()
fondo='Fondo.jpg' 
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Medic_Test")
clock = pygame.time.Clock()
player = Medic.Medic((0, 135))
game_over == False 
while game_over == False:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
    player.handle_event(event)
    background=pygame.image.load(fondo).convert()
    screen.blit(background,(0,0)) 
    screen.blit(pygame.image.load(player.image).convert_alpha(),(player.x,player.y))
    pygame.display.flip()              
    clock.tick(40) 
pygame.quit ()
