__author__ = 'HallaSurvivor'

#Thanks to stackoverflow for the basis of this code
from random import randint
import pygame
import sys
import enemies
import player_party
import required_lists
import items
import images
import battle_functions


'''
TO DO LIST

implement volatile and battle volatile
make held items do things
make abilities a thing

a megaevolve button, and a pokemon-status indicator on the bottom of the screen

'''

in_battle = True
priority = "start"
game_state = "first select"
select_action = 0
enemy_pokemon = enemies.enemy1.party[0]


#automatic pokemon selection at start of battle
def choose_pokemon():
    global player_pokemon
    for i in range(len(player_party.player_party)):
        if player_party.player_party[i].hp > 0:
            player_pokemon = player_party.player_party[i]


#manual pokemon choice after feinting




#roll out next enemy pokemon
def next_enemy(enemy):
    global enemy_pokemon
    for i in range(len(enemy.party)):
        if enemy.party[i].hp > 0:
            enemy_pokemon = enemy.party[i]
            required_lists.to_print.append("{0} sent out {1}".format(enemy.name, enemy_pokemon.name))
            required_lists.to_damage.append("NULL")
            return True
    else:
        return False


def check_health(player, enemy):
    if player.hp <= 0:
        #make a list of "immediate to print" that will override the current gamestate if len(list) > 0
        #append "player's %pokemon_name feinted!"
        #force select
        #animation?
        game_state = "pokemon select"
    elif enemy.hp <= 0:
        return next_enemy(enemies.enemy1)
        get_exp(player, enemy)
    else:
        return True



def open_bag():
    global bag


def reset_labels():
    global box1data, box2data, box3data, box4data, boxadata, boxbdata, boxcdata, boxddata, boxedata, boxfdata
    box1data = "Fight"
    box2data = "Bag"
    box3data = "Pokemon"
    box4data = "Run"
    boxadata = ""
    boxbdata = ""
    boxcdata = ""
    boxddata = ""
    boxedata = ""
    boxfdata = ""

reset_labels()
def define_text_boxes():
    global box1data, box2data, box3data, box4data, boxadata, boxbdata, boxcdata, boxddata, boxedata, boxfdata
    global box1text, box2text, box3text, box4text, box5text, boxatext, boxbtext, boxctext, boxdtext, boxetext, boxftext
    global box1text_rect, box2text_rect, box3text_rect, box4text_rect, box5text_rect, boxatext_rect, boxbtext_rect, boxctext_rect, boxdtext_rect, boxetext_rect, boxftext_rect

    box1text = images.render_text(box1data)
    box2text = images.render_text(box2data)
    box3text = images.render_text(box3data)
    box4text = images.render_text(box4data)
    box5text = images.render_text(box5data, images.WHITE)

    box1text_rect = box1text.get_rect()
    box2text_rect = box2text.get_rect()
    box3text_rect = box3text.get_rect()
    box4text_rect = box4text.get_rect()
    box5text_rect = box4text.get_rect()

    boxatext = images.render_text(boxadata)
    boxbtext = images.render_text(boxbdata)
    boxctext = images.render_text(boxcdata)
    boxdtext = images.render_text(boxddata)
    boxetext = images.render_text(boxedata)
    boxftext = images.render_text(boxfdata)

    boxatext_rect = boxatext.get_rect()
    boxbtext_rect = boxbtext.get_rect()
    boxctext_rect = boxctext.get_rect()
    boxdtext_rect = boxdtext.get_rect()
    boxetext_rect = boxetext.get_rect()
    boxftext_rect = boxftext.get_rect()


def update_box_5():
    '''Updates the text in box5 alongisde the hp of the pokemon and the status images'''
    if len(required_lists.to_damage) != len(required_lists.to_print):
        del required_lists.to_damage[0] #compensates for a random extra "NULL" that came from somewhere...

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


def render_background():
    global screen
    screen.fill(images.WHITE)
    screen.blit(images.GRASS_BATTLE, images.TOPLEFT)

def render_4_boxes():
    global box1, box2, box3, box4, box5

    box1 = screen.blit(box_1_var, images.BOX1POS)
    box1text_rect.center = box1.center
    screen.blit(box1text, box1text_rect)

    box2 = screen.blit(box_2_var, images.BOX2POS)
    box2text_rect.center = box2.center
    screen.blit(box2text, box2text_rect)

    box3 = screen.blit(box_3_var, images.BOX3POS)
    box3text_rect.center = box3.center
    screen.blit(box3text, box3text_rect)

    box4 = screen.blit(box_4_var, images.BOX4POS)
    box4text_rect.center = box4.center
    screen.blit(box4text, box4text_rect)

