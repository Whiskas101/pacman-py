import pygame

class GridObject:
    
    def __init__(self,pos, size, color=(0,0,255), board=None):
        self.pos = pos
        self.dim = (size, size) 
        self.actualPos = (self.dim[0]*pos[0],self.dim[1]*pos[1]) 
        self.color = color
        self.rect = pygame.Rect(self.actualPos, self.dim)
        self.size = size
        self.board = board 
        
    
    def draw(self, screen):
        # if its not a consumable object, just draw a simple colored box  
        x, y = self.pos

        if self.board[y][x] == 1:
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.board[y][x] == 0:

            #Scale factor, so the tiny consumable is relative to the size of the grid cell.
            pygame.draw.circle(screen, (255, 0 , 0), (self.actualPos[0]+self.size//2, self.actualPos[1]+self.size//2 ), 3) # Red colored box to act as consumable
