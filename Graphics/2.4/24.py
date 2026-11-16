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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameWindow.fill(BLACK)

    # Building
    pygame.draw.rect(gameWindow, GRAY, (450, 250, 300, 300))
    pygame.draw.rect(gameWindow, BROWN, (580, 430, 60, 120))
    pygame.draw.rect(gameWindow, BLUE, (480, 280, 60, 60))
    pygame.draw.rect(gameWindow, BLUE, (480, 400, 60, 60))
    pygame.draw.rect(gameWindow, BLUE, (660, 400, 60, 60))

    Light += 1
    if (Light // 30) % 2 == 0:
        pygame.draw.rect(gameWindow, YELLOW, (660, 280, 60, 60))
    else:
        pygame.draw.rect(gameWindow, GRAY, (660, 280, 60, 60))

    # Stick figure waving
    arm_counter += 1
    if arm_counter >= 20:
        arm_state = 1 - arm_state
        arm_counter = 0

    pygame.draw.circle(gameWindow, WHITE, (200, 380), 20, 2)
    pygame.draw.line(gameWindow, WHITE, (200, 400), (200, 480), 2)
    pygame.draw.line(gameWindow, WHITE, (200, 480), (170, 550), 2)
    pygame.draw.line(gameWindow, WHITE, (200, 480), (230, 550), 2)
    pygame.draw.line(gameWindow, WHITE, (200, 420), (160, 450), 2)

    if arm_state == 0:
        pygame.draw.line(gameWindow, WHITE, (200, 420), (240, 450), 2)  # Arm down
    else:
        pygame.draw.line(gameWindow, WHITE, (200, 420), (250, 390), 2)  # Arm up

    squareX = ((squareX - square_speed + square_size) % (WIDTH + square_size)) - square_size
    pygame.draw.rect(gameWindow, RED, (squareX, squareY, square_size, square_size), outline)

    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()