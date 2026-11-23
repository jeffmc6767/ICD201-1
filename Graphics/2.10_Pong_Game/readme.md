Pseudocode for project: 

IMPORT pygame
IMPORT random generator

#0. System and audio setup
IMPORT audio mixer 44100,-16,2,512
INITIALIZE pygame and font module

#1. Screen dimensions and colours
SET width to 800
SET height to 600
CREATE game window with dimensions width, height

SET white to RGB 255,255,255
SET black to RGB 0,0,0
SET red to RGB 255,0,0
SET blue to RGB 0,0,255

SET top to 0
SET bottom to height
SET left to 0
SET right to width

#2. Ball properties
SET ball radius to 15
SET ball X to width div 2
SET ball Y to height div 2
SET starting speed to 4
SET speed X to starting speed * random choice either -1 or 0
SET speed Y to starting speed * random choice either -1 or 0

#3. Paddle properties
SET paddle width to 15
SET paddle height to 100
SET paddle speed to 6 

SET paddle blue X = 30
SET paddle blue Y = (height - paddle height) div 2

SET paddle red X = width - 30 - paddle width
SET paddle red Y = (height - paddle height) div 2

#4. Score and game state
SET score blue = 0
SET score red = 0
SET winning score to 7

SET font to system font of Arial, size 40
SET game over font to system font of Arial, size 50
IMPORT game clock

LOAD background music “EndBoss.ogg”, set volume to 0.4, and play on infinite loop
LOAD sound effect “click.wav” as gulp, and set volume to 0.8
LOAD background image “toronto.png” and scale to (width, height)

SET in game to true
SET game state to “PLAYING”

#5. Main game loop
WHILE in game is true, 
GET current keyboard keys

#6. Exit condition
IF key Esc is pressed,
	SET in game to false

#7. Paddle blue controls
IF key W is pressed, 
	SET paddle blue Y to the max of either top or paddle blue Y - paddle speed

IF key S is pressed,
	SET paddle blue Y to the min of either bottom - paddle height, or paddle blue Y +         paddle shift
	
	
	#8. Paddle red controls
	IF key up arrow is pressed,
		SET paddle red Y to the max of either top, or paddle red Y - paddle speed
	
	IF the down arrow is pressed,
		SET paddle red Y to the min of either bottom - paddle height, or paddle red Y + paddle speed 
	
	
	#9. Updating ball position
	SET ball X to ball X + speed X
	SET ball Y to ball Y + speed Y
	
	#10. Checking win condition
	IF score blue is 7 or score red is 7,
		SET in game to false

	#11. Top and bottom wall collision
	IF ball Y - ball radius is <= top,
		SET ball Y to top + ball radius
		SET speed Y to negative of speed Y
	IF ball Y + ball radius >= bottom,
		SET ball Y to bottom - ball radius
		SET speedY to negative of speed Y
	
	#12. Paddle blue collision
	IF (ball X - ball radius <= paddle blue X + paddle width) AND
	    (ball X >= paddle blue X) AND
	    (paddle blue Y <= ball Y <= paddle blue Y + paddle height),
		SET speed X to negative of speed X * 1.05
		SET speed Y to speed Y * 1.05
		PLAY gulp sound

	#13. Paddle red collision
	IF (ball X + ball radius >= paddle red X ) AND
	    (ball X <= paddle red X + paddle width) AND
	    (paddle red Y <= ball Y <= paddle red Y + paddle height),
		SET speed X to negative of speed X * 1.05
		SET speed Y to speed Y * 1.05
		PLAY gulp sound

	#14. Ball goes through left
	IF ball X < left,
		SET score red to score red + 1
		SET ball X to width div 2
		SET ball Y to height div 2
		SET speed X to start speed * random choice between -1 or 0
		SET speed Y to start speed * random choice between -1 or 0
	
	#15. Ball goes through red
	IF ball X > right,
		SET score blue to score blue + 1
		SET ball X to width div 2
		SET ball Y to height div 2
		SET speed X to start speed * random choice between -1 or 0
		SET speed Y to start speed * random choice between -1 or 0
	
	#16. Graphics 
	FILL game with black
	DRAW blue rectangle at (paddle blue X, paddle blue Y) with size (paddle width, paddle height)
	DRAW red rectangle at (paddle red X, paddle red Y) with size (paddle width, paddle height)
	DRAW white circle at (ball X, ball Y) with ball radius
	
	RENDER score text blue to score blue in white using font
	RENDER score text red to score red in white using font
	DRAW score text blue at (width div 4, 20)
	DRAW score text red at ((width*3) div 4, 20)
	
	UPDATE display screen
	TICK clock at 60 fps
	PROCESS system events
	
#17. Game over screen
ELSE IF game state is “GAME_OVER”,
	FILL game window with black
	RENDER over text as “GAME OVER” in white using game over font
	RENDER credit text as “Thanks for playing!” in blue using font
		RENDER restart text as “Press ESC to Exit” in red using font
		
	
	DRAW over text at (Width div 2 - 120,150)
	DRAW credit text at (width div 2 - 250, 250)
	DRAW restart text at (width div 2 - 150, 350)

	UPDATE display screen
	TICK clock at 60 fps
#18. Exit
STOP background music
QUIT pygame
	