def render_6_boxes():
    global boxa, boxb, boxc, boxd, boxe, boxf
    boxa = screen.blit(images.POKEMONBOX, images.BOXAPOS)
    boxatext_rect.center = boxa.center
    screen.blit(boxatext, boxatext_rect)

    boxb = screen.blit(images.POKEMONBOX, images.BOXBPOS)
    boxbtext_rect.center = boxb.center
    screen.blit(boxbtext, boxbtext_rect)

    boxc = screen.blit(images.POKEMONBOX, images.BOXCPOS)
    boxctext_rect.center = boxc.center
    screen.blit(boxctext, boxctext_rect)

    boxd = screen.blit(images.POKEMONBOX, images.BOXDPOS)
    boxdtext_rect.center = boxd.center
    screen.blit(boxdtext, boxdtext_rect)

    boxe = screen.blit(images.POKEMONBOX, images.BOXEPOS)
    boxetext_rect.center = boxe.center
    screen.blit(boxetext, boxetext_rect)

    boxf = screen.blit(images.POKEMONBOX, images.BOXFPOS)
    boxftext_rect.center = boxf.center
    screen.blit(boxftext, boxftext_rect)

def render_box_5():
    global box5
    box5 = screen.blit(images.TEXTBOX, images.BOX5POS)
    box5text_rect.left = box5.left + 15
    box5text_rect.top = box5.top + 15
    screen.blit(box5text, box5text_rect)

def render_choice_boxes():
    render_box_5()
    if game_state != "pokemon list":
        render_4_boxes()
    else:
        render_6_boxes()


def render_hp_boxes():
    global screen
    screen.blit(images.PLAYER_HP_BOX, images.PLAYERHPPOS)
    screen.blit(images.ENEMY_HP_BOX, images.ENEMYHPPOS)

def render_player_hp():
    hp_percent = float(player_pokemon.hp)/float(player_pokemon.hp_full)
    hp_to_render = hp_percent * 84 #hp bar is 84px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (275+hp, 174))

def render_enemy_hp():
    hp_percent = float(enemy_pokemon.hp)/float(enemy_pokemon.hp_full)
    hp_to_render = hp_percent * 86 #hp bar is 86px wide
    hp_to_render = int(hp_to_render)
    for hp in range(hp_to_render):
        screen.blit(images.HP_GREEN, (74+hp, 40))


def select_box(move):
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

def choose_box_color():
    global box_1_var, box_2_var, box_3_var, box_4_var
    if game_state == "first select":
        box_1_var = images.BOX
        box_2_var = images.BOX
        box_3_var = images.BOX
        box_4_var = images.BOX
    elif game_state == "move list":
        if move_choices[0] != "":
            box_1_var = select_box(player_pokemon.moveset[0])
        else:
            box_1_var = images.BOX

        if move_choices[1] != "":
            box_2_var = select_box(player_pokemon.moveset[1])
        else:
            box_1_var = images.BOX

        if move_choices[2] != "":
            box_3_var = select_box(player_pokemon.moveset[2])
        else:
            box_1_var = images.BOX

        if move_choices[3] != "":
            box_4_var = select_box(player_pokemon.moveset[3])
        else:
            box_1_var = images.BOX

    elif game_state == "wait for prompt":
        box_1_var = images.BOX
        box_2_var = images.BOX
        box_3_var = images.BOX
        box_4_var = images.BOX

def blit_pokemon():
    screen.blit(player_pokemon.player_sprite, images.BOTTOMLEFT)
    screen.blit(enemy_pokemon.enemy_sprite, images.TOPRIGHT)

def blit_numerical_hp():
    numerical_hp = images.render_small_text(str(player_pokemon.hp))
    numerical_hp_full = images.render_small_text("/  " + str(player_pokemon.hp_full))
    screen.blit(numerical_hp, images.HPTEXTPOS)
    screen.blit(numerical_hp_full, images.FULLHPTEXTPOS)

def blit_player_name():
    player_name = images.render_small_text(str(player_pokemon.name))
    screen.blit(player_name, images.PLAYERNAMEPOS)
    player_name_rect = player_name.get_rect()
    gender_rect = images.MALE.get_rect()
    gender_rect.center = player_name_rect.center
    screen.blit(images.MALE, gender_rect)

def blit_enemy_name():
    enemy_name = images.render_small_text(str(enemy_pokemon.name))
    screen.blit(enemy_name, images.ENEMYNAMEPOS)

def blit_status_ailment():
    for i in range(len(required_lists.nonvolatile)):
        if player_pokemon.status_nonvolatile == required_lists.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.PLAYER_STATUS_POS)

        if enemy_pokemon.status_nonvolatile == required_lists.nonvolatile[i]:
            screen.blit(images.status_icons[i], images.ENEMY_STATUS_POS)

