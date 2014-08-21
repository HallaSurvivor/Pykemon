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


bulbasaur_front = import_gif('sprites/bulbasaur.gif')

bulbasaur_back = pyganim.PygAnimation([
    ('sprites/bulbasaur/back0.gif', 0.1),
    ('sprites/bulbasaur/back1.gif', 0.1),
    ('sprites/bulbasaur/back2.gif', 0.1),
    ('sprites/bulbasaur/back3.gif', 0.1),
    ('sprites/bulbasaur/back4.gif', 0.1),
    ('sprites/bulbasaur/back5.gif', 0.1),
    ('sprites/bulbasaur/back6.gif', 0.1),
    ('sprites/bulbasaur/back7.gif', 0.1),
    ('sprites/bulbasaur/back8.gif', 0.1),
    ('sprites/bulbasaur/back9.gif', 0.1),
    ('sprites/bulbasaur/back10.gif', 0.1),
])