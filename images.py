"""Import all the sprites and store them as public variables."""
#Thanks to pokemondb for the majority of these sprites. :)
import pygame
import os

def load(image_name, subfolder = "NULL"):
    if subfolder == "NULL":
        return pygame.image.load(os.path.join("sprites", image_name))
    else:
        return pygame.image.load(os.path.join("sprites", subfolder, image_name))

pygame.init()

#pokemon
BULBASAUR_SMALL = load("bulbasaur_small.png", "pokemon")
IVYSAUR_SMALL = load("ivysaur_small.png", "pokemon")


#backgrounds
GRASS_BATTLE = load("grass_battle.png", "battle backgrounds")

#boxes
BOX = load("box.png", "move boxes")
SQUAREBOX = load("squarebox.png", "pokemon boxes")
TEXTBOX = load("text_box.png", "misc")
POKEMONBOX = load("pokemon_box.png", "pokemon boxes")
FAINTEDPOKEMONBOX = load("fainted_pokemon_box.png", "pokemon boxes")
BACK = load("back.png", "misc")


NORMAL_BOX = load("box_normal.png", "move boxes")
FIGHTING_BOX = load("box_fighting.png", "move boxes")
FLYING_BOX = load("box_flying.png", "move boxes")
POISON_BOX = load("box_poison.png", "move boxes")
GROUND_BOX = load("box_ground.png", "move boxes")
ROCK_BOX = load("box_rock.png", "move boxes")
BUG_BOX = load("box_bug.png", "move boxes")
GHOST_BOX = load("box_ghost.png", "move boxes")
STEEL_BOX = load("box_steel.png", "move boxes")
FIRE_BOX = load("box_fire.png", "move boxes")
WATER_BOX = load("box_water.png", "move boxes")
GRASS_BOX = load("box_grass.png", "move boxes")
ELECTRIC_BOX = load("box_electric.png", "move boxes")
PSYCHIC_BOX = load("box_psychic.png", "move boxes")
ICE_BOX = load("box_ice.png", "move boxes")
DRAGON_BOX = load("box_dragon.png", "move boxes")
DARK_BOX = load("box_dark.png", "move boxes")
FAIRY_BOX = load("box_fairy.png", "move boxes")

PLAYER_HP_BOX = load("player_hp.png", "pokemon boxes")
ENEMY_HP_BOX = load("enemy_hp.png", "pokemon boxes")
HP_GREEN = load("hp_green.png", "misc")
HP_YELLOW = load("hp_yellow.png", "misc")
EXP_BAR = load("exp_bar.png", "misc")

BRN = load("brn.png", "status ailments")
PAR = load("par.png", "status ailments")
FRZ = load("frz.png", "status ailments")
PSN = load("psn.png", "status ailments")
SLP = load("slp.png", "status ailments")
FNT = load("fnt.png", "status ailments")

MALE = load("male.png", "misc")
FEMALE = load("female.png", "misc")
GENDERLESS = load("genderless.png", "misc")
genders = {"male": MALE, "female": FEMALE, "genderless": GENDERLESS}


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