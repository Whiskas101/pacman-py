
import pygame
from player import Player


pygame.init()

screen = pygame.display.set_mode((1280, 720))
 
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
running = True

p = Player(speed=10, grid=[], graphicsPath="pacman-art")
print(p.animations)
print(len(p.animations))




