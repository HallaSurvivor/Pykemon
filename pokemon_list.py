__author__ = 'HallaSurvivor'
import pokemon_functions
import images
from random import randint

class Bulbasaur(pokemon_functions.Pokemon):
    def __init__(self, name, level, exp, moveset, iv_list, trainer = "wild", item = "none"):

#base stats
        super(Bulbasaur, self).__init__(

        "overgrow", "grass", "poison",

        "monster", "grass", 21,

        45, 0.7, 6.9, 87.5, "medium slow",

        16, "Ivysaur", 64, [0, 0, 0, 1, 0, 0],

        45, 49, 49, 65, 65, 45,

        ["Tackle"], ["Tackle"], ["Tackle"],

        images.BULBASAUR_BACK, images.BULBASAUR_FRONT, images.GREEN,

        iv_list, name, level, exp, moveset, trainer, item)


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
