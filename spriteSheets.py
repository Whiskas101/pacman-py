import pygame as pg


class SpriteSheet:
    
    def get_image(self, image, width, height, scale , pos): #declare the images width height scale and position 
        self.image=image
        image= pg.Surface((width, height)).convert_alpha() 
        image.blit(self.image, pos) #blit out image on the image screen
        image=pg.transform.scale(image, (width*scale, height*scale)) #change the images scale
        #image.set_colorkey((255,255,255)) #change the background of the image 
        return image 
    
