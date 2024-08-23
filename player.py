import pygame

# For loading graphical data
from spriteSheets import SpriteSheet
from ImageLoc import some_dict

GRID_SIZE = 50 

class Player:
    def __init__(self, speed,grid, dim=(25,25), pos = (1,1), color=(20,100,125), graphicsPath=None):

        # not sure of what attributes to even give this
        self.speed = speed 
        
        self.dim = dim # height and width of the player

        self.pos = pos # starting position, this is in terms of the Grid Indices, not pixel values

        self.actualPos = (pos[0]*dim[0], pos[1]*dim[1]) # in terms of actual pixel values
        
        self.targetPos = self.actualPos # for initialisation

        self.color = color # RGB format

        # this is the rect for movement smoothing
        self.rect = pygame.Rect(self.actualPos, self.dim) # Pygame rect
        self.direction = (0,0)# player is stationary by default
       
        # To keep track of when the player is actually in the
        # state of moving to next grid, but not quite there yet
        self.isMoving = False;
        
        # To know which moves are illegal.
        self.grid = grid
        

        # ANIMATION STUFF
        # Location of where the animation frames are stored.
        self.graphicsPath = graphicsPath
        
        self.animations = self.loadGraphics()
        self.animation_cooldown = 100

        
        # To decide which animation frame to show
        self.frame_step = 0
        self.animationSpeed = 1

        # To know how long the current frame has been on the screen for.
        self.last_time = pygame.time.get_ticks()
        
        print(f"Created Player: {self.dim, self.pos}") 


    def set_direction(self, direction):
        match direction.upper():
            case "UP":
                self.direction = ( 0,-1 )
            case "DOWN":
                self.direction = ( 0, 1 )

            case "LEFT":
                self.direction = (-1, 0 )
            case "RIGHT":
                self.direction = ( 1, 0 )

    
    def draw(self, screen):
        # if no asset data is provided, default back to a square  
        #pygame.draw.rect(screen, self.color, self.rect) 
        #return
        if self.graphicsPath == None:
            pygame.draw.rect(screen, self.color, self.rect) 
            return

            
        # NEW DRAW 
        Map = {
            (0,0):0,
            (-1,0):0,
            (1,0):1,
            (0,1): 3,
            (0, -1):2
        }

        action = Map.get(self.direction)
        #action = self.direction[0] + self.direction[1] + 2

        print(self.direction, action) 

        self.current_time = pygame.time.get_ticks()
        if self.current_time-self.last_time>=self.animation_cooldown:
            self.last_time=self.current_time
            self.frame_step+=1

            # redundant line, can just use % operator : [ % len(animations) ]
            
            if self.frame_step>=len(self.animations[action]):
               self.frame_step=0
        
        #pos=self.animations[action][self.frame_step].get_rect()
        print("Attempting", action, self.frame_step)
        screen.blit(self.animations[action][self.frame_step], self.rect.topleft) 
        


    def move(self):
        
        if self.isMoving == False:
            if self.direction == (0,0): # for the initial condition, theres def a better approach to handling the default
                return

            # THIS IS WHERE I'M PREVENTING THE PLAYER FROM MOVING INTO A WALL!
            # check if the current pos + direction == wall

            # In terms of the grid, first value, refers to the Y axis,
            # second value for the X axis, this is opposite to the convention followed
            # in pygame (which is absurd in it's own right)

            upcomingY = self.pos[0] + self.direction[0]
            upcomingX = self.pos[1] + self.direction[1]
            
            if self.grid[upcomingX][upcomingY] == 1:
                self.direction = (0,0)
                return


            self.targetPos = (self.rect.x + (GRID_SIZE * self.direction[0]), self.rect.y + (GRID_SIZE * self.direction[1]))
            self.isMoving = True
            
            # go to next frame.
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
   

    def loadGraphics(self):
        if self.graphicsPath == None:
            return []


        # Only try to load the graphics if the path was actually mentioned.      
        animations = []
        print(some_dict)
        for key, animationPaths in some_dict.items():   
            print("ANim path:", animationPaths)
            animation = []
            for image in animationPaths.values():
                image = pygame.image.load(f"{self.graphicsPath}/{key}/{image}").convert_alpha() 
                print(image)
                

                
                frame = SpriteSheet().get_image(image, self.dim[0], self.dim[1], (0,0))
                animation.append(frame)
                
                # Collection of frames, the animation is added as an array.
            animations.append(animation)
        
        return animations


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
            Graphical Data
            --------------
            Location: {self.graphicsPath}
            num of unique animations: {len(self.animations)}
            animations: {self.animations}
            frame: {self.frame_step}
        -------------------------------------
        
        """










