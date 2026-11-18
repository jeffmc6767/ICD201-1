game_state = "PLAYING"

while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:   
        inPlay = False

    if game_state == "PLAYING":
        # ... your game logic, movement, and collisions ...
        
        if score1 == 7 or score2 == 7:
            game_state = "GAME_OVER"
            
    elif game_state == "GAME_OVER":
        gameWindow.fill(BLACK)
        
        # Render end credits text
        overText = gameOverFont.render("GAME OVER", True, WHITE)
        creditText = font.render("Thanks for playing! Built with Pygame.", True, BLUE)
        restartText = font.render("Press ESC to Exit", True, RED)
        
        gameWindow.blit(overText, (WIDTH // 2 - 120, 150))
        gameWindow.blit(creditText, (WIDTH // 2 - 250, 250))
        gameWindow.blit(restartText, (WIDTH // 2 - 150, 350))

    pygame.display.update()
    clock.tick(60)
