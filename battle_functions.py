'''Handles all of the functions associated with being in a battle.'''
import player_party
import enemies
import required_lists
import move_list
from random import randint

player_pokemon = 0

required_lists.current_enemy = enemies.enemy1

enemy_pokemon = required_lists.current_enemy.party[0]

def auto_choose_pokemon():
    '''Automatically selects the first pokemon in the player's party with hp > 0.'''
    global player_pokemon
    for i in range(len(player_party.player_party)):
        if player_party.player_party[i].hp > 0:
            player_pokemon = player_party.player_party[i]
            break

def check_speed(player, enemy, player_choice, enemy_choice):
    '''Compares the speeds of the player and enemy pokemon, and does the faster pokemon's move first.'''
    if player_choice != 5:
        if player.battle_speed > enemy.battle_speed:
            player.moveset[player_choice].use(player, enemy)
            print"ran layer"
            check_player_health(player)
            check_enemy_health(player, enemy)
            enemy.moveset[enemy_choice].use(enemy, player)
            print "ran enemy"
        else:
            enemy.moveset[enemy_choice].use(enemy, player)
            print "ran enemy"
            check_player_health(player)
            check_enemy_health(player, enemy)
            player.moveset[player_choice].use(player, enemy)
            print "ran player"
    else:
        enemy.moveset[enemy_choice].use(enemy, player)
        check_player_health(player)
        check_enemy_health(player, enemy)


def check_player_health(player):
    '''Check if the player hp is > 0, if not, have the user select another pokemon.'''
    if player.hp <= 0:
        required_lists.to_print.append("{0} feinted!".format(player.name))
        #animation?
        watch_count = 0
        for i in range(len(player_party.player_party)):
            if player_party.player_party[i].hp > 0:
                game_state = "pokemon select"
            else:
                watch_count += 1
        else:
            if watch_count == len(player_party.player_party):
                required_lists.to_print.append("{0} is out of usable pokemon!".format("Player"))
                required_lists.to_print.append("{0} whited out!".format("Player"))

def get_money():
    '''Give the player money after winning a battle.'''
    pass
    #money_recieved += required_lists.payday_count * Meowth.level (or Purrloin.level)

def check_enemy_health(player, enemy):
    '''Check if the enemy healtlh is > 0, if not, return the next pokemon and give experience.'''
    global enemy_pokemon
    if enemy.hp <= 0:
        required_lists.to_print.append("{0} feinted!".format(enemy.name))
        for i in range(len(required_lists.current_enemy.party)):
            if required_lists.current_enemy.party[i].hp > 0:
                required_lists.to_print.append("{0} sent out {1}!".format(required_lists.current_enemy.name, required_lists.current_enemy.party[i].name))
                enemy_pokemon = required_lists.current_enemy.party[i]

        else:
            required_lists.to_print.append("{0} has run out of usable pokemon!")
            get_money()

        player.get_exp(enemy)
        player.get_ev(enemy)
        print player.exp
        print player.ev
        print "\n"


