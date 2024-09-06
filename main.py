#testing this code


from random import randint
import pygame
from player import Player
from GridObject import GridObject
from ImageLoc import pacman_dir, monster_dir 
from introPage import StartEndScreen

pygame.init()


WIDTH, HEIGHT= 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('Arial', 36)


objects = []

SIZE = 25 
SCORE = 0
END_SCORE = 0

# Could add more to give it a higher resolution, sprite based
# graphics would be implemented by the GridObject and the Player class itself.
board = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


# Instantiating shit
player = Player(pos=(7,1),grid=board, size=SIZE, speed=3, graphicsPath="pacman-art", dir_shape=pacman_dir)
monsters = []

#num of monsters set here
for i in range(2):
    monster = Player(grid=board, pos=(1,1), size=SIZE, speed=5, color=(100,100,200), graphicsPath="pacman-art", dir_shape=monster_dir) 
    monsters.append(monster)

# Helper function to give some motion to the monsters
def pick_random_move():
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    return moves[randint(0, len(moves)-1)]

# Initialising the board.
for i in range(len(board)):
    for j in range(len(board[0])):
        val = board[i][j]
        if val == 0:
            END_SCORE += 1
        obj = GridObject(pos=(j, i), size=SIZE, board=board)
        objects.append(obj)
    


StartEndScreen(screen, "Press Space To Start", font, (255,255,10)).wait()


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
        print("\n\n\nYou Lost.")

 
    #check if the player is currently on a 'consumable item'
    playerX, playerY = player.pos

    
    if SCORE == END_SCORE:
        running = False
        print("\n\n\nYou won.") 
        
    if board[playerY][playerX] == 0:
        # 0 indicates a consumable here
        SCORE += 1 
        # set current board value to -1, to indicate that it has been consumed
        board[playerY][playerX] = -1
        
    text_surface = font.render(f"{SCORE}", True, (255,200,100))
    screen.blit(text_surface, (450,450))

    #for drawing the map 
    for obj in objects:
        obj.draw(screen)
    
    
    # Debug information.
    # print(player)

    pygame.display.flip()

    clock.tick(60)




pygame.quit()


