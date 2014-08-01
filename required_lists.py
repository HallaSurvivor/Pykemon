stage_conversion = [.25, .29, .33, .4, .5, .66, 1, 1.5, 2, 2.5, 3, 3.5, 4]

accuracy_conversion = [.33, .38, .43, .50, .60, .75, 1, 1.33, 1.67, 2, 2.33, 2.67, 3]


nature_modifiers = {
#nature[hp, atk, def, sp atk, sp def, spd]
#used as multiplier, hp is always 1

                "adamant":[1, 1.1, 1, .9, 1, 1], "bashful":[1, 1, 1, 1, 1, 1],

                "bold":[1, .9, 1.1, 1, 1, 1], "brave":[1, 1.1, 1, 1, 1, .9],

                "calm":[1, .9, 1, 1, 1.1, 1], "careful":[1, 1, 1, .9, 1.1, 1],

                "docile":[1, 1, 1, 1, 1, 1], "gentle":[1, 1, .9, 1, 1.1, 1],

                "hardy":[1, 1, 1, 1, 1, 1], "hasty":[1, 1, .9, 1, 1, 1.1],

                "impish":[1, 1, 1.1, .9, 1, 1], "jolly":[1, 1, 1, .9, 1, 1.1],

                "lax":[1, 1, 1.1, 1, .9, 1], "lonely":[1, 1.1, .9, 1, 1, 1],

                "mild":[1, 1, .9, 1.1, 1, 1], "modest":[1, .9, 1, 1.1, 1, 1],

                "naive":[1, 1, 1, 1, .9, 1.1], "naughty":[1, 1.1, 1, 1, .9, 1],

                "quiet":[1, 1, 1, 1.1, 1, .9], "quirky":[1, 1, 1, 1, 1, 1],

                "rash":[1, 1, 1, 1.1, .9, 1], "relaxed":[1, 1, 1.1, 1, 1, .9],

                "sassy":[1, 1, 1, 1, 1.1, .9], "serious":[1, 1, 1, 1, 1, 1],

                "timid":[1, .9, 1, 1, 1, 1.1]

                }

growth_rates = ["slow", "medium fast", "fast", "medium slow", "erratic", "fluctuating"]

stat_list = ["attack", "defense", "special attack", "special defense", "speed"]

nonvolatile = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep"]

volatile = ["confused", "cursed", "embargo", "encore", "flinch", "healblocK", "identification", "infatuation", "nightmare", "partially trapped", "parish song", "seeded", "taunt", "telekenetic levitation", "torment"]

to_print = []

to_damage = [] #added to every time to_print is added to. calls one of three things: player, enemy, null

to_damage_count = []

to_print_immediate = []