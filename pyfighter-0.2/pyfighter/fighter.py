#! /usr/bin/env python

# PyFighter
# StreetFighter-like game

#
#   Copyright (C) 2009  Francis Stokes
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.




#Import
import os, sys, pygame, random
from pygame.locals import *

#-------------------------------------------------- ////// SET UP ENVIRONMENT //////// ----------------------------------

os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
pygame.display.set_caption("PyFighter v0.2")

screen = pygame.display.set_mode((800, 600))
pygame.mouse.set_visible(1)

#Background Set Up
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

#Better image loading
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


# ------------- CLASSES --------------- #

class Arena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("arena.png", -1)
        self.dy = 600
        self.reset()
        
    def update(self):
        self.rect.bottom = self.dy
        if self.rect.bottom >= 1200:
            self.reset() 
    
    def reset(self):
        self.rect.top = -600


class Scores(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.p1health = 300
	self.p2health = 300
        self.font = pygame.font.Font("data/fonts/arial.ttf", 28)
        
    def update(self):
        self.text = "Player 1: %d HP    Player 2: %d HP" % (self.p1health, self.p2health)
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,170)


class title_version(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 24)

    def update(self):
        self.text = "-- PyFighter -- v0.1.5 --"
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,450)

class MainMenu1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 28)

    def update(self):
        self.text = "-- PyFighter -- Version 0.2 --"
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,200)

class MainMenu2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 20)

    def update(self):
        self.text = "[N]ew Game"
        self.image = self.font.render(self.text, 1, (144, 30, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,250)


class MainMenu3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 20)

    def update(self):
        self.text = "e[X]it"
        self.image = self.font.render(self.text, 1, (144, 30, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,280)


class p1_wins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 28)

    def update(self):
        self.text = "-- Player 1 wins --"
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)

class p2_wins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/flipside.ttf", 28)

    def update(self):
        self.text = "-- Player 2 wins --"
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)

#Player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("sprites/girl1/1.png", -1)
		self.dx = 0       # X Movement
		self.dy = 0       # Y movement
		self.jmp = 0     # Jump flag
		self.w = 0         # Walk Flag
		self.a_m = 0    # Attack (melee) flag
		self.a_r   = 0    # Attack (range) flag
		self.a_dam = 0 # Attack Damage
		self.a_type = 0 # Attack Type (used for attack overrides)
		self.d = 0         # Defense flag
		self.d_type = 0        # Defense Type
		self.rect.center = (160, 320)
	
	def update(self):
		self.rect.move_ip((self.dx, self.dy))
		self.dx = 0
		self.dy = 0

#Enemy (player 2)
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("sprites/ken/1.png", -1)
		self.dx = 0       # X Movement
		self.dy = 0       # Y movement
		self.jmp = 0     # Jump flag
		self.w = 0         # Walk Flag
		self.a_m = 0    # Attack (melee) flag
		self.a_r   = 0    # Attack (range) flag
		self.a_dam = 0 # Attack Damage
		self.a_type = 0 # Attack Type (used for attack overrides)
		self.d = 0         # Defense flag
		self.d_type = 0 # Defense Type
		self.rect.center = (300, 320)
	
	def update(self):
		self.rect.move_ip((self.dx, self.dy))
		self.dx = 0
		self.dy = 0

