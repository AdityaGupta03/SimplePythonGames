import pygame, random

#Perform necessary pygame functions
pygame.init()
clock = pygame.time.Clock()

#Specify the size of the playing screen and start it
screen_width = 960
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Create shapes for the player paddles and the ball and their starting positions
#Keep in mind the top left corner of the screen is coordinate 0, 0.
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

#Choose colors for each object
bkg_color = pygame.Color("gray15")
object_color = pygame.Color("white")

#Choose the starting speeds that the objects move with
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
player1_speed = 0
player2_speed = 0

#Score variables
player1_score = 0
player2_score = 0

#Create a font for writing to the screen
font = pygame.font.Font("freesansbold.ttf", 32)

#Do this forever
while 1:
    #For each button the user presses do something
    for event in pygame.event.get():
        #If the person hits a keyboard key
        if event.type == pygame.KEYDOWN:
            #If the key is s, then move player 1 down
            if event.key == pygame.K_s and player1_speed != 5:
                player1_speed = 5
            #If the key is w, then move player 1 up
            if event.key == pygame.K_w and player1_speed != -5:
                player1_speed = -5
            #If the key is up arrow, then move player 2 up
            if event.key == pygame.K_UP and player2_speed != -5:
                player2_speed = -5
            #If the key is down arrow, then move player 2 down
            if event.key == pygame.K_DOWN and player2_speed != 5:
                player2_speed = 5
        #If the person hits the red x button to close the program
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #If the ball hits either the top or bottom then change the speed to be the reverse direction
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    #If the ball hits either the left or right side then add the point to the other player and reset the ball
    elif ball.left <= 0:
        player2_score += 1
        print(player2_score)
        ball_speed_x = -5
        ball.center = (screen_width / 2, screen_height / 2) #type: ignore
    elif ball.right >= screen_width:
        player1_score += 1
        print(player1_score)
        ball_speed_x = 5
        ball.center = (screen_width / 2, screen_height / 2) #type: ignore

    #If the player hits the top or bottom and try to move past edge of the screen, stop them
    if player1.top <= 0 and player1_speed == -5:
        player1_speed = 0
    if player1.bottom >= screen_height and player1_speed == 5:
        player1_speed = 0

    #Move the player
    player1.y += player1_speed

    #Repeat the player logic for player2
    if player2.top <= 0 and player2_speed == -5:
        player2_speed = 0
    if player2.bottom >= screen_height and player2_speed == 5:
        player2_speed = 0

    player2.y += player2_speed

    #If the ball hits one of the players then move its x speed to opposite direction
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    #Fill the screen with the background color
    screen.fill(bkg_color)
    #Draw the player1 rectangle with the color we chose earlier
    pygame.draw.rect(screen, object_color, player1)
    #Draw the player2 rectangle with the color we chose earlier
    pygame.draw.rect(screen, object_color, player2)
    #Draw the ball following the same logic as the players
    pygame.draw.ellipse(screen, object_color, ball)
    #Draw a dividing line in the center of the screen
    pygame.draw.aaline(screen, object_color, (screen_width/2,0), (screen_width/2, screen_height))

    #Draw the score
    player1_text = font.render(f"{player1_score}", True, object_color)
    screen.blit(player1_text, (screen_width / 2 - 50, screen_height / 2 - 50))
    player2_text = font.render(f"{player2_score}", True, object_color)
    screen.blit(player2_text, (screen_width / 2 + 50, screen_height / 2 - 50))

    #Update the screen
    pygame.display.flip()
    
    #Choose the frames the game will run in (just like in video games frames per second)
    #If no number is selected, the game will run very, very fast
    clock.tick(60)

    if player1_score == 5:
        congrats_text = font.render("Congratulations Player 1!", True, object_color)
        screen.blit(congrats_text, (screen_width / 2 - 200, 50))
        pygame.display.flip()
        pygame.time.wait(2100)
        pygame.quit()
        exit()
    if player2_score == 5:
        congrats_text = font.render("Congratulations Player 2!", True, object_color)
        screen.blit(congrats_text, (screen_width / 2 - 200, 50))
        pygame.display.flip()
        pygame.time.wait(2100)
        pygame.quit()
        exit()