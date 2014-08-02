__author__ = "HallaSurvivor"

import move_list
from random import randint
from math import floor
import required_lists


class Pokemon(object):

    def calculate_real_stats(self):
            self.hp_full = ((self.iv[0] + (2*self.base_hp)      + (self.ev[0]/4) + 100)*self.level/100 + 10)*required_lists.nature_modifiers[self.nature][0]
            self.hp      = ((self.iv[0] + (2*self.base_hp)      + (self.ev[0]/4) + 100)*self.level/100 + 10)*required_lists.nature_modifiers[self.nature][0]
            self.atk     = ((self.iv[1] + (2*self.base_atk)     + (self.ev[1]/4)      )*self.level/100 +  5)*required_lists.nature_modifiers[self.nature][1]
            self.defs    = ((self.iv[2] + (2*self.base_defs)    + (self.ev[2]/4)      )*self.level/100 +  5)*required_lists.nature_modifiers[self.nature][2]
            self.sp_atk  = ((self.iv[3] + (2*self.base_sp_atk)  + (self.ev[3]/4)      )*self.level/100 +  5)*required_lists.nature_modifiers[self.nature][3]
            self.sp_defs = ((self.iv[4] + (2*self.base_sp_defs) + (self.ev[4]/4)      )*self.level/100 +  5)*required_lists.nature_modifiers[self.nature][4]
            self.speed   = ((self.iv[5] + (2*self.base_speed)   + (self.ev[5]/4)      )*self.level/100 +  5)*required_lists.nature_modifiers[self.nature][5]

    def __init__(self,

    ability, type1, type2,

    egg1, egg2, egg_cycles,

    capture_rate, height, weight, gender_ratio, growth_rate,

    evolution_level, evolution, exp_yield, ev_yield,

    base_hp, base_atk, base_defs, base_sp_atk, base_sp_defs, base_speed,

    TM_list, move_tutor_list, breeding_move_list,

    player_sprite, enemy_sprite, pokedex_color,

    iv_list, name, level, exp, moveset, trainer, item):

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

        self.name = name
        self.level = level
        self.exp = exp
        self.moveset = moveset
        self.nature = required_lists.nature_list[randint(0, 24)]
        print self.name
        print self.nature
        self.trainer = trainer
        self.item = item #held item

        self.status_nonvolatile = "healthy"
        self.volatile = {"confused":False, "cursed":False, "embargo":False,
                        "encore":False, "flinch":False, "healblock":False,
                        "identification":False, "infatuated":False,
                        "nightmare":False, "partially trapped":False,
                        "parish song":False, "seeded":False, "taunt":False,
                        "telekenetic levitation":False, "torment":False
                        }
        self.skip_turn = False
        self.status_counter = 1 #changes depending on status. paralz: can attack or no. frzn/sleep: time to cure. badly poisoned: used to tell what turn of poison to calc damage

        if self.gender_ratio == -1:
            self.gender = "genderless"
        elif randint(1, 100) <= gender_ratio:
            self.gender =  "male"
        else:
            self.gender =  "female"

        if randint(0, 8192) == 1:
            self.shiny = True
        else:
            self.shiny = False

        self.iv = iv_list
        self.ev = [0, 0, 0, 0, 0, 0]
        self.stages = [0, 0, 0, 0, 0, 0]
        self.accuracy_stage = 0
        self.evasion_stage = 0

        self.pp_list = []

        self.calculate_real_stats()

    def calculate_in_battle_stats(self):
        self.battle_atk = int(floor(self.atk * (required_lists.stage_conversion[self.stages[0]+6])))
        self.battle_defs = int(floor(self.defs * (required_lists.stage_conversion[self.stages[1]+6])))
        self.battle_sp_atk = int(floor(self.sp_atk * (required_lists.stage_conversion[self.stages[2]+6])))
        self.battle_sp_defs = int(floor(self.sp_defs * (required_lists.stage_conversion[self.stages[3]+6])))
        self.battle_speed = int(floor(self.speed * (required_lists.stage_conversion[self.stages[4]+6])))
        self.accuracy = required_lists.accuracy_conversion[self.accuracy_stage + 6]
        self.evasion = required_lists.accuracy_conversion[self.evasion_stage + 6]
        if self.status_nonvolatile == "burned":
            self.battle_atk /= 2

    def get_ev(player_self, enemy_self):
        for i in range(6):
            player_self.ev[i] += enemy_self.ev_yield[i]
        calculate_real_stats(player_self)


    def level_up(self):
        self.level += 1
        required_lists.to_print_immediate.append("{0} leveled up!".format(self.name))
        #blit a new box filled with stats
        self.calculate_real_stats


def get_exp(self, enemy_self):
    if self.level < 100:
        #formula for exp gain uses variables from bulbapedia for convenience reasons on my end
        #it's pretty clear what they do from the if statements, though.
        #if you need to know, you can always look it up :)

        if enemy_self.trainer == "wild":
            a = 1
        else:
            a = 1.5

        b = enemy_self.exp_yield

        if self.item == "lucky egg":
            e = 1.5
        else:
            e = 1

        L = enemy_self.level

        if self.item == "exp share":
            s = 2
        else:
            s = 1

        given_exp = a*b*e*L/(7*s) #t is discluded, as there isn't another player to trade with
        given_exp = int(given_exp)
        print "{0} gained {1} experience!".format(self.name, given_exp)
        self.exp += given_exp
        if self.exp >= self.needed_exp:
            level_up(self)



#experience functions
def get_needed_exp(self):
    n = self.level
    exp_type = self.growth_rate

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


def get_pp(self):
    for i in range(len(self.moveset)):
        self.pp_list.append(self.moveset[i].pp_full)


def lower_pp(self, move_name):
    for i in range(len(self.moveset)):
        if move_name == self.moveset[i].name:
            self.pp_list[i] -= 1

def set_volatile_status(self):
    self.cursed = False #loses 1/4 hp_full per turn. can't un-cursed except by switching out
    self.embargo = False #unable to use held items or items for 5 turns
    self.encore = False #repeats last attack for 3 turns
    self.flinch = False #kings rock, razor fang cause flinch.
    self.healblock = False #cannot heal for 5 turns. items can still be used. absorb etc. will deal damage, won't restore health. leftovers negated
    self.identification = False #ghost types can be effected, dark types too
    self.infatuated = False #cannot attack 50% of the time, against all self
    self.nightmare = False #sleeping pkmn loses 1/4 max hp per turn
    self.parish_song = False #after 3 turns, all self who heard parishsong will feint (includes user)
    self.seeded = False #infected pkmn loses 1/8 max hp, opponent is healed by same amount. grass pkmn can't be seeded
    self.taunt = False #taunted pkmn cannot use non damaging moves for 3 turns
    self.telekinetic_levitation = False #immune to ground type, spikes, toxic spikes, and arena traps for 3 turns. All moves hit, regardless of accuracy/evasion, gravity forces False
    self.torment = False #cannot use same move twice in a row. struggle forced every other turn
