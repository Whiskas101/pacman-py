import pygame as pg


class SpriteSheet:
    
    def get_image(self, image, width, height, pos): #declare the images width height scale and position 

        # Increase the size of the image to fit into given height and width
        self.image = pg.transform.scale(image, (width, height)) #change the images scale

        image = pg.Surface((width, height)).convert_alpha() 
        image.fill((0,0,0,0))
        image.blit(self.image, (0,0)) #blit out image on the image screen
        #image.set_colorkey((255,255,255)) #change the background of the image 
        return image 
    
