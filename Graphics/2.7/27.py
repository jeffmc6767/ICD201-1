#########################################
# File Name: MusicAndSound.py
# Description: Car moves from riht to left. 
# Author: Jacy Qiu
# Date: 12/11/2026
#########################################
from random import randrange
from math import sqrt

import pygame
pygame.init()
HEIGHT = 600
WIDTH  = 800
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
OUTLINE=1

#---------------------------------------a#
# load the music and the sound          #
#---------------------------------------#
pygame.mixer.music.load("Graphics/2.7/EndBoss.ogg")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops = -1)
gulp = pygame.mixer.Sound("Graphics/2.7/click.mp3")

car = pygame.image.load("Graphics/2.7/car.png").convert()

backround = pygame.image.load("Graphics/2.7/toronto.png").convert()
backround = pygame.transform.scale(backround, (WIDTH, HEIGHT))



gulp.set_volume(0.8)

#---------------------------------------#
# main program                          #
#---------------------------------------#
objX = WIDTH//2
objY = HEIGHT//2
objR = 20
markerX = 0
markerY = 0
markerR = 20
carx = -100
cary = 250
move = 10

inPlay = True
while inPlay:
    gameWindow.fill(BLACK)      
    gameWindow.blit(backround, (0,0))       
    gameWindow.blit(car, (carx, cary))
    pygame.draw.circle(gameWindow,   RED, (objX,objY), objR, 0) 
    pygame.draw.circle(gameWindow, WHITE, (markerX,markerY), markerR, 0)
    pygame.display.update() 
    pygame.time.delay(30)

    carx += move
    if carx > WIDTH:
        carx = -100

    # move the white marker with the mouse
    markerX,markerY = pygame.mouse.get_pos()
    # use Pythagorean theorem to calculate the distance
    distance = sqrt((markerX-objX)**2+(markerY-objY)**2)
    # check for collision and move the object    
    if distance < objR + markerR:
        gulp.play()
        objX = randrange(0, WIDTH)
        objY = randrange(0, HEIGHT)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    pygame.event.clear()         
#---------------------------------------#  
pygame.mixer.music.stop()
pygame.quit()