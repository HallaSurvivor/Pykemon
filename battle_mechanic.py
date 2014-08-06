'''Handles everything that happens during a single battle sequence.'''
from random import randint
import pygame
import sys
import enemies
import player_party
import required_lists
import items
import images
import battle_functions
import battle_blitting

'''
TO DO LIST

flinch
make everything in move_functions a method
make the pokemon selection menu an iteration
make a move with no PP stay on the selection screen instead of wasting a turn.

make it possible to print to multiple lines
add in attack animations
make held items do things
make abilities a thing



a megaevolve button, and a pokemon-status indicator on the bottom of the screen

'''

in_battle = True
priority = 8


def open_bag():
    global bag

def choose_box_color():
    '''Choose the correct box color based on game state.'''
    if battle_blitting.game_state == "first select":
        required_lists.box_colors[0] = images.BOX
        required_lists.box_colors[1] = images.BOX
        required_lists.box_colors[2] = images.BOX
        required_lists.box_colors[3] = images.BOX

    elif battle_blitting.game_state == "move list":
        if move_choices[0] != "":
            required_lists.box_colors[0] = battle_blitting.select_box(player_pokemon.moveset[0])
        else:
            required_lists.box_colors[0] = images.BOX

        if move_choices[1] != "":
            required_lists.box_colors[1] = battle_blitting.select_box(player_pokemon.moveset[1])
        else:
            required_lists.box_colors[1] = images.BOX

        if move_choices[2] != "":
            required_lists.box_colors[2] = battle_blitting.select_box(player_pokemon.moveset[2])
        else:
            required_lists.box_colors[2] = images.BOX

        if move_choices[3] != "":
            required_lists.box_colors[3] = battle_blitting.select_box(player_pokemon.moveset[3])
        else:
            required_lists.box_colors[3] = images.BOX

    elif battle_blitting.game_state == "wait for prompt":
        required_lists.box_colors[0] = images.BOX
        required_lists.box_colors[1] = images.BOX
        required_lists.box_colors[2] = images.BOX
        required_lists.box_colors[3] = images.BOX


pygame.init()
pygame.display.set_caption("Pokemon!")

player_to_do = 0

wait_timer = 0

battle_functions.auto_choose_pokemon()


while in_battle == True:

    player_pokemon = battle_functions.player_pokemon

    enemy_pokemon = battle_functions.enemy_pokemon

    battle_blitting.render_background()

    choose_box_color()

    battle_blitting.render_correct_boxes()

    battle_blitting.render_hp_boxes()

    battle_blitting.render_player_hp(player_pokemon)

    battle_blitting.render_enemy_hp(enemy_pokemon)

    battle_blitting.blit_pokemon(player_pokemon, enemy_pokemon)

    battle_blitting.blit_numerical_hp(player_pokemon)

    battle_blitting.blit_player_name(player_pokemon)

    battle_blitting.blit_enemy_name(enemy_pokemon)

    battle_blitting.blit_exp(player_pokemon)

    if required_lists.nonvolatile_test_player == True:
        battle_blitting.blit_player_status_ailment(player_pokemon)

    if required_lists.nonvolatile_test_enemy == True:
        battle_blitting.blit_enemy_status_ailment(enemy_pokemon)

    battle_blitting.blit_back_button()

    player_pokemon.calculate_in_battle_stats()
    enemy_pokemon.calculate_in_battle_stats()

    box1 = required_lists.four_boxes[0]
    box2 = required_lists.four_boxes[1]
    box3 = required_lists.four_boxes[2]
    box4 = required_lists.four_boxes[3]

    boxa = required_lists.six_boxes[0]
    boxb = required_lists.six_boxes[1]
    boxc = required_lists.six_boxes[2]
    boxd = required_lists.six_boxes[3]
    boxe = required_lists.six_boxes[4]
    boxf = required_lists.six_boxes[5]


    if battle_blitting.game_state == "first select":


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5
                if player_pokemon.skip_turn == False:
                    move_choices = []

                    if box1.collidepoint(pos):
                        for i in range(len(player_pokemon.moveset)):
                            move_choices.append(player_pokemon.moveset[i].name)
                        while len(move_choices) != 4:
                            move_choices.append("")
                        required_lists.box_data[0] = move_choices[0]
                        required_lists.box_data[1] = move_choices[1]
                        required_lists.box_data[2] = move_choices[2]
                        required_lists.box_data[3] = move_choices[3]
                        battle_blitting.game_state = "move list"

                    elif box3.collidepoint(pos):
                        pokemon_choices = []
                        for i in range(len(player_party.player_party)):
                            pokemon_choices.append(player_party.player_party[i].name)
                        while len(pokemon_choices) != 6:
                            pokemon_choices.append("")

                        required_lists.box_data[4] = pokemon_choices[0]
                        required_lists.box_data[5] = pokemon_choices[1]
                        required_lists.box_data[6] = pokemon_choices[2]
                        required_lists.box_data[7] = pokemon_choices[3]
                        required_lists.box_data[8] = pokemon_choices[4]
                        required_lists.box_data[9] = pokemon_choices[5]
                        battle_blitting.game_state = "pokemon list"
                    elif box4.collidepoint(pos):
                        box5data = "Player successfully ran away"
                        pygame.quit()
                        sys.exit(0)
                else:
                    required_lists.to_print.append("{0} must recharge".format(player_pokemon.name))
                    required_lists.to_damage.append("NULL")
                    player_pokemon.skip_turn = False
                    battle_blitting.game_state = "executing"



    elif battle_blitting.game_state == "move list":


