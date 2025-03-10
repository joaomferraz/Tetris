import pygame, sys
from grid import Grid
from blocks import *

pygame.init()
purple = (87, 9, 117)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris com Python")

clock = pygame.time.Clock()

game_grid = Grid()

block = IBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Drawing the display
    screen.fill(purple)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)