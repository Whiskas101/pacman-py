import pygame as pg 

pg.init()

HEIGHT=500
WIDTH=500
screen=pg.display.set_mode((WIDTH, HEIGHT))



class StartEndScreen:
    def __init__(self, screen, text, font, text_col): #initialize the start screen like text , font, color etc
        self.screen=screen 
        self.text=text
        self.font=font
        self.text_col=text_col
        self.text=font.render(self.text, True, text_col)
        self.text_rect = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.alpha=255
        self.fade_out=True
        self.fade_speed=0.1
        
    def fade(self): #fades our text

        if self.fade_out: 
            self.alpha-=self.fade_speed
            if self.alpha<=0:
                self.alpha=0
                self.fade_out=False
            
        if not self.fade_out:
            self.alpha+=self.fade_speed
            if self.alpha>=255:
                self.alpha=255
                self.fade_out=True
        
        self.text.set_alpha(self.alpha)
        screen.blit(self.text, self.text_rect)

    def wait(self):
        run = True 
        while run:
            screen.fill((255,100,10))
            self.fade()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN: #checking if 'Space' key is pressed to proceed to the game
                    if event.key==pg.K_SPACE:
                        run = False 
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()


