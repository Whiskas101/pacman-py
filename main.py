# Testing this code


import pygame
from player import Player
from GridObject import GridObject
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
running = True

player = Player(speed=10)
obstacle = GridObject(dim=(200,200))

collision = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() 

    if keys[pygame.K_UP]:
        player.move("UP")
    if keys[pygame.K_DOWN]:
        player.move("DOWN")
    if keys[pygame.K_LEFT]:
        player.move("LEFT")
    if keys[pygame.K_RIGHT]:
        player.move("RIGHT")

    screen.fill("purple")
    
    # rendering works here
    player.draw(screen)    
    obstacle.draw(screen)

    collision = player.rect.collidelistall([obstacle])
    if collision:
        print(collision)

    #simple collision detection
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


