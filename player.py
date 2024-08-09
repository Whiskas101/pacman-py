import pygame
GRID_SIZE = 75

class Player:
    def __init__(self, speed, dim=(25,25), pos = (1,1)):
        # not sure of what attributes to even give this
        self.speed = speed 
        self.dim = dim # height and width 
        self.pos = pos # starting position, this is in terms of the Grid Indices

        self.actualPos = (pos[0]*dim[0], pos[0]*dim[0]) # in terms of actual pixel values
        
        self.targetPos = self.actualPos # for initialisation

        self.color = (20,100,125) # RGB format

        # this is the rect for movement smoothing
        self.rect = pygame.Rect(self.actualPos, self.dim) # Pygame rect
        self.direction = (0,0)# player is stationary by default
       
        # To keep track of when the player is actually in the
        # state of moving to next grid, but not quite there yet
        #
        self.isMoving = False;
        print(f"Created Player: {self.dim, self.pos}") 


    def set_direction(self, direction):
        match direction.upper():
            case "UP":
                self.direction = (0,-1)
            case "DOWN":
                self.direction = (0, 1)

            case "LEFT":
                self.direction = (-1, 0)
            case "RIGHT":
                self.direction = (1, 0)

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect) 
    
    def move(self):
        
        if self.isMoving == False:
            if self.direction == (0,0): # for the initial condition, theres def a better approach to handling the default
                return
            self.targetPos = (self.rect.x + (GRID_SIZE * self.direction[0]), self.rect.y + (GRID_SIZE * self.direction[1]))
            self.isMoving = True
            return
        else:
            #if the player is moving, handle the offset and stop/update condition
            # Applying linear interpolation for the smooth movement.
            
            deltaX = self.targetPos[0] - self.rect.x
            deltaY = self.targetPos[1] - self.rect.y

            distance = ((deltaX**2 + deltaY**2))**0.5
            moveDistance = min(distance, self.speed)
            print("Distance, moveDistance", distance, moveDistance)
            xMove = deltaX / distance * moveDistance
            yMove = deltaY / distance * moveDistance
            
            # if the player reaches close enough to the target, just snap its position to the target
            # set moving to false, so a new target can be calculated
            if distance <= self.speed:
                self.rect.topleft = self.targetPos
                self.pos = (self.targetPos[0] // GRID_SIZE, self.targetPos[1]//GRID_SIZE)
                
                self.isMoving = False
                return
            
            self.rect.move_ip(xMove, yMove)



    # this method wont be needed in terms of collisions with the walls,
    # only for possibly detecting when the player gets a point? or gets killed?

    def collidelistall(self, *args, **kwargs):
        return self.rect.collidelistall(*args, **kwargs)
   
    def __repr__(self):
        # Clears the console and prints some debug information
        print("\033[2J\033[H", end="")
        return f"""
        -------------------------------------
            Grid Size: {GRID_SIZE},
            Direction : {self.direction},
            Raw Position: {self.rect.topleft},
            Grid Position: {self.pos},
            Target Position: {self.targetPos},
            State: {self.isMoving}
            Dist: {self.targetPos[0] - self.rect.x, self.targetPos[1] - self.rect.y}
        -------------------------------------
        
        """










