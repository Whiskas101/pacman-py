# Testing this code


from random import randint
import pygame
from player import Player
from GridObject import GridObject
from ImageLoc import pacman_dir, monster_dir 

pygame.init()



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True



objects = []

SIZE = 50 

# Could add more to give it a higher resolution, sprite based
# graphics would be implemented by the GridObject and the Player class itself.
board = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Instantiating shit
player = Player(pos=(7,1),grid=board, dim=(SIZE,SIZE), speed=5, graphicsPath="pacman-art", dir_shape=pacman_dir)
monsters = []

#num of monsters set here
for i in range(4):
    monster = Player(grid=board, pos=(1,1), dim=(SIZE, SIZE), speed=3, color=(100,100,200), graphicsPath="pacman-art", dir_shape=monster_dir) 
    monsters.append(monster)

# Helper function to give some motion to the monsters
def pick_random_move():
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    print("moving")
    return moves[randint(0, len(moves)-1)]

# Initialising the board.
for i in range(len(board)):
    for j in range(len(board[0])):
        val = board[i][j]

        if val == 0:
            continue

        obj = GridObject(pos=(SIZE*j, SIZE*i), dim=(SIZE, SIZE))
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
    

    for dumb_ai in monsters:
        random_direction = pick_random_move()
        dumb_ai.set_direction(random_direction)
        dumb_ai.move()

    player.move();

    screen.fill((0,0,0))
    
    # rendering works here
    player.draw(screen)   
    for dumb_ai in monsters:
        dumb_ai.draw(screen)



    #detecting collisions and ending game
    # Method returns the indexes of all items that collided with the player
    indices = player.collidelistall(monsters)

    #simple: end the game the instant theres any collisions
    if len(indices) > 0:
        running = False # Simple end rule


 

    #for drawing the map 
    for obj in objects:
        obj.draw(screen)
            
    # Debug information.
    # print(player)
    
    pygame.display.flip()

    clock.tick(60)




pygame.quit()


