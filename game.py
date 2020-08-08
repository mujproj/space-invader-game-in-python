import pygame
import random
import math
import time

# importing mixer module which heleps us to apply sounds to our game
from pygame import mixer

# initialising the pygame modules
pygame.init()

# Screen width
SCREEN_WIDTH = 800

# Screen height
SCREEN_HEIGHT = 600

# creating the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading the background image
background1 = pygame.image.load('background1.jpg')

# setting the caption of the window
pygame.display.set_caption("WELCOME TO SPACE INVADERS")

# setting the icon of the window
icon = pygame.image.load('ufoicon2.png')
pygame.display.set_icon(icon)

## PLAYER 
# loading the player image
player1 = pygame.image.load('player2.png')

## setting the dimesions where the image has to be loaded
# position of the image in x direction
playerX = 370

# position of the image in y direction
playerY = 480

# chnage in x direction
playerX_change = 0

# chnage in y direction
playerY_change = 0

## ENEMY
# loading the enemy image
enemy1 = pygame.image.load('enemy1.png')

## setting the dimesions where the image has to be loaded
# position of the image in x direction
enemyX = random.randint(0, 740)

# position of the image in y direction
enemyY = random.randint(50, 150)

# chnage in x direction
enemyX_change = 4

# chnage in y direction
enemyY_change = 40

## BULLET
# loading the bullet image
bullet1 = pygame.image.load('bullet1.png')

## defining the dimensions of bullets and corresponding variables
# defining the x position
bulletX = 0

#defining the y position
bulletY = 480

# defining the change in position in x direction
bulletX_change = 0

# defining the change in position in y direction
bulletY_change = 5

# defining the state of bullet fired or not
bulletState = "ready"

# deffinig player score
score_value = 0

# setting the style of the font for score
font = pygame.font.Font('freesansbold.ttf', 32)

# setting the dimesions of the text
textX = 10
textY = 10

# setting the style of the font for game over
fontgameover = pygame.font.Font('freesansbold.ttf', 64)

# setting the dimensions of the game over text
gameoverX = 50
gameoverY = 50

# defining the function to display the score
def displayscore(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# defining the function to display gameover function
def displayGameOver(x, y):
    gameOver = fontgameover.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameOver, (x, y))

# defining the function to display the image of the player on the screen
def player(x, y):
    screen.blit(player1, (x, y))

# defining the function to display the image of the enemy on the screen
def enemy(x, y):
    screen.blit(enemy1, (x, y))

# defining the function to display the image of the bullet
# def bullet(x, y):
#     screen.blit(bullet1, (x, y))

# defining a function to tell the state of the bullet
def bullet_fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bullet1, (x + 16, y + 10))
    
    # loading the music for firing a bullet
    mixer.music.load('bulletsound.wav')

    # playing the music
    mixer.music.play()

# defining a function to check collision
def isCollision(x1, y1, x2, y2):

    if math.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1))) <= 20:

        # loading the music for when collision occurs
        mixer.music.load('explosionsound.wav')

        # playing the music when collision occurs
        mixer.music.play()

        # return True if collision occured
        return True

    else:
        return False

# creating a variable that would make the game loop work till its true. as soon as it is set to false, the loop will end and game will be over
running = True 

# game loop starts
while running:

    # setting the window color black again
    screen.fill((0, 0, 0))

    # displaying the background image
    screen.blit(background1, (0, 0))

    # retrieving all the events one by one
    for event in pygame.event.get():

        # searching for an event quit, as soon as we get that we would quit the game by setting running as false
        if event.type == pygame.QUIT:

            # setting the running variable to false
            running = False 

        ## if key stroke is pressed, check if its right or left
        # this checks if key stroke is pressed down. keydown means the key has been pressed down.
        if event.type == pygame.KEYDOWN:
            # print("HERE")
            # checking if key is left
            if event.key == pygame.K_LEFT:
                # print("LEFT ARROW IS PRESSED")
                playerX_change = -4

            # checking if key is right
            if event.key == pygame.K_RIGHT:
                # print("RIGHT ARROW IS PRESSED")
                playerX_change = 4
            
            # checking for space key to fire the bullet
            if event.key == pygame.K_SPACE:

                if bulletState == 'ready':
                    bulletX = playerX
                    # call the funcyion fire bullet to fire the bullet
                    bullet_fire(bulletX, bulletY)

        ## if they key stroke is released , it means keyup
        if event.type == pygame.KEYUP:

            # checking if left or right key is unpressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("LEFT OR RIGHT ARROW KEY IS BEING PRESSED")
                playerX_change = 0

    # this is changing the position of player in x direction
    playerX += playerX_change

    # setting up restriction on the boundary for player
    if playerX <= 0:
        playerX = 0

    if playerX >= 740:
        playerX = 740

    # enemy changing posiion in x direction
    enemyX += enemyX_change

    # sertting up restriction on the booundary for enemy
    if enemyX <= 0:
        enemyX_change = 4
        # print("HER2")
        enemyY += enemyY_change

    if enemyX >= 740:
        enemyX_change = -4
        # print("HER1")
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision function, checking if collision occured between bullet and enemy, if occured increase the score
    if isCollision(enemyX, enemyY, bulletX, bulletY):

        bulletY = 480
        bulletState = "ready"

        # increasing the score of player
        score_value = score_value + 1
        # print(score)

        # resetting the enemy after collision
        enemyX = random.randint(0, 740)
        enemyY = random.randint(50, 150)

    if (playerY - enemyY) < 40:
        print("GAME OVER")
        displayGameOver(gameoverX, gameoverY)
        # time.sleep(40)
        exit()

    # this function would return display the player image according to the dimension set
    player(playerX, playerY)

    # this function would return display the enemy image according to the dimensions
    enemy(enemyX, enemyY)

    # this function returns the text to be displayed according to the dimension
    displayscore(textX, textY)

    # this function would return display the bullet image according to the dimensions
    # bullet(0, 0)
    # this updates the pygamme module
    pygame.display.update()
