import pygame

class GridObject:
    
    def __init__(self,dim=(10,10), pos=(100,100)):
        self.pos = pos
        self.dim = dim

        self.rect = pygame.Rect(pos, dim)
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, (100,100,10), self.rect)
