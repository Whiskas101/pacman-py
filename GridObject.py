import pygame

class GridObject:
    
    def __init__(self,dim=(10,10), pos=(100,100), color=(0,0,255)):
        self.pos = pos
        self.dim = dim
        self.color = color
        self.rect = pygame.Rect(pos, dim)
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
