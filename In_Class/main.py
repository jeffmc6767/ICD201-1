import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (50, 100, 255)
GRAY  = (120, 120, 120)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

outline = 0
square_size = 40
squareX = WIDTH
squareY = 100
square_speed = 5

Light = 0
arm_state = 0
arm_counter = 0

def drawhouse():
    pygame.draw.rect(gameWindow, GRAY, (450, 250, 300, 300))
    pygame.draw.rect(gameWindow, BROWN, (580, 430, 60, 120))
    pygame.draw.rect(gameWindow, BLUE, (480, 280, 60, 60))
    pygame.draw.rect(gameWindow, BLUE, (480, 400, 60, 60))
    pygame.draw.rect(gameWindow, BLUE, (660, 400, 60, 60))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawhouse()


    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()