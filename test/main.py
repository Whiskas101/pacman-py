import pygame


pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

board = [

[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,1,1,0,0,1,1,1,1,1],
[1,0,1,1,1,1,0,1,1,1,1,1],
[1,0,1,1,1,1,0,1,1,1,1,1],
[1,0,0,0,0,0,0,1,1,1,1,1],
[1,0,1,1,0,1,0,1,1,1,1,1],
[1,0,0,1,1,1,0,0,0,1,1,1],
[1,1,1,1,1,1,0,1,0,0,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1],

]

CELL = 25
running = True


class Player:
    def __init__(self, pos, size, board):
        self.pos = pos
        self.size = size
        self.speed = 1 
        y, x = self.pos
        self.actualPos = (x*self.size, y*self.size)
        self.board = board
        
        aX, aY = self.actualPos
        self.rect = pygame.Rect(aX, aY, CELL, CELL)
        
        self.targetPos = self.actualPos
        self.direction = (0,0)
        self.isMoving = False 
        
    def set_direction(self, direction: str):
       direction = direction.upper()
       if direction == "UP":
           self.direction = (-1, 0)
       if direction == "DOWN":
           self.direction = (1, 0)
       if direction == "LEFT":
           self.direction = (0, -1)
       if direction == "RIGHT":
           self.direction = (0, 1)
        
    def draw(self, screen):
        color = None
        if self.isMoving:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        pygame.draw.rect(screen, color, self.rect)
        
     
    def move(self):
        
        if self.isMoving is False:
            if self.direction == (0,0):
                # this condition is basically saying, dont do anything if the player hasn't done anything. 
                # or if the player ran into a wall (to be done later])
                return
              
            #pick a targetpos and set it up
            
           
            self.targetPos = (self.actualPos[0]+self.direction[1]*CELL,  self.actualPos[1]+ self.direction[0]*CELL)
            
            nextY, nextX = self.pos[0]+self.direction[0], self.pos[1]+self.direction[1]
            
            if self.board[nextY][nextX] == 1:
                self.direction = (0,0)
                return
            
            
            
            self.isMoving = True
        else:
             
            x0, y0 = self.rect.x, self.rect.y
            x1, y1 = self.targetPos
            
            deltaX, deltaY = x1-x0, y1-y0
            
            
            dist = ((y1-y0)**2 + (x1-x0)**2)**0.5
            deltaX, deltaY = deltaX/dist, deltaY/dist 
            
            # print(f"if {dist} <= {self.speed}:  {dist <= self.speed:} | pos: {self.actualPos} | target: {self.targetPos} ") 
            if dist <= self.speed:
                self.actualPos = self.targetPos
                self.pos = (self.targetPos[1]//CELL, self.targetPos[0]//CELL)

                self.rect.topleft = self.targetPos
                
                
                self.isMoving = False
                return
            

            self.rect.move_ip(
                deltaX*self.speed, deltaY*self.speed
            )
     
                    
                    
             
                
                
                
                 
        
        
        
player = Player(
    size=25,
    pos=(4,1),
    board=board
)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill((255,255,255)) 
    for y in range(len(board)):
        for x in range(len(board[0])):
            value = board[y][x]
            if value == 1:
                pygame.draw.rect(screen, (100,100,100), pygame.Rect(x*CELL, y*CELL, CELL, CELL )) 

    player.draw(screen=screen)  
    pygame.draw.circle(screen, (100,0,0), center=player.targetPos, radius=5)
    pygame.draw.line(screen, (0, 0, 200), start_pos=(player.rect.x, player.rect.y), end_pos=player.targetPos, width=2)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        player.set_direction("UP")
    if keys[pygame.K_DOWN]:
        player.set_direction("DOWN")
    if keys[pygame.K_LEFT]:
        player.set_direction("LEFT")
    if keys[pygame.K_RIGHT]:
        player.set_direction("RIGHT")
    # print(player.direction) 
    
    player.move()
    pygame.display.flip() 
    clock.tick(60)


