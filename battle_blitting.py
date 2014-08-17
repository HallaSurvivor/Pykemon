'''Handles all of the graphics in the battle screen.'''
import pygame
import required_lists as r
import images
import battle_functions as f


screen = images.SCREEN


class Battle_States(object):
    first_select = 0
    move_select = 1
    item_select = 2
    pokemon_select = 3
    executing = 4
    printing = 5

game_state = Battle_States.first_select


def render_background():
    '''Fill the background with white to make sure the battle screen blits on a clean surface.'''
    screen.fill(images.WHITE)
    screen.blit(images.GRASS_BATTLE, images.TOPLEFT)

def reset_labels():
    '''Resets the text in the available boxes.'''
    r.box_data = ["Fight", "Bag", "Pokemon", "Run", "", "", "", "", "", ""]
    r.box5data = "What would you like to do?"

def print_ask_for_space():
    '''Tell the user to push a button to continue.'''
    r.box5data = "Press any key to continue."

def define_text_boxes():
    '''Renders the text that goes in each box, and defines a rectangle around each block of text.'''
    text_image_list = []
    text_box_list = []

    for i in range(4):
        text_image_list.append(images.render_text(r.box_data[i]))

    six_box_list = []
    for i in range(len(f.player_party.player_party)):
        if f.player_party.player_party[i].fainted == False:
            six_box_list.append(images.render_text(r.box_data[i+4]))
        else:
            six_box_list.append(images.render_text(r.box_data[i+4], color=images.WHITE))

    while len(six_box_list) != 6:
        six_box_list.append(images.render_text(""))

    for i in range(6):
        text_image_list.append(six_box_list[i])

    for i in range(10):
        text_box_list.append(text_image_list[i].get_rect())

    return [text_image_list, text_box_list]

def render_4_boxes():
    '''Blit the 4 boxes, with corrosponding text, to the screen.'''
    text_list = define_text_boxes()

    box1 = screen.blit(r.box_colors[0], images.BOX1POS)
    text_list[1][0].center = box1.center
    screen.blit(text_list[0][0], text_list[1][0])

    box2 = screen.blit(r.box_colors[1], images.BOX2POS)
    text_list[1][1].center = box2.center
    screen.blit(text_list[0][1], text_list[1][1])

    box3 = screen.blit(r.box_colors[2], images.BOX3POS)
    text_list[1][2].center = box3.center
    screen.blit(text_list[0][2], text_list[1][2])

    box4 = screen.blit(r.box_colors[3], images.BOX4POS)
    text_list[1][3].center = box4.center
    screen.blit(text_list[0][3], text_list[1][3])

    r.four_boxes = [box1, box2, box3, box4]

def render_6_boxes():
    '''Blit the 6 boxes, with corrosponding pokemon, to the screen.'''
    text_list = define_text_boxes()

    boxa = screen.blit(r.box_colors[0], images.BOXAPOS)
    text_list[1][4].center = boxa.center
    screen.blit(text_list[0][4], text_list[1][4])

    boxb = screen.blit(r.box_colors[1], images.BOXBPOS)
    text_list[1][5].center = boxb.center
    screen.blit(text_list[0][5], text_list[1][5])

    boxc = screen.blit(r.box_colors[2], images.BOXCPOS)
    text_list[1][6].center = boxc.center
    screen.blit(text_list[0][6], text_list[1][6])

    boxd = screen.blit(r.box_colors[3], images.BOXDPOS)
    text_list[1][7].center = boxd.center
    screen.blit(text_list[0][7], text_list[1][7])

    boxe = screen.blit(r.box_colors[4], images.BOXEPOS)
    text_list[1][8].center = boxe.center
    screen.blit(text_list[0][8], text_list[1][8])

    boxf = screen.blit(r.box_colors[5], images.BOXFPOS)
    text_list[1][9].center = boxf.center
    screen.blit(text_list[0][9], text_list[1][9])

    r.six_boxes = [boxa, boxb, boxc, boxd, boxe, boxf]


