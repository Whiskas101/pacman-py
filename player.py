import pygame


class Player:
    def __init__(self, speed, dim=[25,25], pos = [200,200]):
        # not sure of what attributes to even give this
        self.speed = speed 
        self.dim = dim # height and width 
        self.pos = pos # starting position
        print(f"Created Player: {self.dim, self.pos}") 


    def move(self, direction):
        # currently not accounting for the physics, might add it later [time.deltaTime]
        print("called ", direction) 
        match direction.upper():
            case "UP":
                self.pos[1] -= self.speed * 0.1 # move up
            case "DOWN":
                self.pos[1] += self.speed * 0.1

            case "LEFT":
                self.pos[0] -= self.speed * 0.1

            case "RIGHT":
                self.pos[0] += self.speed * 0.1
    

    # having the draw method here is bad coupling, but composition would be harder to explain

    def draw(self, screen):
        pygame.draw.rect(screen, (10,200,10), (self.pos[0], self.pos[1],
                         self.dim[0], self.dim[1]))


    










