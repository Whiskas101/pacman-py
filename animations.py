import pygame as pg
import spriteSheets 
from ImageLoc import some_dict

pg.init()

WIDTH=500
HEIGHT=500
screen=pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption('Sprite Sheet')


ss=spriteSheets.SpriteSheet()

animations=[]

for key ,value in some_dict.items(): #use loop to get the images from the folders
    temp=[]
    for image in value.values():
        some_image=pg.image.load(f"C:/Users/lenovo/OneDrive/Desktop/Coding/{key}/{image}").convert_alpha()
        frame=ss.get_image(some_image, 20, 20, 2, (0,0))
        temp.append(frame)
    animations.append(temp)

animation_cooldown=100 #cooldown time for changing animation
last_time=pg.time.get_ticks() #get the time when the game starts

frame_step=0
action=0
speed=1


run=True
while run:
    screen.fill((0,0,0))
    
    current_time=pg.time.get_ticks()
    if current_time-last_time>=animation_cooldown:
        last_time=current_time
        frame_step+=1
        if frame_step>=len(animations[action]):
            frame_step=0
    
    pos=animations[action][frame_step].get_rect()
    screen.blit(animations[action][frame_step], (HEIGHT//2, WIDTH//2))

    pg.display.update()

    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False

        if event.type==pg.KEYDOWN: #use the keys to chnage the direction of the frames 
            if event.key==pg.K_LEFT:
                action=0
    
            if event.key==pg.K_RIGHT:
                action=1

            if event.key==pg.K_UP:
                action=2

            if event.key==pg.K_DOWN:
                action=3

    
    pg.display.update()
pg.quit()