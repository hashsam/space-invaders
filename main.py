import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-ship (1).png')
pygame.display.set_icon(icon)
background = pygame.image.load('backgroung.jpg')

playerImg = pygame.image.load('arcade-game (2).png')
playerX = 385
playerY = 500
playerX_change = 0

enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

score = 0


def player(X, Y):
    screen.blit(playerImg, (X, Y))


def enemy(X, Y):
    screen.blit(enemyImg, (X, Y))


def fire_bullet(X, Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (X + 16, Y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