def blit_exp():
    exp_percent = float(player_pokemon.exp) / float(player_pokemon.needed_exp)
    exp_percent = int(exp_percent)
    for exp in exp_percent:
        screen.blit(EXP_BAR, (300+exp, 200) )

def blit_pp_1():
    pp1 = images.render_small_text(str(player_pokemon.pp_list[0]) + "  /  "+str(player_pokemon.moveset[0].pp_full))
    pp1_rect = pp1.get_rect()
    pp1_rect.center = images.PP1POS
    screen.blit(pp1, pp1_rect)

def blit_pp_2():
    pp2 = images.render_small_text(str(player_pokemon.pp_list[1]) + "  /  "+str(player_pokemon.moveset[1].pp_full))
    pp2_rect = pp2.get_rect()
    pp2_rect.center = images.PP2POS
    screen.blit(pp2, pp2_rect)

def blit_pp_3():
    pp3 = images.render_small_text(str(player_pokemon.pp_list[2]) + "  /  "+str(player_pokemon.moveset[2].pp_full))
    pp3_rect = pp3.get_rect()
    pp3_rect.center = images.PP3POS
    screen.blit(pp3, pp3_rect)

def blit_pp_4():
    pp4 = images.render_small_text(str(player_pokemon.pp_list[3]) + "  /  "+str(player_pokemon.moveset[3].pp_full))
    pp4_rect = pp4.get_rect()
    pp4_rect.center = images.PP4POS
    screen.blit(pp4, pp4_rect)

def blit_back_button():
    global back_button
    back_button = screen.blit(images.BACK, images.BACKBUTTONPOS)


pygame.init()
pygame.display.set_caption("Pokemon!")
choose_pokemon()
reset_labels()
box5data = ""

screen = images.SCREEN

player_to_do = 0

while in_battle == True:
    define_text_boxes()

    render_background()

    choose_box_color()

    render_choice_boxes()

    render_hp_boxes()

    render_player_hp()

    render_enemy_hp()

    blit_pokemon()

    blit_numerical_hp()

    blit_player_name()

    blit_enemy_name()

    blit_status_ailment()

    blit_back_button()

    if game_state == "move list":
        if box1data != "":
            blit_pp_1()
        if box2data != "":
            blit_pp_2()
        if box3data != "":
            blit_pp_3()
        if box4data != "":
            blit_pp_4()

    while priority == "start":
        choose_pokemon()
        player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(player_pokemon)
        player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(enemy_pokemon)
        priority = 8

    enemy_to_do = randint(0, 3)

#get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

#if you're printing stuff to box5
        if game_state == "wait for prompt":
            if len(required_lists.to_print) > 0:
                box5data = required_lists.to_print[0]
                if event.type == pygame.KEYDOWN:
                    update_box_5()
            else:
                box5data = ""
                game_state = "first select"


#if the user clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

#if you're on the main screen (fight/bag/pkmn/run):
            if game_state == "first select":
                player_to_do = 5
                if player_pokemon.skip_turn == False:
                    move_choices = []
                    if box1.collidepoint(pos):
                        for i in range(len(player_pokemon.moveset)):
                            move_choices.append(player_pokemon.moveset[i].name)
                        while len(move_choices) != 4:
                            move_choices.append("")
                        box1data = move_choices[0]
                        box2data = move_choices[1]
                        box3data = move_choices[2]
                        box4data = move_choices[3]
                        game_state = "move list"

                    elif box3.collidepoint(pos):
                        pokemon_choices = []
                        for i in range(len(player_party.player_party)):
                            pokemon_choices.append(player_party.player_party[i].name)
                        while len(pokemon_choices) != 6:
                            pokemon_choices.append("")

                        boxadata = pokemon_choices[0]
                        boxbdata = pokemon_choices[1]
                        boxcdata = pokemon_choices[2]
                        boxddata = pokemon_choices[3]
                        boxedata = pokemon_choices[4]
                        boxfdata = pokemon_choices[5]
                        game_state = "pokemon list"
                    elif box4.collidepoint(pos):
                        box5data = "Player successfully ran away"
                        pygame.quit()
                        sys.exit(0)
                else:
                    required_lists.to_print.append("{0} must recharge".format(player_pokemon.name))
                    required_lists.to_damage.append("NULL")
                    player_pokemon.skip_turn = False
                    game_state = "wait for prompt"
                    select_action = 1

