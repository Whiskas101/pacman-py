import pygame


class Player:
    def __init__(self, speed, dim=(25,25), pos = (200,200)):
        # not sure of what attributes to even give this
        self.speed = speed 
        self.dim = dim # height and width 
        self.pos = pos # starting position
        
        self.rect = pygame.Rect(self.pos, self.dim) # Pygame rect

        print(f"Created Player: {self.dim, self.pos}") 


    def move(self, direction):
        # currently not accounting for the physics, might add it later [time.deltaTime]
        print("called ", direction) 
        match direction.upper():
            case "UP":
                self.rect.move_ip(0, -self.speed*0.1) # move up
            case "DOWN":
                self.rect.move_ip(0, +self.speed*0.1) # move up

            case "LEFT":
                self.rect.move_ip(-self.speed*0.1, 0) # move up

            case "RIGHT":
                self.rect.move_ip(+self.speed*0.1, 0) # move up
    

    # having the draw method here is bad coupling, but composition would be harder to explain

    def draw(self, screen):
        pygame.draw.rect(screen, (10,200,10), self.rect)

    
    def collidelistall(self, *args, **kwargs):
        return self.rect.collidelistall(*args, **kwargs)
    










