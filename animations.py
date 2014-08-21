import pyganim
import pygame
from PIL import Image, ImageSequence
# bulbasaur_front = pyganim.PygAnimation([
#    ('sprites/bulbasaur/front0.gif', 0.1),
#    ('sprites/bulbasaur/front1.gif', 0.1),
#    ('sprites/bulbasaur/front2.gif', 0.1),
#    ('sprites/bulbasaur/front3.gif', 0.1),
#    ('sprites/bulbasaur/front4.gif', 0.1),
#    ('sprites/bulbasaur/front5.gif', 0.1),
#    ('sprites/bulbasaur/front6.gif', 0.1),
#    ('sprites/bulbasaur/front7.gif', 0.1),
#    ('sprites/bulbasaur/front8.gif', 0.1),
#    ('sprites/bulbasaur/front9.gif', 0.1),
#    ('sprites/bulbasaur/front10.gif', 0.1),
# ])

bulbasaur_front_gif = Image.open('sprites/bulbasaur.gif')
sprite_list = []

for frame in ImageSequence.Iterator(bulbasaur_front_gif):
    frame = frame.convert("RGBA")
    mode = frame.mode
    size = frame.size
    data = frame.tobytes()

    print(mode, size)

    sprite = pygame.image.frombuffer(data, size, mode)
    test_image = sprite
    sprite_list.append((sprite, 0.1))

bulbasaur_front = pyganim.PygAnimation(sprite_list)

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