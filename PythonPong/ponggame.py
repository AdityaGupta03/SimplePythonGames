# Get pygame to use
import pygame

# Start pygame
pygame.init()

# Set the clock
clock = pygame.time.Clock()

# Draw screen
wide = 800
long = 500

# This function creates the screen
screen = pygame.display.set_mode((wide, long))
pygame.display.set_caption("Pong")

ball_wide = 30
ball_long = 30
ball_x = wide / 2 - ball_wide / 2
ball_y = long / 2 - ball_long / 2

# This function creates a pygame object to use (x position, y position, wide, long)
ball = pygame.Rect(ball_x, ball_y, ball_wide, ball_long)
ball_color = pygame.Color("aquamarine2")

rectangle_wide = 30
rectangle_long = 80
player1_paddle = pygame.Rect(100, 100, rectangle_wide, rectangle_long)
player2_paddle = pygame.Rect(700, 100, rectangle_wide, rectangle_long)

# Make a color for us to use
background_color = pygame.Color("gray15")

# speed tells us the direction and how much to move

# Player paddle speed
player2_speed = 0
player1_speed = 0

# Ball speeds
ball_x_speed = 5
ball_y_speed = 5

# Forever loop
while 1:
    # Go through each item in the list
    # Get all the events
    for event in pygame.event.get():
        # You are pressing a key on the keyboard
        are_you_pressing_a_key = pygame.KEYDOWN
        # A type is like the type of an event. An event can be clicking, typing on the keyboard, and more.
        if event.type == are_you_pressing_a_key:
            # You are pressing the down arrow key
            if event.key == pygame.K_DOWN:
                # set the speed to go down the screen
                player2_speed = 5
            # You are pressing the up arrow key
            if event.key == pygame.K_UP:
                # set the speed to go up the screen
                player2_speed = -5
            # You are pressing the s key
            if event.key == pygame.K_s:
                # Move down
                player1_speed = 5
            # You are pressing the w key
            if event.key == pygame.K_w:
                # Move up
                player1_speed = -5
        # If they click the red x button
        if event.type == pygame.QUIT:
            # Quit pygame and python!
            pygame.quit()
            exit()

    # Check if we hit the top of the screen and stop moving
    if player2_paddle.top == 0 and player2_speed == -5:
        player2_speed = 0

    # Check if we hit the bottom of the screen and stop moving
    if player2_paddle.bottom == long and player2_speed == 5:
        player2_speed = 0

    # Change the y position (height) of the player 2 paddle
    player2_paddle.y = player2_paddle.y + player2_speed

     # Check if we hit the top of the screen and stop moving
    if player1_paddle.top == 0 and player1_speed == -5:
        player1_speed = 0

    # Check if we hit the bottom of the screen and stop moving
    if player1_paddle.bottom == long and player1_speed == 5:
        player1_speed = 0

    # move the paddle
    player1_paddle.y = player1_paddle.y + player1_speed

    # ball.colliderect(paddle) checks if the ball (or pygame object) hit the paddle (any object) inside the ()
    # Check if we hit either paddle
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        print("You hit a paddle!")

    # Move the ball
    ball.y = ball.y + ball_y_speed
    ball.x = ball.x + ball_x_speed

    screen.fill(background_color)
    # Draw the object on the screen, of this color, and the object name
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.rect(screen, ball_color, player1_paddle)
    pygame.draw.rect(screen, ball_color, player2_paddle)
    # Update the screen
    pygame.display.flip()

    # Choose the frames the game will run in (just like in video games frames per second)
    # If no number is selected, the game will run very, very fast
    # This changes the speed of the game
    clock.tick(50)