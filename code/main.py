import pygame
from settings import *
from editor import Editor

pygame.init()
pygame.display.set_caption('Pathfinding')
screen = pygame.display.set_mode((WIDTH, HEIGHT ))
clock = pygame.time.Clock()

editor = Editor()

while True:
    screen.fill('black')
    editor.run()
    pygame.display.update()
    clock.tick(60)