#make this a list and iterate?
        if required_lists.box_data[0] != "":
            battle_blitting.blit_pp_1(player_pokemon)
        if required_lists.box_data[1] != "":
            battle_blitting.blit_pp_2(player_pokemon)
        if required_lists.box_data[2] != "":
            battle_blitting.blit_pp_3(player_pokemon)
        if required_lists.box_data[3] != "":
            battle_blitting.blit_pp_4(player_pokemon)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5

                if required_lists.back_button.collidepoint(pos):
                    battle_blitting.reset_labels()
                    battle_blitting.game_state = "first select"

                for num in range(len(player_pokemon.moveset)):
                    if required_lists.four_boxes[num].collidepoint(pos):
                        player_to_do = num
                        battle_blitting.game_state = "executing"
                        battle_blitting.reset_labels()
                        battle_blitting.print_ask_for_space()



    elif battle_blitting.game_state == "pokemon list":



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5

                if required_lists.back_button.collidepoint(pos):
                    battle_blitting.reset_labels()
                    battle_blitting.game_state = "first select"

                #make the box a greyed out color for the current pkmn, and a red color if feinted
                for num in range(len(player_party.player_party)):
                    if required_lists.six_boxes[num].collidepoint(pos):

                        if player_pokemon.name != required_lists.box_data[num + 4]: #if the clicked pokemon isn't already out

                            battle_functions.player_pokemon = player_party.player_party[num]
                            battle_blitting.game_state = "executing"
                            required_lists.to_print.append("{0}, I choose you!".format(battle_functions.player_pokemon.name))
                            required_lists.to_damage.append("NULL")
                            battle_functions.player_pokemon.reset_in_battle_stats()
                            battle_functions.player_pokemon.calculate_in_battle_stats()
                            battle_blitting.reset_labels()



    elif battle_blitting.game_state == "wait for prompt":



        if len(required_lists.to_print) > 0:
            wait_timer += 1
            if wait_timer == 100:
                battle_blitting.update_box_5(player_pokemon, enemy_pokemon)
                wait_timer = 0
        else:
            battle_blitting.game_state = "first select"
            battle_blitting.reset_labels()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN):

                if len(required_lists.to_print) > 0:
                    box5data = required_lists.to_print[0]
                    wait_timer = 0
                    battle_blitting.update_box_5(player_pokemon, enemy_pokemon)
                else:
                    battle_blitting.game_state = "first select"



    elif battle_blitting.game_state == "executing":



        enemy_to_do = randint(0, 3)
    #priority 8 through -8 execute in descending order, then the loop repeats
        while priority == 8:
            #custap berry
            if player_to_do != 5:
                if player_pokemon.moveset[player_to_do].priority == 8:
                    use_attack(player_pokemon, enemy_pokemon, player_to_do)

            if enemy_pokemon.moveset[enemy_to_do].priority == 8:
                use_attack(enemy_pokemon, player_pokemon, enemy_to_do)
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
            priority = 8
            battle_blitting.game_state = "wait for prompt"


    pygame.display.flip()
else:
    pygame.quit()
    sys.exit(0)