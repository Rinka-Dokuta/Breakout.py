#Import the pygame libary and initialise the game engine
import pygame
pygame.init()
import random

#open a new window, caption it "Breakout"
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Breakout")

#Here's the variable that runs our game loop
doExit = False

#The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Paddle postion
p1x = 350
p1y = 445

mousePos = (400,400)

#Ball variables
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vertical speed)

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100,250),random.randrange(100,250),random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50)) #Width ad height are 100 and 50
    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + 20 > self.xpos and
                ball_x < self.xpos + 100 and #Width of brick is 100
                ball_y + 20 > self.ypos and
                ball_y < self.ypos + 50): #Height of brick is 50 
                self.isDead = True
                return True
            return False
b1 = brick(50, 50)#Goes above game loop
b2 = brick(200, 50)
b3 = brick(350, 50)
b4 = brick(500, 50)
b5 = brick(650, 50) 
b6 = brick(50, 150)
b7 = brick(200, 150)
b8 = brick(350, 150)
b9 = brick(500, 150)
b10 = brick(650,150)
p1Score = 0
while not doExit: #GAME LOOP-----------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        print(mousePos) 
    
    
    
    #Event queue stuff------------------------
    clock.tick(60) #set the FPS
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #Flag that we are done so we exit game loop
            
    #game logic will go here----------------
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_a]:#Move left
       p1x-=5
    if Keys[pygame.K_d]:#Move right
      p1x+=5
    
    #pshyics
    if b1.collide(bx, by):#Ball collision with each brick
        bVy *= -1
    if b2.collide(bx, by):
        bVy *= -1
    if b3.collide(bx, by):
        bVy *= -1
    if b4.collide(bx, by):
        bVy *= -1
    if b5.collide(bx, by):
        bVy *= -1
    if b6.collide(bx, by):
        bVy *= -1
    if b7.collide(bx, by):
        bVy *= -1
    if b8.collide(bx, by):
        bVy *= -1
    if b9.collide(bx, by):
        bVy *= -1
    if b10.collide(bx, by):
        bVy *= -1
    if b1.collide(bx, by):
        bVy *= -1
    
    
    #ball movement
    bx += bVx
    by += bVy
     
    #reflect ball off side walls of screen
    #if bx < 0 or bx + 20 > 700:
    #    bVx *= -1
    
    
    #reflect ball off top and bottom    
    if by < 0 or by + 20 > 500:
        bVy *= -1
        
    #ball-paddle reflection    
    if bx < p1x + 100 and by + 20 > p1y and by < p1y + 20: 
         bVx *= -1
         bVy *= -1
     
       
    
    #reflect ball off side walls of screen, change score 
    if bx < 0: #this has been split up from right wall collision so we can increase scores
        bVx *= -1
        
   
    #add score for the right wall here
    if bx + 20 > 700:
        bVx*= -1
        

    #render section will go here--------------
   
    screen.fill((0,0,0)) #wipe screen black
    #First paddle
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 100, 20), 4)
    
   
            
    #Ball
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)
     
           
    #display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (220,10))

    
    b1.draw()#Draw bricks on screen
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    
    #update the screen
    pygame.display.flip()
            
            
#END GAME LOOP------------------------------------------------

pygame.quit()#when game is done close down pygame
             
