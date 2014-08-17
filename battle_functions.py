'''Handles all of the functions associated with being in a battle.'''
import player_party
import enemies
import required_lists
import move_list
from random import randint


player_pokemon = player_party.Cameron

enemies.current_enemy = enemies.enemy1

enemy_pokemon = enemies.current_enemy.party[0]


def auto_choose_pokemon():
    '''Automatically selects the first pokemon in the player's party with hp > 0.'''
    global player_pokemon
    for i in range(len(player_party.player_party)):
        if player_party.player_party[i].hp > 0:
            player_pokemon = player_party.player_party[i]
            break

def check_speed(player_choice, enemy_choice):
    '''Compares the speeds of the player and enemy pokemon, and does the faster pokemon's move first.'''
    if player_choice != 5:
        if player_pokemon.battle_speed > enemy_pokemon.battle_speed:
            player_pokemon.moveset[player_choice].use(player_pokemon, enemy_pokemon)
            enemy_pokemon.moveset[enemy_choice].use(enemy_pokemon, player_pokemon)
        else:
            enemy_pokemon.moveset[enemy_choice].use(enemy_pokemon, player_pokemon)
            player_pokemon.moveset[player_choice].use(player_pokemon, enemy_pokemon)
    else:
        enemy_pokemon.moveset[enemy_choice].use(enemy_pokemon, player_pokemon)




def check_player_health():
    '''Check if the player hp is > 0, if not, have the user select another pokemon.'''
    if player_pokemon.hp <= 0:
        required_lists.to_do.append("{0} fainted!".format(player_pokemon.name))
        #animation?
        watch_count = 0
        player_pokemon.faint()
        for i in range(len(player_party.player_party)):
            if not player_party.player_party[i].fainted:
                game_state = "pokemon select"
                return 0

        else:
                required_lists.to_do.append("{0} is out of usable pokemon!".format("Player"))
                required_lists.to_do.append("{0} whited out!".format("Player"))

def get_money():
    '''Give the player money after winning a battle.'''
    pass
    #money_recieved += required_lists.payday_count * Meowth.level (or Purrloin.level)

def check_enemy_health():
    '''Check if the enemy healtlh is > 0, if not, return the next pokemon and give experience.'''
    global enemy_pokemon
    if enemy_pokemon.hp <= 0:
        required_lists.to_do.append("{0} fainted!".format(enemy_pokemon.name))
        required_lists.to_damage.append("NULL")
        enemy_pokemon.faint()
        for i in range(len(enemies.current_enemy.party)):
            if not enemies.current_enemy.party[i].fainted:
                required_lists.to_do.append("{0} sent out {1}!".format(enemies.current_enemy.name, enemies.current_enemy.party[i].name))
                enemy_pokemon = enemies.current_enemy.party[i]
                print(enemy_pokemon.name)
                return 0

        else:
            required_lists.to_do.append("{0} has run out of usable pokemon!".format(required_lists.current_enemy.name))
            get_money()

        player_pokemon.get_exp(enemy_pokemon)
        player_pokemon.get_ev(enemy_pokemon)


