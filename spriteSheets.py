import pygame as pg


class SpriteSheet:
    
    def get_image(self, image, width, height, pos, scale = 0.62): #declare the images width height scale and position 
        # The actual image may be too big or too small for the grid, therefore
        # increase the size of the image to fit into given height and width

        self.image = pg.transform.scale(image, (width*scale, height*scale)) #change the images scale

        # If the items aren't supposed to occupy the entire grid space, must shrink them, and move them
        # to the center of the grid cell, otherwise it would be stuck in the corner.
        offsetX, offsetY = (width - width*scale)/2, (height-height*scale)/2
        
        # Adding transparency to the asset that is being loaded.
        image = pg.Surface((width, height)).convert_alpha() 
        image.fill((0,0,0,0))
        image.blit(self.image, (offsetX,offsetY)) #blit out image on the image screen
        #image.set_colorkey((255,255,255)) #change the background of the image 

        return image 
    
