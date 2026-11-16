import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

# color define
RED  =(255,  0,  0)
GREEN=(  0,255,  0)
BLUE =(  0,  0,255)
WHITE=(255,255,255)
outline=0

# Ball define
ballX = 100                        
ballY = 240                            
ballR = 30                             
stepX = 10                         
stepY = 10                             

while True:
    for i in range(100):  
        pygame.event.clear()
        gameWindow.fill(WHITE)
        if i == 0:
# Random generation 
            randomx1 = random.randint(0, WIDTH)      
            randomy1 = random.randint(0, HEIGHT)
            randomx2 = random.randint(0, WIDTH)      
            randomy2 = random.randint(0, HEIGHT)
            randomx3 = random.randint(0, WIDTH)      
            randomy3 = random.randint(0, HEIGHT)
            randomx4 = random.randint(0, WIDTH)      
            randomy4 = random.randint(0, HEIGHT)

# 4 Balls
        pygame.draw.circle(gameWindow, RED, (ballX, randomy1), ballR, outline)
        pygame.draw.circle(gameWindow, RED, (randomx1, ballY), ballR, outline)
        pygame.draw.circle(gameWindow, RED, (ballX, randomy1+75), ballR, outline)
        pygame.draw.circle(gameWindow, RED, (randomx1+75, ballY), ballR, outline)

        pygame.display.update()
        pygame.time.delay(10)

# Movement
        ballX = ballX + stepX
        ballY = ballY + stepY

        if ballX>=WIDTH or ballX<=0:        # if the ball passes the left or right border of the gameWindow
            stepX = -stepX                  # reverse the direction of horizontal movement

        if ballY>=HEIGHT or ballY<=0:       # if the ball passes the top or bottom of the gameWindow
            stepY = -stepY                  # reverse the direction of vertical movement