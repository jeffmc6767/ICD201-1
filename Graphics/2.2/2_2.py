import sys
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gameWindow.fill(BLUE)

    pygame.draw.polygon(
        gameWindow, GREY, [(350, 450), (450, 450), (550, 600), (250, 600)]
    )

    pygame.draw.rect(gameWindow, WHITE, (250, 250, 300, 200))
    pygame.draw.rect(gameWindow, BLACK, (250, 250, 300, 200), 3)

    pygame.draw.polygon(gameWindow, RED, [(230, 250), (400, 120), (570, 250)])
    pygame.draw.polygon(
        gameWindow, BLACK, [(230, 250), (400, 120), (570, 250)], 3
    )

    pygame.draw.rect(gameWindow, BROWN, (370, 350, 60, 100))
    pygame.draw.circle(gameWindow, YELLOW, (420, 400), 5)

    pygame.draw.rect(gameWindow, BLUE, (280, 290, 60, 60))
    pygame.draw.rect(gameWindow, BLACK, (280, 290, 60, 60), 2)

    pygame.draw.rect(gameWindow, BLUE, (460, 290, 60, 60))
    pygame.draw.rect(gameWindow, BLACK, (460, 290, 60, 60), 2)

    pygame.display.update()
    clock.tick(60)