"""Import a gif and save its frame data as a blitable object."""
import pyganim
import pygame
from PIL import Image, ImageSequence

def import_gif(gif):
    PIL_gif = Image.open(gif)
    sprite_list = []

    for frame in ImageSequence.Iterator(PIL_gif):
        frame = frame.convert("RGBA")
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()

        sprite = pygame.image.frombuffer(data, size, mode)
        sprite_list.append((sprite, 0.1))

    return pyganim.PygAnimation(sprite_list)


bulbasaur_front = import_gif('sprites/pokemon/bulbasaur front.gif')
bulbasaur_back = import_gif('sprites/pokemon/bulbasaur back.gif')

ivysaur_front = import_gif("sprites/pokemon/ivysaur front.gif")
ivysaur_back = import_gif("sprites/pokemon/ivysaur back.gif")