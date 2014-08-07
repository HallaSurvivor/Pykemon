'''Handles all of the graphics in the battle screen.'''
import pygame
import required_lists
import images
import battle_functions

screen = images.SCREEN

game_state = "first select"


def render_background():
    '''Fill the background with white to make sure the battle screen blits on a clean surface.'''
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
    if len(required_lists.to_damage) > len(required_lists.to_print):
        del required_lists.to_damage[0] #compensates for a random extra "NULL" that came from somewhere...

    if len(required_lists.to_print_immediate) != 0:
        required_lists.box5data = required_lists.to_print_immediate[0]
        del required_lists.to_print_immediate[0]
    else:
        required_lists.box5data = required_lists.to_print[0]
        del required_lists.to_print[0]

        if required_lists.to_damage[0] == "NULL":
            del required_lists.to_damage[0]

        elif required_lists.to_damage[0] == "player status":
            blit_player_status_ailment(player_pokemon)
            required_lists.nonvolatile_test_player = True
            del required_lists.to_damage[0]

        elif required_lists.to_damage[0] == "enemy status":
            blit_enemy_status_ailment(enemy_pokemon)
            required_lists.nonvolatile_test_enemy = True
            del required_lists.to_damage[0]

        elif required_lists.to_damage[0] == "player":
            player_pokemon.hp -= required_lists.to_damage_count[0]
            del required_lists.to_damage[0]
            del required_lists.to_damage_count[0]

        else: #enemy
            enemy_pokemon.hp -= required_lists.to_damage_count[0]
            del required_lists.to_damage[0]
            del required_lists.to_damage_count[0]

        battle_functions.check_enemy_health(player_pokemon, enemy_pokemon)
        battle_functions.check_player_health(player_pokemon)

    print required_lists.to_print
    print required_lists.to_damage

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

def blit_exp(player_pokemon):
    '''Blit the correct length experience bar to the screen.'''
    exp_percent = float(player_pokemon.exp) / float(player_pokemon.needed_exp)
    exp_percent = int(exp_percent)
    for exp in range(exp_percent):
        screen.blit(images.EXP_BAR, (300+exp, 200) )

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

def blit_pokemon(player_pokemon, enemy_pokemon):
    '''Blit the actual pokemon sprites in their proper places.'''
    screen.blit(player_pokemon.player_sprite, images.PLAYERSPRITEPOS)
    screen.blit(enemy_pokemon.enemy_sprite, images.ENEMYSPRITEPOS)

def blit_numerical_hp(player_pokemon):
    '''Blit the actual hp value to the screen for the player pokemon.'''
    numerical_hp = images.render_small_text(str(player_pokemon.hp))
    numerical_hp_full = images.render_small_text("/  " + str(player_pokemon.hp_full))
    screen.blit(numerical_hp, images.HPTEXTPOS)
    screen.blit(numerical_hp_full, images.FULLHPTEXTPOS)

def blit_player_name(player_pokemon):
    '''Blit the player's name and gender to the screen.'''
    player_name = images.render_small_text(str(player_pokemon.name))
    player_name_rect = screen.blit(player_name, images.PLAYERNAMEPOS)

    gender_image = images.genders[player_pokemon.gender]
    gender_rect = gender_image.get_rect()
    gender_rect.left = player_name_rect.right + 5
    gender_rect.centery = player_name_rect.centery
    screen.blit(gender_image, gender_rect)

def blit_enemy_name(enemy_pokemon):
    '''Blit the enemy pokemon's name and gender to the screen.'''
    enemy_name = images.render_small_text(str(enemy_pokemon.name))
    enemy_name_rect = screen.blit(enemy_name, images.ENEMYNAMEPOS)

    gender_image = images.genders[enemy_pokemon.gender]
    gender_rect = gender_image.get_rect()
    gender_rect.left = enemy_name_rect.right + 5
    gender_rect.centery = enemy_name_rect.centery
    screen.blit(gender_image, gender_rect)

def blit_player_status_ailment(player_pokemon):
    '''Check for a nonvolatile status ailment on the player, and blit its image to the screen if it exists.'''
    for i in range(len(required_lists.nonvolatile)):
        if player_pokemon.status_nonvolatile == required_lists.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.PLAYER_STATUS_POS)

def blit_enemy_status_ailment(enemy_pokemon):
    '''Check for a nonvolatile status ailment on the enemy, and blit its image to the screen if it exists.'''
    for i in range(len(required_lists.nonvolatile)):
        if enemy_pokemon.status_nonvolatile == required_lists.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.ENEMY_STATUS_POS)

def blit_pp_1(player_pokemon):
    '''Blit the pp of the player's first move.'''
    pp1 = images.render_small_text(str(player_pokemon.pp_list[0]) + "  /  "+str(player_pokemon.moveset[0].pp_full))
    pp1_rect = pp1.get_rect()
    pp1_rect.center = images.PP1POS
    screen.blit(pp1, pp1_rect)

def blit_pp_2(player_pokemon):
    '''Blit the pp of the player's second move.'''
    pp2 = images.render_small_text(str(player_pokemon.pp_list[1]) + "  /  "+str(player_pokemon.moveset[1].pp_full))
    pp2_rect = pp2.get_rect()
    pp2_rect.center = images.PP2POS
    screen.blit(pp2, pp2_rect)

def blit_pp_3(player_pokemon):
    '''Blit the pp of the player's third move.'''
    pp3 = images.render_small_text(str(player_pokemon.pp_list[2]) + "  /  "+str(player_pokemon.moveset[2].pp_full))
    pp3_rect = pp3.get_rect()
    pp3_rect.center = images.PP3POS
    screen.blit(pp3, pp3_rect)

def blit_pp_4(player_pokemon):
    '''Blit the pp of the player's fourth move.'''
    pp4 = images.render_small_text(str(player_pokemon.pp_list[3]) + "  /  "+str(player_pokemon.moveset[3].pp_full))
    pp4_rect = pp4.get_rect()
    pp4_rect.center = images.PP4POS
    screen.blit(pp4, pp4_rect)

def blit_player_party():
    '''Blit the player's party to the bottom of the screen.'''
    offset = 0
    for num in range(len(battle_functions.player_party.player_party)):
        required_lists.party_images[num] = screen.blit(battle_functions.player_party.player_party[num].small_sprite, (7 + offset, 292) )
        offset += 20

def blit_back_button():
    '''Blit a back button to the screen.'''
    required_lists.back_button = screen.blit(images.BACK, images.BACKBUTTONPOS)