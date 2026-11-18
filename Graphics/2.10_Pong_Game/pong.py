import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()

# Set display 
WIDTH,HEIGHT = 800, 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Constraints  
TOP = 0  
BOTTOM = HEIGHT
LEFT = 0     
RIGHT = WIDTH         

# Ball settings
BALL_RADIUS = 15
ballX = WIDTH // 2
ballY = HEIGHT // 2
INITIAL_SPEED = 4
speedX = INITIAL_SPEED * random.choice([-1, 1])
speedY = INITIAL_SPEED * random.choice([-1, 1])

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SHIFT = 6

paddle1X = 30
paddle1Y = (HEIGHT - PADDLE_HEIGHT) // 2

paddle2X = WIDTH - 30 - PADDLE_WIDTH
paddle2Y = (HEIGHT - PADDLE_HEIGHT) // 2

# Score def
score1 = 0
score2 = 0
WINNING_SCORE = 7

# Fond settings
font = pygame.font.SysFont("Arial", 40)
gameOverFont = pygame.font.SysFont("Arial", 50)

clock = pygame.time.Clock()

# Music load and settings
pygame.mixer.music.load("Graphics/2.10_Pong_Game/EndBoss.ogg")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops = -1)

# Click settings
gulp = pygame.mixer.Sound("Graphics/2.10_Pong_Game/click.wav")
gulp.set_volume(0.8)

# Backround load
backround = pygame.image.load("Graphics/2.10_Pong_Game/toronto.png").convert()
backround = pygame.transform.scale(backround, (WIDTH, HEIGHT))

# Main loop
inPlay = True
game_state = "PLAYING"
while inPlay:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:   
        inPlay = False
# Score set status
    if score1 == 7 or score2 == 7:
        print("Game over")
        game_state = "GAME_OVER"

# If playing
    if game_state == "PLAYING":
        if inPlay == True: 
            gameWindow.blit(backround, (0,0))       

# Left paddle move
        if keys[pygame.K_w]:
            paddle1Y = max(TOP, paddle1Y - PADDLE_SHIFT)
        if keys[pygame.K_s]:
            paddle1Y = min(BOTTOM - PADDLE_HEIGHT, paddle1Y + PADDLE_SHIFT)

# Right paddle move  
        if keys[pygame.K_UP]:
            paddle2Y = max(TOP, paddle2Y - PADDLE_SHIFT)
        if keys[pygame.K_DOWN]:
            paddle2Y = min(BOTTOM - PADDLE_HEIGHT, paddle2Y + PADDLE_SHIFT)


        ballX += speedX
        ballY += speedY

# Ball collision
        if ballY - BALL_RADIUS <= TOP:
            ballY = TOP + BALL_RADIUS  
            speedY = -speedY

        if ballY + BALL_RADIUS >= BOTTOM:
            ballY = BOTTOM - BALL_RADIUS 
            speedY = -speedY

# Ball bounce and speed up 
        if (ballX - BALL_RADIUS <= paddle1X + PADDLE_WIDTH and 
            ballX >= paddle1X and 
            paddle1Y <= ballY <= paddle1Y + PADDLE_HEIGHT):
            speedX = -speedX * 1.05
            speedY = speedY * 1.05
            gulp.play()


        if (ballX + BALL_RADIUS >= paddle2X and 
            ballX <= paddle2X + PADDLE_WIDTH and 
            paddle2Y <= ballY <= paddle2Y + PADDLE_HEIGHT):
            speedX = -speedX * 1.05
            speedY = speedY * 1.05
            gulp.play()

# Ball reset location
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

        
# Paddle, ball        
        pygame.draw.rect(gameWindow, BLUE, (paddle1X, paddle1Y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(gameWindow, RED, (paddle2X, paddle2Y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), BALL_RADIUS)

# Score        
        scoreText1 = font.render(str(score1), True, WHITE)
        scoreText2 = font.render(str(score2), True, WHITE)
        gameWindow.blit(scoreText1, (WIDTH // 4, 20))
        gameWindow.blit(scoreText2, (WIDTH * 3 // 4, 20))
        
        pygame.display.update()
        
        clock.tick(60)
        pygame.event.get()
# If game over make end screen
    elif game_state == "GAME_OVER":
            gameWindow.fill(BLACK)
            
            overText = gameOverFont.render("GAME OVER", True, WHITE)
            creditText = font.render("Thanks for playing!", True, BLUE)
            restartText = font.render("Press ESC to Exit", True, RED)
            
            gameWindow.blit(overText, (WIDTH // 2 - 120, 150))
            gameWindow.blit(creditText, (WIDTH // 2 - 250, 250))
            gameWindow.blit(restartText, (WIDTH // 2 - 150, 350))

            pygame.display.update()
            clock.tick(60)
    
pygame.mixer.music.stop()    
pygame.quit()
