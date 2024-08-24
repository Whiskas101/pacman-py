import pygame

class GridObject:
    
    def __init__(self,pos, size, color=(0,0,255), board=None):
        self.pos = pos
        self.dim = (size, size) 
        self.actualPos = (self.dim[0]*pos[0],self.dim[1]*pos[1]) 
        self.color = color
        self.rect = pygame.Rect(self.actualPos, self.dim)

        self.board = board 
        
    
    def draw(self, screen):
        # if its not a consumable object, just draw a simple colored box  
        x, y = self.pos

        if self.board[y][x] == 1:
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.board[y][x] == 0:

            #Scale factor, so the tiny consumable is relative to the size of the grid cell.
            scale = 0.1
            small_box_width = self.rect.width*scale
            small_box_height = self.rect.height*scale

            # Draw small tiny box 
            small_box = pygame.Rect(
                self.rect.x + (self.rect.width - small_box_width)//2,
                self.rect.y + (self.rect.height - small_box_height)//2,
                small_box_width,
                small_box_height
            )

            pygame.draw.rect(screen, self.color, small_box)
