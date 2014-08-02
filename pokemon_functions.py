__author__ = "HallaSurvivor"

import move_list
from random import randint
from math import floor
import required_lists

class Pokemon(object):
    def __init__(self,

    ability, type1, type2,

    egg1, egg2, egg_cycles,

    capture_rate, height, weight, gender_ratio, growth_rate,

    evolution_level, evolution, exp_yield, ev_yield,

    base_hp, base_atk, base_defs, base_sp_atk, base_sp_defs, base_speed,

    TM_list, move_tutor_list, breeding_move_list,

    player_sprite, enemy_sprite, pokedex_color):

        self.ability = ability
        self.type1 = type1
        self.type2 = type2
        self.egg1 = egg1
        self.egg2 = egg2
        self.egg_cycles = egg_cycles
        self.capture_rate = capture_rate
        self.height = height
        self.weight = weight
        self.gender_ratio = gender_ratio #percent male, if genderless, -1
        self.growth_rate = growth_rate
        self.evolution_level = evolution_level
        self.evolution = evolution
        self.base_hp = base_hp
        self.base_atk = base_atk
        self.base_defs = base_defs
        self.base_sp_atk = base_sp_atk
        self.base_sp_defs = base_sp_defs
        self.base_speed = base_speed
        self.base_happiness = 70
        self.TM_list = TM_list
        self.move_tutor_list = move_tutor_list
        self.breeding_move_list = breeding_move_list
        self.exp_yield = exp_yield
        self.ev_yield = ev_yield
        self.player_sprite = player_sprite
        self.enemy_sprite = enemy_sprite
        self.pokedex_color = pokedex_color

        self.status_nonvolatile = "healthy"

        self.volatile = {"confused":False, "cursed":False, "embargo":False,
                        "encore":False, "flinch":False, "healblock":False,
                        "identification":False, "infatuated":False,
                        "nightmare":False, "partially trapped":False,
                        "parish song":False, "seeded":False, "taunt":False,
                        "telekenetic levitation":False, "torment":False}

        self.skip_turn = False

        self.status_counter = 1 #changes depending on status. paralz: can attack or no. frzn/sleep: time to cure. badly poisoned: used to tell what turn of poison to calc damage
        self.gender = "male"






def calculate_real_stats(pokemon):
        pokemon.hp_full = ((pokemon.iv[0] + (2*pokemon.base_hp)      + (pokemon.ev[0]/4) + 100)*pokemon.level/100 + 10)*required_lists.nature_modifiers[pokemon.nature][0]
        pokemon.hp      = ((pokemon.iv[0] + (2*pokemon.base_hp)      + (pokemon.ev[0]/4) + 100)*pokemon.level/100 + 10)*required_lists.nature_modifiers[pokemon.nature][0]
        pokemon.atk     = ((pokemon.iv[1] + (2*pokemon.base_atk)     + (pokemon.ev[1]/4)      )*pokemon.level/100 +  5)*required_lists.nature_modifiers[pokemon.nature][1]
        pokemon.defs    = ((pokemon.iv[2] + (2*pokemon.base_defs)    + (pokemon.ev[2]/4)      )*pokemon.level/100 +  5)*required_lists.nature_modifiers[pokemon.nature][2]
        pokemon.sp_atk  = ((pokemon.iv[3] + (2*pokemon.base_sp_atk)  + (pokemon.ev[3]/4)      )*pokemon.level/100 +  5)*required_lists.nature_modifiers[pokemon.nature][3]
        pokemon.sp_defs = ((pokemon.iv[4] + (2*pokemon.base_sp_defs) + (pokemon.ev[4]/4)      )*pokemon.level/100 +  5)*required_lists.nature_modifiers[pokemon.nature][4]
        pokemon.speed   = ((pokemon.iv[5] + (2*pokemon.base_speed)   + (pokemon.ev[5]/4)      )*pokemon.level/100 +  5)*required_lists.nature_modifiers[pokemon.nature][5]

def calculate_in_battle_stats(pokemon):
    pokemon.battle_atk = int(floor(pokemon.atk * (required_lists.stage_conversion[pokemon.stages[0]+6])))
    pokemon.battle_defs = int(floor(pokemon.defs * (required_lists.stage_conversion[pokemon.stages[1]+6])))
    pokemon.battle_sp_atk = int(floor(pokemon.sp_atk * (required_lists.stage_conversion[pokemon.stages[2]+6])))
    pokemon.battle_sp_defs = int(floor(pokemon.sp_defs * (required_lists.stage_conversion[pokemon.stages[3]+6])))
    pokemon.battle_speed = int(floor(pokemon.speed * (required_lists.stage_conversion[pokemon.stages[4]+6])))
    pokemon.accuracy = required_lists.accuracy_conversion[pokemon.accuracy_stage + 6]
    pokemon.evasion = required_lists.accuracy_conversion[pokemon.evasion_stage + 6]
    if pokemon.status_nonvolatile == "burned":
        pokemon.battle_atk /= 2

