"""Handles everything that happens during a single battle sequence."""
from random import randint
import pygame
import sys
import player_party
import required_lists as r
import items
import battle_functions as f
import battle_blitting as b
import printing as p

'''
TO DO LIST

make b a class, make a class for battle variables (weather, mist, etc.)
make a move with no PP stay on the selection screen instead of wasting a turn.

replace all "break"s with "return 0" and add an "else: print 'function name' failed" to detect if a function failed

make it possible to print to multiple lines
make the enemy AI more advanced
add in attack animations
make held items do things
make abilities a thing



a megaevolve button on the bottom of the screen

http://www.upokecenter.com/content/pokemon-black-version-and-pokemon-white-version-timing-notes

'''

priority = 8


def open_bag():
    global bag


pygame.init()
pygame.display.set_caption("Pokemon!")

player_to_do = 0

wait_timer = 0

f.auto_choose_pokemon()

while r.in_battle is True:

    b.blit_battle_screen()

    b.blit_player_status_ailment()

    b.blit_enemy_status_ailment()

    b.blit_back_button()

    # Make this part of an "initial send out" function.
    f.player_pokemon.calculate_in_battle_stats()
    f.enemy_pokemon.calculate_in_battle_stats()

    box1 = r.four_boxes[0]
    box2 = r.four_boxes[1]
    box3 = r.four_boxes[2]
    box4 = r.four_boxes[3]

    boxa = r.six_boxes[0]
    boxb = r.six_boxes[1]
    boxc = r.six_boxes[2]
    boxd = r.six_boxes[3]
    boxe = r.six_boxes[4]
    boxf = r.six_boxes[5]

    b.blit_in_party_stats()

    if b.game_state == b.Battle_States.first_select:


        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            b.check_for_hover_over_party(pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5
                if f.player_pokemon.skip_turn == False:

                    if box1.collidepoint(pos):
                        movelist = []
                        for i in range(len(f.player_pokemon.moveset)):
                            movelist.append(f.player_pokemon.moveset[i].name)
                        while len(movelist) != 4:
                            movelist.append("")
                        for i in range(4):
                            r.box_data[i] = movelist[i]

                        b.game_state = b.Battle_States.move_select

                    elif box3.collidepoint(pos):
                        pokemon_choices = []
                        for i in range(len(player_party.player_party)):
                            pokemon_choices.append(player_party.player_party[i].name)
                        while len(pokemon_choices) != 6:
                            pokemon_choices.append("")

                        r.box_data[4] = pokemon_choices[0]
                        r.box_data[5] = pokemon_choices[1]
                        r.box_data[6] = pokemon_choices[2]
                        r.box_data[7] = pokemon_choices[3]
                        r.box_data[8] = pokemon_choices[4]
                        r.box_data[9] = pokemon_choices[5]
                        b.game_state = b.Battle_States.pokemon_select

                    elif box4.collidepoint(pos):
                        r.to_do.append("end battle")
                        player_to_do = 5
                        b.game_state = b.Battle_States.executing

                else:
                    r.to_do.append("{0} must recharge".format(f.player_pokemon.name))
                    r.to_damage.append("NULL")
                    f.player_pokemon.skip_turn = False
                    b.game_state = b.Battle_States.executing



    elif b.game_state == b.Battle_States.move_select:

        b.blit_pp()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            b.check_for_hover_over_party(pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5

                if r.back_button.collidepoint(pos):
                    b.reset_labels()
                    b.game_state = b.Battle_States.first_select

                for num in range(len(f.player_pokemon.moveset)):
                    if r.four_boxes[num].collidepoint(pos):
                        player_to_do = num
                        b.game_state = b.Battle_States.executing
                        b.reset_labels()
                        b.print_ask_for_space()



    elif b.game_state == b.Battle_States.pokemon_select:


        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            b.check_for_hover_over_party(pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                player_to_do = 5

                if r.back_button.collidepoint(pos):
                    b.reset_labels()
                    b.game_state = b.Battle_States.first_select

                for num in range(len(player_party.player_party)):
                    if r.six_boxes[num].collidepoint(pos):

                        if f.player_pokemon.name != r.box_data[num + 4]:  #if the clicked pokemon isn't already out
                            if not player_party.player_party[num].fainted:
                                f.player_pokemon.to_switch_out = True
                                player_party.player_party[num].to_switch_in = True
                                b.game_state = b.Battle_States.executing
                                b.reset_labels()



    elif b.game_state == b.Battle_States.printing:
        if len(r.to_do) > 0:

            if isinstance(r.to_do[0], p.PrintingStuff):
                wait_timer += 1
                if wait_timer == 100:
                    b.update_box_5()
                    wait_timer = 0

            else:
                b.update_box_5()

        else:
            b.game_state = b.Battle_States.first_select
            b.reset_labels()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            b.check_for_hover_over_party(pos)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) \
                    or (event.type == pygame.KEYDOWN):

                if len(r.to_do) > 0:
                    wait_timer = 0
                    b.update_box_5()
                else:
                    b.game_state = b.Battle_States.first_select



    elif b.game_state == b.Battle_States.executing:

        enemy_to_do = randint(0, 3)
        #priority 8 through -8 execute in descending order, then the loop repeats
        while priority == 8:
            #custap berry
            '''
            if player_to_do != 5:
                if player_pokemon.moveset[player_to_do].priority == 8:
                    player_pokemon.moveset[player_to_do].use(player_pokemon, enemy_pokemon)

            if enemy_pokemon.moveset[enemy_to_do].priority == 8:
                enemy_pokemon.moveset[enemy_to_do].use(enemy_pokemon, player_pokemon)
                '''
            priority = 7

        while priority == 7:
            #if opponent switches, pursuit:
            #if enemy_pokemon.to_switch_out == True:
            #pursuit
            priority = 6

        while priority == 6:

            if f.player_pokemon.to_switch_out is True:
                f.player_pokemon.reset_all_stats()

                for i in range(len(player_party.player_party)):

                    if player_party.player_party[i].to_switch_in is True:
                        p.add_to_print_buffer("{0}, I choose you!".format(player_party.player_party[i].name),
                                              required_pokemon=[f.player_pokemon],
                                              to_switch_in=player_party.player_party[i])

                        f.player_pokemon.to_switch_out = False
                        player_party.player_party[i].to_switch_in = False
                        break

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
            f.check_speed(player_to_do, enemy_to_do)
            priority = -1

        while priority == -1:
            #vital throw
            priority = -2

        while priority == -2:
            priority = -3  #priority 2 actually does nothing... idk why

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
            r.to_do.append("check player status")
            r.to_do.append("check enemy status")

            r.to_do.append("check player volatile")
            r.to_do.append("check enemy volatile")

            p.add_to_print_buffer(" ", required_pokemon=[f.enemies.default])

            priority = 8
            b.game_state = b.Battle_States.printing

            f.end_of_turn_reset()

    pygame.display.flip()
else:
    pygame.quit()
    sys.exit(0)
