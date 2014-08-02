'''Handles all of the graphics in the battle screen.'''
import pygame
import required_lists
import images
import battle_functions

screen = images.SCREEN

game_state = "first select"

def render_background():
    screen.fill(images.WHITE)
    screen.blit(images.GRASS_BATTLE, images.TOPLEFT)

def reset_labels():
    '''Resets the text in the available boxes.'''
    required_lists.box_data = ["Fight", "Bag", "Pokemon", "Run", "", "", "", "", "", ""]
    required_lists.box5data = "What would you like to do?"

def print_ask_for_space():
    '''Tell the user to push a button to continue.'''
    required_lists.box5data = "Press any key to continue."

def define_text_boxes():
    '''Renders the text that goes in each box, and defines a rectangle around each block of text.'''
    box1_text_image = images.render_text(required_lists.box_data[0])
    box2_text_image = images.render_text(required_lists.box_data[1])
    box3_text_image = images.render_text(required_lists.box_data[2])
    box4_text_image = images.render_text(required_lists.box_data[3])

    box1_text_rect = box1_text_image.get_rect()
    box2_text_rect = box2_text_image.get_rect()
    box3_text_rect = box3_text_image.get_rect()
    box4_text_rect = box4_text_image.get_rect()

    boxa_text_image = images.render_text(required_lists.box_data[4])
    boxb_text_image = images.render_text(required_lists.box_data[5])
    boxc_text_image = images.render_text(required_lists.box_data[6])
    boxd_text_image = images.render_text(required_lists.box_data[7])
    boxe_text_image = images.render_text(required_lists.box_data[8])
    boxf_text_image = images.render_text(required_lists.box_data[9])

    boxa_text_rect = boxa_text_image.get_rect()
    boxb_text_rect = boxb_text_image.get_rect()
    boxc_text_rect = boxc_text_image.get_rect()
    boxd_text_rect = boxd_text_image.get_rect()
    boxe_text_rect = boxe_text_image.get_rect()
    boxf_text_rect = boxf_text_image.get_rect()

    text_image_list = [box1_text_image, box2_text_image, box3_text_image, box4_text_image, boxa_text_image, boxb_text_image, boxc_text_image, boxd_text_image, boxe_text_image, boxf_text_image]
    text_box_list = [box1_text_rect, box2_text_rect, box3_text_rect, box4_text_rect, boxa_text_rect, boxb_text_rect, boxc_text_rect, boxd_text_rect, boxe_text_rect, boxf_text_rect]

    return [text_image_list, text_box_list]

def render_4_boxes():
    '''Blit the 4 boxes, with corrosponding text, to the screen.'''
    text_list = define_text_boxes()

    box1 = screen.blit(required_lists.box_colors[0], images.BOX1POS)
    text_list[1][0].center = box1.center
    screen.blit(text_list[0][0], text_list[1][0])

    box2 = screen.blit(required_lists.box_colors[1], images.BOX2POS)
    text_list[1][1].center = box2.center
    screen.blit(text_list[0][1], text_list[1][1])

    box3 = screen.blit(required_lists.box_colors[2], images.BOX3POS)
    text_list[1][2].center = box3.center
    screen.blit(text_list[0][2], text_list[1][2])

    box4 = screen.blit(required_lists.box_colors[3], images.BOX4POS)
    text_list[1][3].center = box4.center
    screen.blit(text_list[0][3], text_list[1][3])

    required_lists.four_boxes = [box1, box2, box3, box4]

def render_6_boxes():
    '''Blit the 6 boxes, with corrosponding pokemon, to the screen.'''
    text_list = define_text_boxes()

    boxa = screen.blit(images.POKEMONBOX, images.BOXAPOS)
    text_list[1][4].center = boxa.center
    screen.blit(text_list[0][4], text_list[1][4])

    boxb = screen.blit(images.POKEMONBOX, images.BOXBPOS)
    text_list[1][5].center = boxb.center
    screen.blit(text_list[0][5], text_list[1][5])

    boxc = screen.blit(images.POKEMONBOX, images.BOXCPOS)
    text_list[1][6].center = boxc.center
    screen.blit(text_list[0][6], text_list[1][6])

    boxd = screen.blit(images.POKEMONBOX, images.BOXDPOS)
    text_list[1][7].center = boxd.center
    screen.blit(text_list[0][7], text_list[1][7])

    boxe = screen.blit(images.POKEMONBOX, images.BOXEPOS)
    text_list[1][8].center = boxe.center
    screen.blit(text_list[0][8], text_list[1][8])

    boxf = screen.blit(images.POKEMONBOX, images.BOXFPOS)
    text_list[1][9].center = boxf.center
    screen.blit(text_list[0][9], text_list[1][9])

    required_lists.six_boxes = [boxa, boxb, boxc, boxd, boxe, boxf]


