__author__ = 'HallaSurvivor'
import pokemon_functions
import images
from random import randint

class Bulbasaur(object):
    def __init__(self, name, level, exp, moveset, nature,
                    iv_list):
#base stats
        self.ability = "overgrow"
        self.type1 = "grass"
        self.type2 = "poison"
        self.egg1 = "monster"
        self.egg2 = "grass"
        self.capture_rate = 45
        self.base_happiness = 70
        self.height = 0.7
        self.weight = 6.9
        self.egg_cycles = 21
        self.gender_ratio = 87.5 #percent male
        self.growth_rate = "medium slow"
        self.evolution_level = 16
        self.evolution = "Ivysasur"
        self.base_hp = 45
        self.base_atk = 49
        self.base_defs = 49
        self.base_sp_atk = 65
        self.base_sp_defs = 65
        self.base_speed = 45
        self.move_pool = ["Tackle"]
        self.exp_yield = 64
        self.ev_yield = [0, 0, 0, 1, 0, 0]
        self.player_sprite = images.BULBASAUR_BACK
        self.enemy_sprite = images.BULBASAUR_FRONT
        self.pokedex_color = images.GREEN

#per instance stats
        self.name = name
        self.level = level
        self.exp = exp
        self.moveset = moveset
        self.nature = nature
        self.trainer = "wild"
        self.gender = pokemon_functions.choose_gender(self.gender_ratio)
        self.item = "none" #held item

        self.status_nonvolatile = "healthy"
        self.status_counter = 1 #changes depending on status. paralz: can attack or no. frzn/sleep: time to cure. badly poisoned: used to tell what turn of poison to calc damage


        pokemon_functions.set_volatile_status(self)
        self.skip_turn = False

#iv, ev, and in-battle modifiers
        self.iv = iv_list
        self.ev = [0, 0, 0, 0, 0, 0]
        self.stages = [0, 0, 0, 0, 0, 0]
        self.accuracy_stage = 0
        self.evasion_stage = 0

        pokemon_functions.calculate_real_stats(self) #constant attack based on iv/ev

        pokemon_functions.calculate_in_battle_stats(self) #variable attack based on things like growl

#move PP
        self.pp_list = []

        self.needed_exp = pokemon_functions.get_needed_exp(self)


class Mudkip(object):
    def __init__(self, name, level, exp, moveset, nature,
                    iv_list):
#base stats
        self.ability = "torrent"
        self.type1 = "water"
        self.type2 = "none"
        self.egg1 = "monster"
        self.egg2 = "water1"
        self.capture_rate = 45
        self.base_happiness = 70
        self.height = 0.4
        self.weight = 7.6
        self.egg_cycles = 21
        self.gender_ratio = 87.5 #percent male
        self.growth_rate = "medium slow"
        self.evolution_level = 16
        self.evolution = "Marshtomp"
        self.base_hp = 50
        self.base_atk = 70
        self.base_defs = 50
        self.base_sp_atk = 50
        self.base_sp_defs = 50
        self.base_speed = 40
        self.move_pool = ["Tackle"]
        self.exp_yield = 62
        self.ev_yield = [0, 1, 0, 0, 0, 0]
        self.player_sprite = images.MUDKIP_BACK
        self.enemy_sprite = images.MUDKIP_FRONT
        self.pokedex_color = images.BLUE

#per instance stats
        self.name = name
        self.level = level
        self.exp = exp
        self.moveset = moveset
        self.nature = nature
        self.trainer = "wild"
        self.gender = pokemon_functions.choose_gender(self)
        self.item = "none" #held item

        self.status_nonvolatile = "healthy"
        self.status_counter = 1 #changes depending on status. paralz: can attack or no. frzn/sleep: time to cure. badly poisoned: used to tell what turn of poison to calc damage


        pokemon_functions.set_volatile_status(self)
        self.skip_turn = False

#iv, ev, and in-battle modifiers
        self.iv = iv_list
        self.ev = [0, 0, 0, 0, 0, 0]
        self.stages = [0, 0, 0, 0, 0, 0]
        self.accuracy_stage = 0
        self.evasion_stage = 0

        pokemon_functions.calculate_real_stats(self) #constant attack based on iv/ev

        pokemon_functions.calculate_in_battle_stats(self) #variable attack based on things like growl

#move PP
        self.pp_list = []

        self.needed_exp = pokemon_functions.get_needed_exp(self)