def choose_gender(gender_ratio):
    if gender_ratio == -1:
        return "genderless"
    elif randint(1, 100) <= gender_ratio:
        return "male"
    else:
        return "female"

def choose_shiny(pokemon):
    if randint(0, 8192) == 1:
        pokemon.shiny = True
    else:
        pokemon.shiny = False


def get_ev(player_pokemon, enemy_pokemon):
    for i in range(6):
        player_pokemon.ev[i] += enemy_pokemon.ev_yield[i]
    calculate_real_stats(player_pokemon)


def level_up(pokemon):
    pokemon.level += 1
    calculate_real_stats(pokemon)


def get_exp(pokemon, enemy_pokemon):
    if pokemon.level < 100:
        #formula for exp gain uses variables from bulbapedia for convenience reasons on my end
        #it's pretty clear what they do from the if statements, though.
        #if you need to know, you can always look it up :)

        if enemy_pokemon.trainer == "wild":
            a = 1
        else:
            a = 1.5

        b = enemy_pokemon.exp_yield

        if pokemon.item == "lucky egg":
            e = 1.5
        else:
            e = 1

        L = enemy_pokemon.level

        if pokemon.item == "exp share":
            s = 2
        else:
            s = 1

        given_exp = a*b*e*L/(7*s) #t is discluded, as there isn't another player to trade with
        given_exp = int(given_exp)
        print "{0} gained {1} experience!".format(pokemon.name, given_exp)
        pokemon.exp += given_exp
        if pokemon.exp >= pokemon.needed_exp:
            level_up(pokemon)



#experience functions
def get_needed_exp(pokemon):
    n = pokemon.level
    exp_type = pokemon.growth_rate

    if exp_type == "erratic":
        if n<= 50:
            needed_exp = n**3*(100-n)/50
        elif n<= 68:
            needed_exp = n**3*(150-n)/100
        elif n<= 98:
            needed_exp = n**3*floor(1911-10*n/3)/500
        else:
            needed_exp = n**3*(160-n)/100

    elif exp_type == "fast":
        needed_exp = 4*n**3/5

    elif exp_type == "medium fast":
        n**3

    elif exp_type == "medium slow":
        needed_exp = 6/5*n**3-15*n**2+100*n-140

    elif exp_type == "slow":
        needed_exp = 5*n**3/4

    else: #fluctuating
        if n <= 15:
            needed_exp = n**3*(floor((n+1)/3)+24)/50

        elif n<= 36:
            needed_exp = n**3*(n+14)/50

        else:
            needed_exp = n**3*(floor(n/2)+32)/50

    return needed_exp


def get_pp(pokemon):
    for i in range(len(pokemon.moveset)):
        pokemon.pp_list.append(pokemon.moveset[i].pp_full)


def lower_pp(pokemon, move_name):
    for i in range(len(pokemon.moveset)):
        if move_name == pokemon.moveset[i].name:
            pokemon.pp_list[i] -= 1

def set_volatile_status(pokemon):
    pokemon.cursed = False #loses 1/4 hp_full per turn. can't un-cursed except by switching out
    pokemon.embargo = False #unable to use held items or items for 5 turns
    pokemon.encore = False #repeats last attack for 3 turns
    pokemon.flinch = False #kings rock, razor fang cause flinch.
    pokemon.healblock = False #cannot heal for 5 turns. items can still be used. absorb etc. will deal damage, won't restore health. leftovers negated
    pokemon.identification = False #ghost types can be effected, dark types too
    pokemon.infatuated = False #cannot attack 50% of the time, against all pokemon
    pokemon.nightmare = False #sleeping pkmn loses 1/4 max hp per turn
    pokemon.parish_song = False #after 3 turns, all pokemon who heard parishsong will feint (includes user)
    pokemon.seeded = False #infected pkmn loses 1/8 max hp, opponent is healed by same amount. grass pkmn can't be seeded
    pokemon.taunt = False #taunted pkmn cannot use non damaging moves for 3 turns
    pokemon.telekinetic_levitation = False #immune to ground type, spikes, toxic spikes, and arena traps for 3 turns. All moves hit, regardless of accuracy/evasion, gravity forces False
    pokemon.torment = False #cannot use same move twice in a row. struggle forced every other turn
