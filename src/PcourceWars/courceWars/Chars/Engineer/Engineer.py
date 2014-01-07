import pygame
Engineer={}
sprite=[]
for i in range(1,5):
    a = "C:sprites/Enginer000_00"+str(i)+".png"
    sprite.append(a)
Engineer[0]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer001_00"+str(i)+".png"
    sprite.append(a)
Engineer[1]=sprite
sprite=[]
for i in range(1,6):
    a = "C:sprites/Enginer002_00"+str(i)+".png"
    sprite.append(a)
Engineer[2]=sprite
sprite=[]
for i in range(1,6):
    a = "C:sprites/Enginer003_00"+str(i)+".png"
    sprite.append(a)
Engineer[3]=sprite
sprite=[]
for i in range(1,8):
    a = "C:sprites/Enginer004_00"+str(i)+".png"
    sprite.append(a)
Engineer[4]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer005_00"+str(i)+".png"
    sprite.append(a)
Engineer[5]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Enginer006_00"+str(i)+".png"
    sprite.append(a)
Engineer[6]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Enginer007_00"+str(i)+".png"
    sprite.append(a)
Engineer[7]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer008_00"+str(i)+".png"
    sprite.append(a)
Engineer[8]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer009_00"+str(i)+".png"
    sprite.append(a)
Engineer[9]=sprite
sprite=[]
for i in range(1,4):
    a = "C:sprites/Enginer010_00"+str(i)+".png"
    sprite.append(a)
Engineer[10]=sprite
sprite=[]
for i in range(1,2):
    a = "C:sprites/Enginer011_00"+str(i)+".png"
    sprite.append(a)
Engineer[11]=sprite
sprite=["C:sprites/Enginer012_001.png"]
Engineer[12]=sprite
sprite=["C:sprites/Enginer013_001.png"]
Engineer[13]=sprite
sprite=[]
sprite=["C:sprites/Enginer014_001.png"]
Engineer[14]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer015_00"+str(i)+".png"
    sprite.append(a)
Engineer[15]=sprite
sprite=["C:sprites/Enginer016_001.png"]
Engineer[16]=sprite
sprite=["C:sprites/Enginer017_001.png"]
Engineer[17]=sprite
sprite=["C:sprites/Enginer018_001.png"]
Engineer[18]=sprite
sprite=[]
for i in range(1,6):
    a = "C:sprites/Enginer019_00"+str(i)+".png"
    sprite.append(a)
Engineer[19]=sprite
sprite=["C:sprites/Enginer020_001.png"]
Engineer[20]=sprite
sprite=["C:sprites/Enginer021_001.png"]
Engineer[21]=sprite
sprite=["C:sprites/Enginer022_001.png"]
Engineer[22]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer023_00"+str(i)+".png"
    sprite.append(a)
Engineer[23]=sprite
sprite=[]
for i in range(1,3):
    a = "C:sprites/Enginer024_00"+str(i)+".png"
    sprite.append(a)
Engineer[24]=sprite
sprite=[]
for i in range(1,12):
    a = "C:sprites/Enginer025_00"+str(i)+".png"
    sprite.append(a)
Engineer[25]=sprite
sprite=[]
for i in range(1,9):
    a = "C:sprites/Enginer026_00"+str(i)+".png"
    sprite.append(a)
Engineer[26]=sprite
class Engineer_class(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.player=player        
        self.max_speed=10        
        self.jump_speed=20
        self.jumping=False
        self.player=player
        self.estado=0        
        self.x=0
        self.y=110
        if self.player==2:
            self.x=300
        
        self.stand=Engineer[0]
        self.lightpunch=Engineer[1]
        self.mediumpunch=Engineer[2]
        self.highpunch=Engineer[3]
        self.jump=Engineer[4]
        self.j_lightpunch=Engineer[5]
        self.j_mediumpunch=Engineer[6]
        self.j_highpunch=Engineer[7]
        self.down=Engineer[8]
        self.d_lightpunch=Engineer[9]
        self.d_mediumpunch=Engineer[10]
        self.guard=Engineer[11]
        self.d_guard=Engineer[12]
        self.j_guard=Engineer[13]
        self.dashfront=Engineer[14]
        self.dashback=Engineer[15]
        self.defense=Engineer[16]
        self.d_defense=Engineer[17]
        self.j_defense=Engineer[18]
        self.walk=Engineer[19]
        self.hit=Engineer[20]
        self.d_hit=Engineer[21]
        self.j_hit=Engineer[22]
        self.recover=Engineer[23]
        self.taunt=Engineer[24]
        self.especial=Engineer[25]
        self.effect=Engineer[26]
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

            if key[pygame.K_LEFT]:
                self.update('caminar')
                self.update_posicion(-10,0)
            if key[pygame.K_f]:
                self.update('LP')
            if key[pygame.K_g]:
                self.update('MP')
            if key[pygame.K_h]:
                self.update('HP')
            if key[pygame.K_RIGHT]:
                self.update('caminar')
                self.update_posicion(10,0)
                
        if event.type == pygame.KEYDOWN and self.player == 2:           

            if key[pygame.K_a]:
                self.update('caminar')
                self.update_posicion(-10,0)
            if key[pygame.K_u]:
                self.update('LP')
            if key[pygame.K_i]:
                self.update('MP')
            if key[pygame.K_o]:
                self.update('HP')
            if key[pygame.K_d]:
                self.update('caminar')
                self.update_posicion(10,0)          

 
        #if event.type == pygame.KEYUP:   
         #   if event.key == pygame.K_a or event.key==pygame.K_d:
          #      self.update('stand')            
           # if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
            #    self.update('stand')

 

        

    