#if you're on the move list screen
            elif game_state == "move list":
                player_to_do = 5
                if box1.collidepoint(pos) and box1data != "":
                    player_to_do = 0
                    select_action = 1
                    game_state = "wait for prompt"
                    reset_labels()
                elif box2.collidepoint(pos) and box2data != "":
                    player_to_do = 1
                    select_action = 1
                    game_state = "wait for prompt"
                    reset_labels()
                elif box3.collidepoint(pos) and box3data != "":
                    player_to_do = 2
                    select_action = 1
                    game_state = "wait for prompt"
                    reset_labels()
                elif box4.collidepoint(pos) and box4data != "":
                    player_to_do = 3
                    select_action = 1
                    game_state = "wait for prompt"
                    reset_labels()
                elif back_button.collidepoint(pos):
                    reset_labels()
                    game_state = "first select"

#if you're on the pokemon list screen
            elif game_state == "pokemon list":
                player_to_do = 5
                #make the box a greyed out color for the current pkmn, and a red color if feinted
                if boxa.collidepoint(pos):
                    if boxadata != "":
                        if player_pokemon.name != boxadata:
                            player_pokemon = player_party.player_party[0]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif boxb.collidepoint(pos):
                    if boxbdata != "":
                        if player_pokemon.name != boxbdata:
                            player_pokemon = player_party.player_party[1]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif boxc.collidepoint(pos):
                    if boxcdata != "":
                        if player_pokemon.name != boxcdata:
                            player_pokemon = player_party.player_party[2]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif boxd.collidepoint(pos):
                    if boxddata != "":
                        if player_pokemon.name != boxddata:
                            player_pokemon = player_party.player_party[3]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif boxe.collidepoint(pos):
                    if boxedata != "":
                        if player_pokemon.name != boxedata:
                            player_pokemon = player_party.player_party[4]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif boxf.collidepoint(pos):
                    if boxfdata != "":
                        if player_pokemon.name != boxfdata:
                            player_pokemon = player_party.player_party[5]
                            select_action = 1
                            required_lists.to_print.append("{0}, I choose you!".format(player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            game_state = "wait for prompt"
                            reset_labels()


                elif back_button.collidepoint(pos):
                    reset_labels()
                    game_state = "first select"

    while select_action == 1:
    #priority 8 through -8 execute in descending order, then the loop repeats
        while priority == 8:
            #custap berry
            #if player_pokemon.moveset[player_to_do].name == "quick claw": FIX FOR PLALYER_TO_DO == 5
                #use_attack(player_pokemon, enemy_pokemon, player_to_do)
            priority = 7

        while priority == 7:
            #if opponent switches, pursuit
            priority = 6

        while priority == 6:
            #switching out, itemes, escaping, Focus Punch Charge, mega evo
            priority = 5

        while priority == 5:
            #if player_pokemon.moveset[player_to_do].name == "helping hand":
             #   use_attack(player_pokemon, enemy_pokemon, player_to_do)
            priority = 4

        while priority == 4:
            #detect, magic coat, protect, spiky shield, snatch
            priority = 3

        while priority == 3:
            #endure, fake out, king's shield, quick guard, wide guiard, crafty shield
            priority = 2

        while priority == 2:
            #extreme speed, feint, follow me, rage powder
            #if player_pokemon.moveset[player_to_do].name == "extreme speed":
             #   use_attack(player_pokemon, enemy_pokemon, player_to_do)
            priority = 1

        while priority == 1:
            #ally switch, aqua jet, baby doll eyes, bide, bullet punch, ice shard, ion deluge, mach punch, powder, quick attack, shadow snake, sucker punch, vacuum wave, water shruiken
            priority = 0

        while priority == 0:
            battle_functions.check_speed(player_pokemon, enemy_pokemon, player_to_do, enemy_to_do)
            priority = -1

        while priority == -1:
            #vital throw
            priority = -2

        while priority == -2:
            priority = -3 #priority 2 actually does nothing... idk why

        while priority == -3:
            #focus punch
            priority = -4

        while priority == -4:
            #avalanche, revenge
            priority = -5

        while priority == -5:
            #counter, mirror coat
            priority = -6

        while priority == -6:
            #circle throw, dragon tail, roar, whirlwind
            priority = -7

        while priority == -7:
            #trick room
            priority = -8

        while priority == -8:
            battle_functions.check_status(player_pokemon)
            battle_functions.check_status(enemy_pokemon)
            battle_functions.check_volatile_status(player_pokemon)
            battle_functions.check_volatile_status(enemy_pokemon)
            in_battle = check_health(player_pokemon, enemy_pokemon)
            priority = 8
            select_action = 0


    pygame.display.flip()
else:
    pygame.quit()
    sys.exit(0)