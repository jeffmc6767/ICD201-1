#########################################
# File Name: ClockFPSexample.py
# Description: This program demonstrates how to use Clock object to set timed loop speed.
#               https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
# Author: ICS2O
# Date: 17/10/2018
#########################################
import pygame
pygame.init()
WIDTH  = 800
HEIGHT = 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

BLACK, WHITE, RED, BLUE,GREY,BROWN,YELLOW = (0, 0, 0), (255, 255, 255), (255, 0, 0), ( 140, 180, 245), (120, 120, 120), (139, 69, 19), (255, 255, 0)

font = pygame.font.SysFont("Arial",36)
    
clock = pygame.time.Clock()
FPS = 24                                
seconds = 0                               

rocket1,rocket2,rocket3,rocket4,rocket5,rocket6 = 450,500,550,600,650,700

inPlay = True
while inPlay:
    gameWindow.fill(BLACK)
    graphics = font.render(f"Time: {seconds:.2f} s", 1, GREY) 
    gameWindow.blit(graphics, (32, 32))    
    clock.tick(FPS)
    seconds = pygame.time.get_ticks() / 1000.0 
# Rocket code:
    pygame.draw.rect(gameWindow, RED, (500, rocket2, 50, 100))
    pygame.draw.polygon(gameWindow, YELLOW, [(500, rocket2), (525, rocket1), (550, rocket2)]) 

    rocket1 -= 5
    rocket2 -= 5



## Escape
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    pygame.event.clear()     
    pygame.display.update()

pygame.quit()