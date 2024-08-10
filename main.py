# Testing this code


from random import randint
import pygame
from player import Player
from GridObject import GridObject
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
running = True



collision = None
objects = []

SIZE = 75

# Could add more to give it a higher resolution, sprite based
# graphics would be implemented by the GridObject.
board = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,1],
    [1,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1],
]

player = Player(grid=board, dim=(75,75), speed=5)
dumb_ai = Player(grid=board, pos=(1,1), dim=(75, 75), speed=3, color=(100,100,200))

def pick_random_move():
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    print("moving")
    return moves[randint(0, len(moves)-1)]


for i in range(len(board)):
    for j in range(len(board[0])):
        val = board[i][j]

        if val == 0:
            continue

        obj = GridObject(pos=(SIZE*i, SIZE*j), dim=(SIZE, SIZE))
        objects.append(obj)
        

while running:
    # Might cause the program to become a ghost process without this,
    # or a persistent window that keeps popping up.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # user input
    keys = pygame.key.get_pressed() 

    if keys[pygame.K_UP]:
        player.set_direction("UP")
    if keys[pygame.K_DOWN]:
        player.set_direction("DOWN")
    if keys[pygame.K_LEFT]:
        player.set_direction("LEFT")
    if keys[pygame.K_RIGHT]:
        player.set_direction("RIGHT")
    

    random_direction = pick_random_move()
    dumb_ai.set_direction(random_direction)

    player.move();
    dumb_ai.move();

    screen.fill("purple")
    
    # rendering works here
    player.draw(screen)   
    dumb_ai.draw(screen)
    
    for obj in objects:
        obj.draw(screen)
            
    # Debug information.
    print(player)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