def render_box_5():
    '''Blits the info box to the screen, along with its corrosponding text.'''
    box5_text_image = images.render_text(r.box5data, images.WHITE)
    box5_text_rect = box5_text_image.get_rect()
    box5 = screen.blit(images.TEXTBOX, images.BOX5POS)
    box5_text_rect.left = box5.left + 15
    box5_text_rect.top = box5.top + 15
    screen.blit(box5_text_image, box5_text_rect)

def update_box_5():
    '''Updates the text in box5 alongisde the hp of the pokemon and the status images'''
    if len(r.to_do) == 0:
        r.box5data = "What would you like to do?"
        game_state = Battle_States.first_select


    else:
        if isinstance(r.to_do[0], r.PrintingStuff):
            r.to_do[0].print_text()
            r.to_do.insert(1, "check player health")
            r.to_do.insert(2, "check enemy health")

        elif r.to_do[0] == "check player status":
            f.player_pokemon.check_status()

        elif r.to_do[0] == "check enemy status":
            f.enemy_pokemon.check_status()

        elif r.to_do[0] == "check player volatile":
            f.player_pokemon.check_volatile_status()

        elif r.to_do[0] == "check enemy volatile":
            f.enemy_pokemon.check_volatile_status()

        elif r.to_do[0] == "check player health":
            f.check_player_health()

        elif r.to_do[0] == "check enemy health":
            f.check_enemy_health()

        elif r.to_do[0] == "end battle":
            r.in_battle = False

        del r.to_do[0]


def render_correct_boxes():
    '''Blits either 4 or 6 boxes depending on the game state, always blits box5.'''
    render_box_5()
    if game_state != Battle_States.pokemon_select:
        render_4_boxes()
    else:
        render_6_boxes()

def render_hp_boxes():
    '''Blits the hp boxes to the screen.'''
    screen.blit(images.PLAYER_HP_BOX, images.PLAYERHPPOS)
    screen.blit(images.ENEMY_HP_BOX, images.ENEMYHPPOS)

def render_player_hp():
    '''Blits the graphical representation of the player's HP to the screen.'''
    hp_percent = float(f.player_pokemon.hp)/float(f.player_pokemon.hp_full)
    hp_to_render = hp_percent * 84 #hp bar is 84px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (275+hp, 174))

def render_enemy_hp():
    '''Blits the graphical representation of the enemy's HP to the screen.'''
    hp_percent = float(f.enemy_pokemon.hp)/float(f.enemy_pokemon.hp_full)
    hp_to_render = hp_percent * 86 #hp bar is 86px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (74+hp, 40))

def blit_exp():
    '''Blit the correct length experience bar to the screen.'''
    exp_percent = float(f.player_pokemon.exp) / float(f.player_pokemon.needed_exp)
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

def blit_pokemon():
    '''Blit the actual pokemon sprites in their proper places.'''
    screen.blit(f.player_pokemon.player_sprite, images.PLAYERSPRITEPOS)
    screen.blit(f.enemy_pokemon.enemy_sprite, images.ENEMYSPRITEPOS)

def blit_numerical_hp():
    '''Blit the actual hp value to the screen for the player pokemon.'''
    if f.player_pokemon.hp <= 0:
        numerical_hp = images.render_small_text(str(0))
    else:
        numerical_hp = images.render_small_text(str(f.player_pokemon.hp))
    numerical_hp_full = images.render_small_text("/  " + str(f.player_pokemon.hp_full))
    screen.blit(numerical_hp, images.HPTEXTPOS)
    screen.blit(numerical_hp_full, images.FULLHPTEXTPOS)

def blit_player_name():
    '''Blit the player's name and gender to the screen.'''
    player_name = images.render_small_text(str(f.player_pokemon.name))
    player_name_rect = screen.blit(player_name, images.PLAYERNAMEPOS)

    gender_image = images.genders[f.player_pokemon.gender]
    gender_rect = gender_image.get_rect()
    gender_rect.left = player_name_rect.right + 5
    gender_rect.centery = player_name_rect.centery
    screen.blit(gender_image, gender_rect)

