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

collision = None
objects = []


SIZE = 75

board = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0],
    [1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,1],
    [1,0,0,0,0,1,1,1],
    [1,0,1,1,0,1,1,1],

]
    
for i in range(len(board)):
    for j in range(len(board[0])):
        val = board[i][j]

        if val == 0:
            continue

        obj = GridObject(pos=(SIZE*i, SIZE*j), dim=(SIZE, SIZE))
        objects.append(obj)
        

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
    
    for obj in objects:
        obj.draw(screen)
            

    #simple collision detection
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


