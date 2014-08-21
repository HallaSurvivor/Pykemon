'''Import all the sprites and store them as public variables.'''
#Thanks to pokemondb for the majority of these sprites. :)
import pygame
import os

def load(image_name):
    return pygame.image.load(os.path.join("sprites", image_name))

pygame.init()

#pokemon
BULBASAUR_SMALL = load("bulbasaur_small.png")

IVYSAUR_BACK = load("blastoise_back.png")
IVYSAUR_FRONT = load("blastoise_front.png")
IVYSAUR_SMALL = load("ivysaur_small.png")

MUDKIP_FRONT = load("mudkip_front.png")
MUDKIP_BACK = load("mudkip_back.png")

#backgrounds
GRASS_BATTLE = load("grass_battle.png")

#boxes
BOX = load("box.png")
SQUAREBOX = load("squarebox.png")
TEXTBOX = load("text_box.png")
POKEMONBOX = load("pokemon_box.png")
FAINTEDPOKEMONBOX = load("fainted_pokemon_box.png")
BACK = load("back.png")


NORMAL_BOX = load("box_normal.png")
FIGHTING_BOX = load("box_fighting.png")
FLYING_BOX = load("box_flying.png")
POISON_BOX = load("box_poison.png")
GROUND_BOX = load("box_ground.png")
ROCK_BOX = load("box_rock.png")
BUG_BOX = load("box_bug.png")
GHOST_BOX = load("box_ghost.png")
STEEL_BOX = load("box_steel.png")
FIRE_BOX = load("box_fire.png")
WATER_BOX = load("box_water.png")
GRASS_BOX = load("box_grass.png")
ELECTRIC_BOX = load("box_electric.png")
PSYCHIC_BOX = load("box_psychic.png")
ICE_BOX = load("box_ice.png")
DRAGON_BOX = load("box_dragon.png")
DARK_BOX = load("box_dark.png")
FAIRY_BOX = load("box_fairy.png")

PLAYER_HP_BOX = load("player_hp.png")
ENEMY_HP_BOX = load("enemy_hp.png")
HP_GREEN = load("hp_green.png")
HP_YELLOW = load("hp_yellow.png")
EXP_BAR = load("exp_bar.png")

BRN = load("brn.png")
PAR = load("par.png")
FRZ = load("frz.png")
PSN = load("psn.png")
SLP = load("slp.png")
FNT = load("fnt.png")

MALE = load("male.png")
FEMALE = load("female.png")
GENDERLESS = load("genderless.png")
genders = {"male":MALE, "female":FEMALE, "genderless":GENDERLESS}


status_icons = [BRN, FRZ, PAR, PSN, PSN, SLP]

box_1_var = BOX
box_2_var = BOX
box_3_var = BOX
box_4_var = BOX

#constants (W, H)
SCREENSIZE = (560, 330)
BATTLESIZE = (374, 210)
SPRITESIZE = (110, 110)

BOX1POS = (383, 7)
BOX2POS = (383, 89)
BOX3POS = (383, 171)
BOX4POS = (383, 253)
BOX5POS = (4, 214)

PP1POS = (469, 60)
PP2POS = (469, 142)
PP3POS = (469, 224)
PP4POS = (469, 306)

PP_POS_LIST = [PP1POS, PP2POS, PP3POS, PP4POS]

BACKBUTTONPOS = (346, 292)

#PARTYSPRITESPOS = (7, 292)

BOXAPOS = (383, 7)
BOXBPOS = (383, 60)
BOXCPOS = (383, 113)
BOXDPOS = (383, 166)
BOXEPOS = (383, 219)
BOXFPOS = (383, 272)

PLAYERHPPOS = (192, 145)
ENEMYHPPOS = (5, 10)

HPTEXTPOS = (300, 185)
FULLHPTEXTPOS = (325, 185)

PLAYERNAMEPOS = (220, 155)
ENEMYNAMEPOS = (20, 20)

PLAYER_STATUS_POS = (216, 170)
ENEMY_STATUS_POS = (14, 31)

TOPLEFT = (0, 0)
ENEMYSPRITEPOS = (235, 70)
PLAYERSPRITEPOS = (40, 130)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FONTSIZE1 = 60

SCREEN = pygame.display.set_mode(SCREENSIZE)

#Fonts
arial24 = pygame.font.SysFont(None, 24)
arial17 = pygame.font.SysFont(None, 17)

def render_text(text, color = BLACK):
    return arial24.render(text, 1, color)

def render_small_text(text, color = BLACK):
    return arial17.render(text, 1, color)