def blit_enemy_name():
    '''Blit the enemy pokemon's name and gender to the screen.'''
    enemy_name = images.render_small_text(str(f.enemy_pokemon.name))
    enemy_name_rect = screen.blit(enemy_name, images.ENEMYNAMEPOS)

    gender_image = images.genders[f.enemy_pokemon.gender]
    gender_rect = gender_image.get_rect()
    gender_rect.left = enemy_name_rect.right + 5
    gender_rect.centery = enemy_name_rect.centery
    screen.blit(gender_image, gender_rect)

def blit_player_status_ailment():
    '''Check for a nonvolatile status ailment on the player, and blit its image to the screen if it exists.'''
    for i in range(len(r.nonvolatile)):
        if f.player_pokemon.status_nonvolatile == r.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.PLAYER_STATUS_POS)

def blit_enemy_status_ailment():
    '''Check for a nonvolatile status ailment on the enemy, and blit its image to the screen if it exists.'''
    for i in range(len(r.nonvolatile)):
        if f.enemy_pokemon.status_nonvolatile == r.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.ENEMY_STATUS_POS)

def blit_pp():
    '''Blit the pp of the player's moveset'''
    for i in range(len(f.player_pokemon.pp_list)):
        pp = images.render_small_text(str(f.player_pokemon.pp_list[i]) + "  /  "+str(f.player_pokemon.moveset[i].pp_full))
        pp_rect = pp.get_rect()
        pp_rect.center = images.PP_POS_LIST[i]
        screen.blit(pp, pp_rect)

def blit_player_party():
    '''Blit the player's party to the bottom of the screen.'''
    offset = 0
    for i in range(len(f.player_party.player_party)):
        r.party_images[i] = screen.blit(f.player_party.player_party[i].small_sprite, (7 + offset, 292) )
        offset += 25

def blit_back_button():
    '''Blit a back button to the screen.'''
    r.back_button = screen.blit(images.BACK, images.BACKBUTTONPOS)

def blit_in_party_stats():
    '''Blit the stats of the pokemon who the user is hovering over to (0, 0).'''
    if r.render_stats != -1:
        stat_box = screen.blit(images.SQUAREBOX, (0, 0))

        pokemon_name = images.render_small_text(f.player_party.player_party[r.render_stats].name)
        pokemon_name_rect = pokemon_name.get_rect()
        pokemon_name_rect.centerx = stat_box.centerx
        pokemon_name_rect.top = stat_box.top + 10
        screen.blit(pokemon_name, pokemon_name_rect)
        if f.player_party.player_party[r.render_stats].fainted == False:
            for i in range(len(r.nonvolatile)):
                if f.player_party.player_party[r.render_stats].status_nonvolatile == r.nonvolatile[i]:
                    screen.blit(images.status_icons[i], (15, 20))
        else:
            screen.blit(images.FNT, (15, 20))

def check_for_hover_over_party(pos):
    '''Check if the user is hovering over a pokemon.'''
    for num in range(len(f.player_party.player_party)):
        if r.party_images[num].collidepoint(pos):
            r.render_stats = num
            break
        else:
            r.render_stats = -1

def choose_box_color():
    '''Choose the correct box color based on game state.'''
    #By default, they're all white
    r.box_colors[0] = images.BOX
    r.box_colors[1] = images.BOX
    r.box_colors[2] = images.BOX
    r.box_colors[3] = images.BOX

    if game_state == Battle_States.move_select:
        for i in range(len(f.player_pokemon.moveset)):
            r.box_colors[i] = select_box(f.player_pokemon.moveset[i])


    elif game_state == Battle_States.pokemon_select:
        pkmn_boxes = []
        for i in range(len(f.player_party.player_party)):
            if f.player_party.player_party[i].fainted == True:
                pkmn_boxes.append(images.FAINTEDPOKEMONBOX)
            else:
                pkmn_boxes.append(images.POKEMONBOX)
        while len(pkmn_boxes) != 6:
            pkmn_boxes.append(images.POKEMONBOX)

        for i in range(6):
            r.box_colors[i] = pkmn_boxes[i]


def blit_battle_screen():

    render_background()

    choose_box_color()

    render_correct_boxes()

    render_hp_boxes()

    render_player_hp()

    render_enemy_hp()

    blit_pokemon()

    blit_numerical_hp()

    blit_player_name()

    blit_enemy_name()

    blit_exp()

    blit_player_party()