class db_console(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/arial.ttf", 12)
        
    def update(self):
        self.text = "Mouse (x: %d  y: %d)" % (self.xpos, self.ypos)
        self.image = self.font.render(self.text, 1, (30, 144, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (200,90)

#---------------------------------------- ////// END SET UP ENVIRONMENT //////// ----------------------------------


#Set Clock
clock = pygame.time.Clock()
keepGoing = True
counter = 0

arena = Arena()
arena = pygame.sprite.RenderPlain((arena))


scores = Scores()
scoreSprite = pygame.sprite.Group(scores)


player = Player()
playerSprite = pygame.sprite.RenderPlain((player))

enemy = Enemy()
enemySprite = pygame.sprite.RenderPlain((enemy))

dbc = db_console()
dbcS = pygame.sprite.Group(dbc)

screennum = 0

menu = MainMenu1()
menu = pygame.sprite.Group(menu)

menu1 = MainMenu2()
menu1 = pygame.sprite.Group(menu1)

menu2 = MainMenu3()
menu2 = pygame.sprite.Group(menu2)

tv = title_version()
tv = pygame.sprite.Group(tv)

ai = -1

p1w = p1_wins()
p1w = pygame.sprite.Group(p1w)

p2w = p2_wins()
p2w = pygame.sprite.Group(p2w)

setbreak1 = 0
setbreak2 = 0

def draw_fs():
	 #Events
        events = pygame.event.get()
	#==================== Player Events ========================
        for e in events:
		if (e.type == pygame.QUIT):
			pygame.quit()
		else:
			if (e.type == KEYDOWN):
				if (e.key == K_RIGHT and player.w == 0):
					a = 0
					for hit in pygame.sprite.groupcollide(playerSprite, enemySprite, 0, 0):
						a = a + 1
					if (a == 0):
						player.w = 1
						player.dx = 15
						a = player.rect.center
						player.image, player.rect = load_image("sprites/girl1/2.png", -1)
						player.rect.center = a
						player.update()
				else:
					if (e.key == K_RIGHT and player.w == 1):
						player.w = 0
						player.dx = 15
						a = player.rect.center
						player.image, player.rect = load_image("sprites/girl1/1.png", -1)
						player.rect.center = a
						player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_LEFT and player.w == 0):
					player.w = 1
					player.dx = -15
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/2.png", -1)
					player.rect.center = a
					player.update()
				else:
					if (e.key == K_LEFT and player.w == 1):
						player.w = 0
						player.dx = -15
						a = player.rect.center
						player.image, player.rect = load_image("sprites/girl1/1.png", -1)
						player.rect.center = a
						player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_UP and player.jmp <= 0 and player.a_m == 0 and player.a_r == 0 and player.d_type == 0):
					player.dy = -60
					player.jmp = 5
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/3.png", -1)
					player.rect.center = a
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_a and player.jmp == 0 and player.a_m == 0 and player.a_r == 0):
					player.a_m = 2
					player.a_dam = 12
					player.a_type = 0
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/5.png", -1)
					player.rect.center = a
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_s and player.jmp == 0 and player.a_m == 0 and player.a_r == 0):
					player.a_m = 4
					player.dam = 16
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/6.png", -1)
					player.rect.center = a
					player.a_type = 0
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_d and player.jmp == 0 and player.d == 0 and player.d_type == 0):
					player.d = 6
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/4.png", -1)
					player.rect.center = a
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_w and player.a_m == 0 and player.a_r == 0 and player.d_type == 0):
					player.a_m = 6
					player.dam = 14
					player.dx = 20
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/7.png", -1)
					player.rect.center = a
					player.a_type = 0
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_q and player.a_m == 0 and player.a_r == 0 and player.d_type == 0):
					player.a_m = 5
					player.dam = 10
					player.a_type = 1
					player.dy = 20
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/8.png", -1)
					player.rect.center = a
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_c and player.d == 0 and player.d_type == 0 and player.a_m == 0):
					player.d = 6
					player.d_type = 1
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/9.png", -1)
					player.rect.center = a
					player.dy = 20
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_x and player.jmp == 0 and player.a_m == 0 and player.a_r == 0):
					player.a_m = 5
					player.dam = 6
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/10.png", -1)
					player.rect.center = a
					# draw next animation sprite
					player.update()
			if (e.type == KEYDOWN):
				if (e.key == K_0):
					pygame.quit()
			
		# =========================================================
		
	# ===================== ENEMY EVENTS =======================
		
		
	if (enemy.a_m == 0 and enemy.d == 0):
		ai = random.randrange(0, 12)
		if (ai == 0 and enemy.d == 0):
			enemy.d = 5
			enemy.dt = 1
			a = enemy.rect.center
			enemy.image, enemy.rect = load_image("sprites/ken/3.png", -1)
			enemy.rect.center = a
			# draw next animation sprite
			enemy.update()
		else:
			if (ai == 1 and enemy.a_m == 0):
				enemy.a_m = 3
				enemy.a_type = 1
				enemy.a_dam = 2 + random.randrange(1, 14)
				a = enemy.rect.center
				enemy.image, enemy.rect = load_image("sprites/ken/4.png", -1)
				enemy.rect.center = a
				# draw next animation sprite
				enemy.update()
			else:
				if (ai == 2 and enemy.a_m == 0):
					enemy.a_m = 6
					enemy.a_type = 1
					enemy.a_dam = 5 + random.randrange(1, 7)
					a = enemy.rect.center
					enemy.image, enemy.rect = load_image("sprites/ken/5.png", -1)
					enemy.rect.center = a
					# draw next animation sprite
					enemy.update()
				else:
					if (ai == 3 or ai == 5 or ai == 7):
						a = 0
						for hit in pygame.sprite.groupcollide(playerSprite, enemySprite, 0, 0):
							a = a + 1
						if (a == 0):
							enemy.dx = -15
							enemy.update()
					else:
						if (ai == 4 or ai == 6 or ai == 8):
							a = 0
							for hit in pygame.sprite.groupcollide(playerSprite, enemySprite, 0, 0):
								a = a + 1
							if (a == 0):
								enemy.dx = 15
								enemy.update()
							
	# =================== END ENEMY EVENTS ======================
	
	# --------------------> CHECK JUMPS <----------------------
	if (player.jmp > 0):
		if (player.jmp == 1):
			a = player.rect.center
			player.image, player.rect = load_image("sprites/girl1/1.png", -1)
			player.rect.center = a
			player.update()
			player.jmp = 0
		else:
			player.dy = 15
			player.jmp = player.jmp - 1
			player.update()

	# --------------------> CHECK ATTACKS <----------------------
	if (player.a_m > 0):
		if (player.a_m >= 2):
			player.a_m = player.a_m -1
		else:
			if (player.a_m == 1 and player.a_type == 0):
				a = player.rect.center
				player.image, player.rect = load_image("sprites/girl1/1.png", -1)
				player.rect.center = a
				player.a_m = 0
			else:
				if (player.a_m == 1 and player.a_type == 1):
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/1.png", -1)
					player.dy = -20
					player.rect.center = a
					player.a_m = 0
					player.at = 0
	if (enemy.a_m > 0):
		if (enemy.a_m >= 2):
			enemy.a_m = enemy.a_m -1
		else:
			if (enemy.a_m == 1 and enemy.a_type == 0):
				a = enemy.rect.center
				enemy.image, enemy.rect = load_image("sprites/ken/1.png", -1)
				enemy.rect.center = a
				enemy.a_m = 0
			else:
				if (enemy.a_m == 1 and enemy.a_type == 1):
					a = enemy.rect.center
					enemy.image, enemy.rect = load_image("sprites/ken/1.png", -1)
					enemy.rect.center = a
					enemy.dam = 10
					enemy.a_m = 0
					enemy.at = 0
	# --------------------> CHECK DEFENSE <----------------------
	if (player.d > 0):
		if (player.d >= 2):
			player.d = player.d -1
		else:
			if (player.d == 1 and player.d_type == 0):
				a = player.rect.center
				player.image, player.rect = load_image("sprites/girl1/1.png", -1)
				player.rect.center = a
				player.d = 0
				player.d_type = 0
			else:
				if (player.d == 1 and player.d_type == 1):
					player.d_type = 0
					player.dy = -20
					a = player.rect.center
					player.image, player.rect = load_image("sprites/girl1/1.png", -1)
					player.rect.center = a
					player.d = 0
	if (enemy.d > 0):
		if (enemy.d >= 2):
			enemy.d = enemy.d -1
		else:
			if (enemy.d == 1 and enemy.d_type == 0):
				a = enemy.rect.center
				enemy.image, enemy.rect = load_image("sprites/ken/1.png", -1)
				enemy.rect.center = a
				enemy.d = 0
			else:
				if (enemy.d >= 1 and enemy.d_type == 1):
					enemy.dt = 0
					a = enemy.rect.center
					enemy.image, enemy.rect = load_image("sprites/ken/1.png", -1)
					enemy.rect.center = a
					enemy.d = 0
	
	# ===================================================================
	# ================== COLLISION / DAMAGE DETECTION =======================
	# ===================================================================
	
	for hit in pygame.sprite.groupcollide(playerSprite, enemySprite, 0, 0):
		if (player.a_m == 0 and player.a_r == 0 and enemy.a_m == 0 and enemy.a_r == 0):
			#no attack on either side
			print("Type 1 collision (no attacks)")
		else:
			if (player.a_m == 1 and player.a_r == 0 and enemy.a_m == 0 and enemy.a_r == 0):
				#player has attacked, enemy has not
				if (enemy.d == 0):
					#no enemy defense
					print("Type 2 collision (player 1 attacked)")
					if (scores.p2health - player.a_dam <= 0):
						scores.p1health = 300
						scores.p2health = 300
						print("Player 1 Wins")
						return 0
					else:
						scores.p2health = scores.p2health - player.a_dam
				else:
					#enemy defense
					print("Type 3 collision (player 1 attacked, player 2 defense)")
			else:
				if (player.a_m == 0 and player.a_r == 0 and enemy.a_m == 1 and enemy.a_r == 0):
					#enemy has attacked, player has not
					if (player.d == 0):
						#no player defense
						print("Type 4 collision (player 2 attacked)")
						if (scores.p1health - enemy.a_dam <= 0):
							scores.p1health = 300
							scores.p2health = 300
							print("Player 2 Wins")
							return 0
						else:
							scores.p1health = scores.p1health - enemy.a_dam
					else:
						#player defense
						print("Type 5 collision (player 2 attacked, player 1 defense)")
	
        #Update
        screen.blit(background, (0,0))
        arena.update()
	tv.update()
	scoreSprite.update()
	
	#dbc.xpos, dbc.ypos = pygame.mouse.get_pos()
	#dbcS.update()
	
	#Draw
        arena.draw(screen)
	scoreSprite.draw(screen)
	#dbcS.draw(screen)
	
	enemySprite.update()
	enemySprite.draw(screen)
	
	playerSprite.update()
	playerSprite.draw(screen)
	tv.draw(screen)
        pygame.display.flip()

def draw_main_menu():
	while (1):
		#Events
		events = pygame.event.get()
		#Quit Event
		for e in events:
			if (e.type == pygame.QUIT):
				pygame.quit()
			else:
				if (e.type == KEYDOWN):
					if (e.key == K_n ):
						while (1):
							clock.tick(12)
							if (draw_fs() == 0):
								return 0
				if (e.type == KEYDOWN):
					if (e.key == K_x ):
						pygame.quit()
						
		#Update
		screen.blit(background, (0,0))
	
		menu.update()
		menu1.update()
		menu2.update()
		menu2.draw(screen)
		menu1.draw(screen)
		menu.draw(screen)
	
		pygame.display.flip()
	

while 1:
	clock.tick(12)
	winner = draw_main_menu()
	if (winner == 1):
		p1w.update()
		p1w.draw()
		pygame.display.flip()



if __name__ == "__main__":
   main()
