import pygame
Medic={}
sprite=[]
for i in range(1,5):
    a = "C:sprites/Medic000_00"+str(i)+".png"
    sprite.append(a)
Medic[0]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Medic001_00"+str(i)+".png"
    sprite.append(a)
Medic[1]=sprite
sprite=[]
for i in range(1,6):
    a = "C:sprites/Medic002_00"+str(i)+".png"
    sprite.append(a)
Medic[2]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Medic003_00"+str(i)+".png"
    sprite.append(a)
Medic[3]=sprite
sprite=[]
for i in range(1,8):
    a = "C:sprites/Medic004_00"+str(i)+".png"
    sprite.append(a)
Medic[4]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic005_00"+str(i)+".png"
    sprite.append(a)
Medic[5]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Medic006_00"+str(i)+".png"
    sprite.append(a)
Medic[6]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Medic007_00"+str(i)+".png"
    sprite.append(a)
Medic[7]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Medic008_00"+str(i)+".png"
    sprite.append(a)
Medic[8]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic009_00"+str(i)+".png"
    sprite.append(a)
Medic[9]=sprite
sprite=[]
for i in range(1,5):
    a = "C:sprites/Medic010_00"+str(i)+".png"
    sprite.append(a)
Medic[10]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic011_00"+str(i)+".png"
    sprite.append(a)
Medic[11]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic012_00"+str(i)+".png"
    sprite.append(a)
Medic[12]=sprite
sprite=["C:sprites/Medic013_001.png"]
Medic[13]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic014_00"+str(i)+".png"
    sprite.append(a)
Medic[14]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Medic015_00"+str(i)+".png"
    sprite.append(a)
Medic[15]=sprite
sprite=["C:sprites/Medic016_001.png"]
Medic[16]=sprite
sprite=["C:sprites/Medic017_001.png"]
Medic[17]=sprite
sprite=["C:sprites/Medic018_001.png"]
Medic[18]=sprite
sprite=[]
for i in range(1,6):
    a = "C:sprites/Medic019_00"+str(i)+".png"
    sprite.append(a)
Medic[19]=sprite
sprite=["C:sprites/Medic020_001.png"]
Medic[20]=sprite
sprite=["C:sprites/Medic021_001.png"]
Medic[21]=sprite
sprite=["C:sprites/Medic022_001.png"]
Medic[22]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Medic023_00"+str(i)+".png"
    sprite.append(a)
Medic[23]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Medic024_00"+str(i)+".png"
    sprite.append(a)
Medic[24]=sprite
sprite=[]
for i in range(1,8):
    a = "C:sprites/Medic025_00"+str(i)+".png"
    sprite.append(a)
Medic[25]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Medic026_00"+str(i)+".png"
    sprite.append(a)
Medic[26]=sprite
class Medic_class(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)        
        self.player=player
        self.max_speed=10        
        self.jump_speed=20
        self.jumping=False        
        self.estado=0
        self.x=0
        self.y=100
        if self.player==2:
            self.x=300
        self.stand=Medic[0]
        self.lightpunch=Medic[1]
        self.mediumpunch=Medic[2]
        self.highpunch=Medic[3]
        self.jump=Medic[4]
        self.j_lightpunch=Medic[5]
        self.j_mediumpunch=Medic[6]
        self.j_highpunch=Medic[7]
        self.down=Medic[8]
        self.d_lightpunch=Medic[9]
        self.d_mediumpunch=Medic[10]
        self.guard=Medic[11]
        self.d_guard=Medic[12]
        self.j_guard=Medic[13]
        self.dashfront=Medic[14]
        self.dashback=Medic[15]
        self.defense=Medic[16]
        self.d_defense=Medic[17]
        self.j_defense=Medic[18]
        self.walk=Medic[19]
        self.hit=Medic[20]
        self.d_hit=Medic[21]
        self.j_hit=Medic[22]
        self.recover=Medic[23]
        self.taunt=Medic[24]
        self.especial=Medic[25]
        self.effect=Medic[26]
        self.image=""
        self.clip(self.stand,self.estado)
    def update_posicion(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
        
    def clip(self,lista,estado):
        sprite = lista
        a = len(sprite)
        if estado >= a:
            self.estado = 0            
        self.image = sprite[self.estado]
    
    def update(self, direction):
        if direction == 'caminar':
            self.clip(self.walk,self.estado)
            self.estado+=1
  
        if direction == 'stand':
            self.clip(self.stand,self.estado)
            self.estado+=1
            
        if direction == 'LP':
            self.clip(self.lightpunch,self.estado)
            self.estado+=1

        if direction=='MP':
            self.clip(self.mediumpunch,self.estado)
            self.estado+=1

        if direction=='HP':
            self.clip(self.highpunch,self.estado)
            self.estado+=1
    
    def handle_event(self, event):
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        while pygame.event.get(): pass
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            game_over = True        
        if event.type == pygame.KEYDOWN and self.player == 1:           
                
            if key[pygame.K_f]:
                self.update('LP')
            if key[pygame.K_g]:
                self.update('MP')
            if key[pygame.K_h]:
                self.update('HP')
            if key[pygame.K_LEFT]:
                self.update('caminar')
                self.update_posicion(-10,0)
                self.defensa=True
            if key[pygame.K_RIGHT]:
                self.update('caminar')
                self.update_posicion(10,0)
                
        if event.type == pygame.KEYDOWN and self.player == 2:           

            if key[pygame.K_u]:
                self.update('LP')
            if key[pygame.K_i]:
                self.update('MP')
            if key[pygame.K_o]:
                self.update('HP')
            if key[pygame.K_a]:
                self.update('caminar')
                self.update_posicion(-10,0)
            if key[pygame.K_d]:
                self.update('caminar')
                self.update_posicion(10,0)
                self.defensa=True
 
        if event.type == pygame.KEYUP:   
            #if event.key == pygame.K_a or event.key==pygame.K_d:
            self.update('stand')            
            #if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
             #   self.update('stand')

 

        

    
