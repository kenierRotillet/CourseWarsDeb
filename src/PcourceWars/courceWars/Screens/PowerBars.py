import sys, pygame

width, height = 1024, 450
red1=(139,0,0)
red2=(178,34,34)
blue1=(100,149,237)
blue2=(128,169,242)
grey=(192,192,192)

class Power_Bar(object):
    def __init__(self, Screen,NumJug):
        self.screen = Screen
        self.numJug = NumJug
        self.counter1 = 0
        self.contador1 = 0
        self.counter2 = 0
        self.contador2 = 0

    def draw(self,power):
        if power == 100 and self.counter1 == 10:
            color=red2
            self.contador1-=1
        else:
            if power == 100:
                color=red1
                self.counter1+=1
                self.contador1+=1
            else:
                if self.counter2 == 10:
                    color =blue2
                    self.contador2-=1
                else:
                    color=blue1
                    self.counter2+=1
                    self.contador2+=1                
        if self.contador1 == 0:
            self.counter1=0
        if self.contador2 == 0:
            self.counter2=0
                
        if(self.numJug == 1):
            pygame.draw.rect(self.screen,grey,(230,60,200,10),0)
            pygame.draw.rect(self.screen,color,(430,60,-power*2,10),0)
        else:
            pygame.draw.rect(self.screen,grey,(width - 430,60,200,10),0)
            pygame.draw.rect(self.screen,color,(width - 430,60,power*2,10),0)
            