def render_box_5():
    '''Blits the info box to the screen, along with its corrosponding text.'''
    box5_text_image = images.render_text(required_lists.box5data, images.WHITE)
    box5_text_rect = box5_text_image.get_rect()
    box5 = screen.blit(images.TEXTBOX, images.BOX5POS)
    box5_text_rect.left = box5.left + 15
    box5_text_rect.top = box5.top + 15
    screen.blit(box5_text_image, box5_text_rect)

def update_box_5(player_pokemon, enemy_pokemon):
    '''Updates the text in box5 alongisde the hp of the pokemon and the status images'''
    if len(required_lists.to_damage) != len(required_lists.to_print):
        del required_lists.to_damage[0] #compensates for a random extra "NULL" that came from somewhere...
    print required_lists.to_print
    print required_lists.to_damage
    print required_lists.to_damage_count
    if len(required_lists.to_print_immediate) != 0:
        required_lists.box5data = required_lists.to_print_immediate[0]
    else:
        required_lists.box5data = required_lists.to_print[0]

    if required_lists.to_damage[0] == "NULL":
        del required_lists.to_damage[0]
    elif required_lists.to_damage[0] == "player":
        player_pokemon.hp -= required_lists.to_damage_count[0]
        del required_lists.to_damage[0]
        del required_lists.to_damage_count[0]
    else:
        enemy_pokemon.hp -= required_lists.to_damage_count[0]
        del required_lists.to_damage[0]
        del required_lists.to_damage_count[0]
    del required_lists.to_print[0]
    battle_functions.check_enemy_health(player_pokemon, enemy_pokemon)
    battle_functions.check_player_health(player_pokemon)
    if len(required_lists.to_print) == 0:
        required_lists.box5data = "What would you like to do?"

def render_correct_boxes():
    '''Blits either 4 or 6 boxes depending on the game state, always blits box5.'''
    render_box_5()
    if game_state != "pokemon list":
        render_4_boxes()
    else:
        render_6_boxes()

def render_hp_boxes():
    '''Blits the hp boxes to the screen.'''
    screen.blit(images.PLAYER_HP_BOX, images.PLAYERHPPOS)
    screen.blit(images.ENEMY_HP_BOX, images.ENEMYHPPOS)

def render_player_hp(pokemon):
    '''Blits the graphical representation of the player's HP to the screen.'''
    hp_percent = float(pokemon.hp)/float(pokemon.hp_full)
    hp_to_render = hp_percent * 84 #hp bar is 84px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (275+hp, 174))

def render_enemy_hp(pokemon):
    '''Blits the graphical representation of the enemy's HP to the screen.'''
    hp_percent = float(pokemon.hp)/float(pokemon.hp_full)
    hp_to_render = hp_percent * 86 #hp bar is 86px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (74+hp, 40))

def select_box(move):
    '''Selects which color box to blit to make it corrospond to that move's type.'''
    if move.move_type == "normal":
        box = images.NORMAL_BOX
    elif move.move_type == "fighting":
        box = images.FIGHTING_BOX
    elif move.move_type == "flying":
        box = images.FLYING_BOX
    elif move.move_type == "poison":
        box = images.POISON_BOX
    elif move.move_type == "ground":
        box = images.GROUND_BOX
    elif move.move_type == "rock":
        box = images.ROCK_BOX
    elif move.move_type == "bug":
        box = images.BUG_BOX
    elif move.move_type == "ghost":
        box = images.GHOST_BOX
    elif move.move_type == "steel":
        box = images.STEEL_BOX
    elif move.move_type == "fire":
        box = images.FIRE_BOX
    elif move.move_type == "water":
        box = images.WATER_BOX
    elif move.move_type == "grass":
        box = images.GRASS_BOX
    elif move.move_type == "electric":
        box = images.ELECTRIC_BOX
    elif move.move_type == "psychic":
        box = images.PSYCHIC_BOX
    elif move.move_type == "ice":
        box = images.ICE_BOX
    elif move.move_type == "dragon":
        box = images.DRAGON_BOX
    elif move.move_type == "dark":
        box = images.DARK_BOX
    elif move.move_type == "fairy":
        box = images.FAIRY_BOX
    else:
        box = images.TEXTBOX
    return box


