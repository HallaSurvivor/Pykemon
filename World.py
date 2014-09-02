__author__ = 'HallaSurvivor'

from .pokemon_list import *
from .enemies import *
from .battle_mechanic import *
import pygame
from random import randint
import math
import os
from . import sprites


def battle_start(enemy):
    global in_battle
    global player_pokemon
    global enemy_pokemon
    global turn
    in_battle = True
    player_pokemon = player_party[0]
    enemy_pokemon = enemy.party[0]

    if player_pokemon.speed >= enemy_pokemon.speed:
        turn = 1
    else:
        turn = 0


available_pokemon = [Charmander, Bulbasaur, Squirtle]
# PyGame stuff

# Define colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Define positions
BOTTOM_RIGHT = (621, 421)
TOP_RIGHT = (621, 0)
BOTTOM_LEFT = (0, 421)
TOP_LEFT = (0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
# Set the title of the window
pygame.display.set_caption("Pokemon")
# Loop until the user clicks the close button.
done = False
# done = True upon clicking close

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # --- Game logic

        # --- Drawing code
    screen.fill(WHITE)
    screen.blit(sprites.sprites.Bulbasaur_back, BOTTOM_LEFT)
    screen.blit(sprites.sprites.Squirtle_front, TOP_RIGHT)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
