'''List of all pokemon with initialization settings.

Parameters listed below:
    super(YourPokemon, self).__init__(

    "ability", "type1", "type2",

    "egg1", "egg2", egg_cycles,

    capture_rate, height, weight, percent_male, "exp type",

    evolution_level, evolution, exp_drop, ev_drop,

    base_hp, base_atk, base_defs, base_sp_atk, base_sp_defs, base_speed,

    player_sprite, enemy_sprite, pokedex_color,

    iv_list, name, level, exp, moveset, trainer, item)

'''


from pokemon_functions import Pokemon
import images
from random import randint

class Bulbasaur(Pokemon):
    def __init__(self, name, level, exp, moveset, iv_list, trainer = "wild", item = "none"):

        super(Bulbasaur, self).__init__(

        "overgrow", "grass", "poison",

        "monster", "grass", 21,

        45, 0.7, 6.9, 87.5, "medium slow",

        16, "Ivysaur", 64, [0, 0, 0, 1, 0, 0],

        45, 49, 49, 65, 65, 45,

        ["Tackle"], ["Tackle"], ["Tackle"],

        images.BULBASAUR_BACK, images.BULBASAUR_FRONT, images.GREEN,

        iv_list, name, level, exp, moveset, trainer, item)

class Ivysaur(Pokemon):
    def __init__(self, name, level, exp, moveset, iv_list, trainer = "wild", item = "none"):

        super(Ivysaur, self).__init__(

        "overgrow", "grass", "poison",

        "monster", "grass", 21,

        45, 1.0, 13.0, 17.5, "medium slow",

        32, "Venusaur", 142, [0, 0, 0, 1, 1, 0],

        60, 62, 63, 80, 80, 60,

        ["Tackle"], ["Tackle"], ["Tackle"],

        images.IVYSAUR_BACK, images.IVYSAUR_FRONT, images.GREEN,

        iv_list, name, level, exp, moveset, trainer, item)