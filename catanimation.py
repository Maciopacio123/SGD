import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')

cat1x = 10
cat1y = 10
cat1_direction = 'right'

cat2x = 300
cat2y = 200
cat2_direction = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if cat1_direction == 'right':
        cat1x += 5
        if cat1x >= 280:
            cat1_direction = 'down'
    elif cat1_direction == 'down':
        cat1y += 5
        if cat1y >= 220:
            cat1_direction = 'left'
    elif cat1_direction == 'left':
        cat1x -= 5
        if cat1x <= 10:
            cat1_direction = 'up'
    elif cat1_direction == 'up':
        cat1y -= 5
        if cat1y <= 10:
            cat1_direction = 'right'

    if cat2_direction == 'left':
        cat2x -= 5
        if cat2x <= 10:
            cat2_direction = 'up'
    elif cat2_direction == 'up':
        cat2y -= 5
        if cat2y <= 10:
            cat2_direction = 'right'
    elif cat2_direction == 'right':
        cat2x += 5
        if cat2x >= 280:
            cat2_direction = 'down'
    elif cat2_direction == 'down':
        cat2y += 5
        if cat2y >= 220:
            cat2_direction = 'left'

    DISPLAYSURF.blit(catImg, (cat1x, cat1y))
    DISPLAYSURF.blit(catImg, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)