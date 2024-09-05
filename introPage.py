import pygame as pg 

pg.init()

HEIGHT=500
WIDTH=500
screen=pg.display.set_mode((WIDTH, HEIGHT))

font=pg.font.SysFont("arialBlack", 30)
text_col=(255,255,255)

text=["Press Space to Start", "Game Over"] #holds the text for start and end screen

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


start_end_screen=StartEndScreen(screen, text[0], font, text_col) #initialize the start screen
start_end_screen_1=None #initialize the object for end screen
endCondition=False #initialize the end condition
startPage=True #initialize the start page
run=True

while run:
    screen.fill((255,100,10))
    if startPage:
        start_end_screen.fade()

    if endCondition: #checking end condition and dsiplaying end screen
        if start_end_screen_1 is None:
            start_end_screen_1=StartEndScreen(screen, text[1], font, text_col)
        start_end_screen_1.fade()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN: #checking if 'Space' key is pressed to proceed to the game
            if event.key==pg.K_SPACE:
                startPage=False #start page is false as key is pressed
                endCondition=True
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    show_text=False
pg.quit()