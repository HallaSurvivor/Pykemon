'''Handles all of the functions associated with being in a battle.'''
import player_party
import enemies
import required_lists
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

def check_status(pokemon):
    '''Checks the status of a pokemon, and deals damage or decrements a turn counter accordingly.'''
    if pokemon.status_nonvolatile == "burned":
        required_lists.to_print.append("{0} was hurt by burn".format(pokemon.name))
        required_lists.to_damage.append(pokemon.trainer)
        required_lists.to_damage_count.append(int(float(pokemon.hp)) / 8)

    elif pokemon.status_nonvolatile == "frozen":
        if randint(0, 100) <= 20:
            pokemon.status_nonvolatle == "healthy"
            required_lists.to_print.append("{0} has thawed out".format(pokemon.name))
            required_lists.to_damage.append("NULL")

    elif pokemon.status_nonvolatile == "paralyzed":
        if randint(0, 100) <= 25:
            pokemon.status_counter = 1
        else:
            pokemon.status_counter = 0

    elif pokemon.status_nonvolatile == "poisoned":
        required_lists.to_print.append("{0} was hurt by poison".format(pokemon.name))
        required_lists.to_damage.append(pokemon.trainer)
        required_lists.to_damage_count.append(int(float(pokemon.hp)) / 8)

    elif pokemon.status_nonvolatile == "badly poisoned":
        required_lists.to_print.append("{0} was hurt by poison".format(pokemon.name))
        required_lists.to_damage.append(pokemon.trainer)
        required_lists.to_damage_count.append(int(float(pokemon.hp_full)/16*pokemon.status_counter))
        pokemon.status_counter += 1


    elif pokemon.status_nonvolatile == "asleep":
        pokemon.status_counter -= 1
        if pokemon.status_counter == 0:
            pokemon.status_nonvolatile = "healthy"

def check_volatile_status(pokemon):
    '''Handles volatile status ailments and their effects.'''
    if pokemon.volatile["cursed"] == True:
        pass

    if pokemon.volatile["embargo"] == True:
        pass

    if pokemon.volatile["encore"] == True:
        pass

    if pokemon.volatile["flinch"] == True:
        pass

    if pokemon.volatile["healblock"] == True:
        pass

    if pokemon.volatile["identification"] == True:
        pass

    if pokemon.volatile["infatuated"] == True:
        pass

    if pokemon.volatile["nightmare"] == True:
        pass

    if pokemon.volatile["partially trapped"] == True:
        required_lists.to_print.append("{0} was hurt by {1}".format(pokemon.name, "bind")) #make "bind" a general case
        required_lists.to_damage.append(pokemon.trainer)
        required_lists.to_damage_count.append(float(pokemon.hp_full) / 8)

    if pokemon.volatile["parish song"] == True:
        pass

    if pokemon.volatile["seeded"] == True:
        pass

    if pokemon.volatile["taunt"] == True:
        pass

    if pokemon.volatile["telekenetic levitation"] == True:
        pass

    if pokemon.volatile["torment"] == True:
        pass


def use_attack(user, target, move):
    '''Goes through all of the checks to try to use an attack.'''
#status ailments
    if move != 5:
        if user.volatile["confused"] == False:
            if (user.status_nonvolatile != "asleep"):
                if (user.status_nonvolatile != "frozen"):
                    if user.status_nonvolatile == "paralyzed":
                        if user.status_counter == 0: #for paralyzed, status counter is 1 if it can't attack, and 0 if it can

                                    if user.pp_list[move] > 0:
                                        user.moveset[move].use(user, target)
                                        player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(user)
                                        player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(target)
                                        user.pp_list[move] -= 1
                                    else:
                                        required_lists.to_print.append(user.moveset[move].name + " has no PP left")
                                        required_lists.to_damage.append("NULL")

                        else:
                            required_lists.to_print.append("{0} was paralyzed and unable to move!".format(user.name))
                            required_lists.to_damage.append("NULL")

            #use move if not paralyzed
                    else:
                        if user.pp_list[move] > 0:
                            user.moveset[move].use(user, target)
                            user.calculate_in_battle_stats()
                            target.calculate_in_battle_stats()
                            user.pp_list[move] -= 1
                        else:
                            required_lists.to_print.append(user.moveset[move].name + " has no PP left")
                            required_lists.to_damage.append("NULL")

            #print what went wrong due to status ailments
                else:
                    required_lists.to_print.append("{0} was frozen and unable to move!".format(user.name))
                    required_lists.to_damage.append("NULL")
            else:
                required_lists.to_print.append("{0} was sleeping and unable to move!".format(user.name))
                required_lists.to_damage.append("NULL")

        else:
            if randint(0, 1) == 0:
                confused_attack.use(user, user)
                required_lists.to_print.append("{0} hurt itself in its confusion!".format(user.name))
                required_lists.to_damage.append("NULL")
            else:
                if user.pp_list[move] > 0:
                    user.moveset[move].use(user, target)
                    player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(user)
                    player_party.generator.pokemon_list.pokemon_functions.calculate_in_battle_stats(target)
                else:
                    required_lists.to_print.append(user.moveset[move].name + " has no PP left")
                    required_lists.to_damage.append("NULL")


def check_speed(player, enemy, player_choice, enemy_choice):
    '''Compares the speeds of the player and enemy pokemon, and does the faster pokemon's move first.'''
    if player.battle_speed > enemy.battle_speed:
        use_attack(player, enemy, player_choice)
        use_attack(enemy, player, enemy_choice)
    else:
        use_attack(enemy, player, enemy_choice)
        use_attack(player, enemy, player_choice)

def check_player_health(player):
    '''Check if the player hp is > 0, if not, have the user select another pokemon.'''
    if player.hp <= 0:
        required_lists.to_print_immediate.append("{0} feinted!".format(player.name))
        #animation?
        #make this not deal damage to the enemy if he switches and the previous pokemon had a status ailment
        watch_count = 0
        for i in range(len(player_party.player_party)):
            if player_party.player_party[i].hp > 0:
                game_state = "pokemon select"
            else:
                watch_count += 1
        else:
            if watch_count == len(player_party.player_party):
                required_lists.to_print_immediate.append("{0} is out of usable pokemon!".format("Player"))
                required_lists.to_print_immediate.append("{0} whited out!".format("Player"))

def get_money():
    '''Give the player money after winning a battle.'''
    pass

def check_enemy_health(player, enemy):
    '''Check if the enemy healtlh is > 0, if not, return the next pokemon and give experience.'''
    global enemy_pokemon
    if enemy.hp <= 0:
        required_lists.to_print_immediate.append("{0} feinted!".format(enemy.name))
        for i in range(len(required_lists.current_enemy.party)):
            if required_lists.current_enemy.party[i].hp > 0:
                required_lists.to_print_immediate.append("{0} sent out {1}!".format(required_lists.current_enemy.name, required_lists.current_enemy.party[i].name))
                enemy_pokemon = required_lists.current_enemy.party[i]

                to_delete = 0
                for i in range(len(required_lists.to_damage)):
                    if required_lists.to_print[i] == enemy_pokemon.name:
                        del required_lists.to_print[i]
                        del required_lists.to_damage[i]
                        del required_lists.to_damage_count[to_delete]
                    else:
                        to_delete += 1
                break
        else:
            required_lists.to_print_immediate.append("{0} has run out of usable pokemon!")
            get_money()

        player.get_exp(enemy)
        player.get_ev(enemy)
        print player.exp
        print player.ev
        print "\n"


