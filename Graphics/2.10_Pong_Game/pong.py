import pygame
import random

pygame.init()
pygame.font.init()

WIDTH,HEIGHT = 800, 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

TOP = 0  
BOTTOM = HEIGHT
LEFT = 0     
RIGHT = WIDTH         

BALL_RADIUS = 15
ballX = WIDTH // 2
ballY = HEIGHT // 2
INITIAL_SPEED = 4
speedX = INITIAL_SPEED * random.choice([-1, 1])
speedY = INITIAL_SPEED * random.choice([-1, 1])

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SHIFT = 6

paddle1X = 30
paddle1Y = (HEIGHT - PADDLE_HEIGHT) // 2

paddle2X = WIDTH - 30 - PADDLE_WIDTH
paddle2Y = (HEIGHT - PADDLE_HEIGHT) // 2

score1 = 0
score2 = 0
WINNING_SCORE = 7

font = pygame.font.SysFont("Arial", 40)
gameOverFont = pygame.font.SysFont("Arial", 50)

print("Hit ESC to end the program.")
inPlay = True
clock = pygame.time.Clock()

while inPlay:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:   
        inPlay = False
        
    if keys[pygame.K_w]:
        paddle1Y = max(TOP, paddle1Y - PADDLE_SHIFT)
    if keys[pygame.K_s]:
        paddle1Y = min(BOTTOM - PADDLE_HEIGHT, paddle1Y + PADDLE_SHIFT)
        
    if keys[pygame.K_UP]:
        paddle2Y = max(TOP, paddle2Y - PADDLE_SHIFT)
    if keys[pygame.K_DOWN]:
        paddle2Y = min(BOTTOM - PADDLE_HEIGHT, paddle2Y + PADDLE_SHIFT)

    ballX += speedX
    ballY += speedY

    if score1 == 7 or score2 == 7:
        inPlay = False
    
    if ballY - BALL_RADIUS <= TOP:
        ballY = TOP + BALL_RADIUS  
        speedY = -speedY
    if ballY + BALL_RADIUS >= BOTTOM:
        ballY = BOTTOM - BALL_RADIUS 
        speedY = -speedY

    if (ballX - BALL_RADIUS <= paddle1X + PADDLE_WIDTH and 
        ballX >= paddle1X and 
        paddle1Y <= ballY <= paddle1Y + PADDLE_HEIGHT):
        speedX = -speedX

    if (ballX + BALL_RADIUS >= paddle2X and 
        ballX <= paddle2X + PADDLE_WIDTH and 
        paddle2Y <= ballY <= paddle2Y + PADDLE_HEIGHT):
        speedX = -speedX

    if ballX < LEFT:
        score2 += 1
        ballX = WIDTH // 2
        ballY = HEIGHT // 2
        speedX = INITIAL_SPEED * random.choice([-1, 1])
        speedY = INITIAL_SPEED * random.choice([-1, 1])

    if ballX > RIGHT:
        score1 += 1
        ballX = WIDTH // 2
        ballY = HEIGHT // 2
        speedX = INITIAL_SPEED * random.choice([-1, 1])
        speedY = INITIAL_SPEED * random.choice([-1, 1])

    gameWindow.fill(BLACK)
    
    
    pygame.draw.rect(gameWindow, BLUE, (paddle1X, paddle1Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(gameWindow, RED, (paddle2X, paddle2Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), BALL_RADIUS)
    
    scoreText1 = font.render(str(score1), True, WHITE)
    scoreText2 = font.render(str(score2), True, WHITE)
    gameWindow.blit(scoreText1, (WIDTH // 4, 20))
    gameWindow.blit(scoreText2, (WIDTH * 3 // 4, 20))
    
    pygame.display.update()
    
    clock.tick(60)
    pygame.event.pump()
