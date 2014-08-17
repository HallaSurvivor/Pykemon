from random import randint

in_battle = True

stage_conversion = [.25, .29, .33, .4, .5, .66, 1, 1.5, 2, 2.5, 3, 3.5, 4]

accuracy_conversion = [.33, .38, .43, .50, .60, .75, 1, 1.33, 1.67, 2, 2.33, 2.67, 3]

nature_list = ["adamant", "bashful", "bold", "brave",
                "calm", "careful", "docile", "gentle",
                "hardy", "hasty", "impish", "jolly",
                "lax", "lonely", "mild", "modest",
                "naive", "naughty", "quiet", "quirky",
                "rash", "relaxed", "sassy", "serious",
                "timid"]

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

class Growth_Rates(object):
    slow = 0
    medium_fast = 1
    fast = 2
    medium_slow = 3
    erratic = 4
    fluctuating = 5

growth_rates = ["slow", "medium fast", "fast", "medium slow", "erratic", "fluctuating"]

stat_list = ["attack", "defense", "special attack", "special defense", "speed"]

class NonVolatile(object):
    burned = 0
    frozen = 1
    paralyzed = 2
    poisoned = 3
    badly_poisoned = 4
    asleep = 5

class Stats(object):
    attack = 0
    defense = 1
    special_attack = 2
    special_defense = 3
    speed = 4

nonvolatile = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep"]

volatile = ["confused", "cursed", "embargo", "encore", "flinch", "healblock", "identification", "infatuation", "nightmare", "partially trapped", "parish song", "seeded", "taunt", "telekenetic levitation", "torment"]

to_do = []

class Style(object):
    NULL = 0
    damage = 1
    modify = 2
    status = 3
    nonvolatile = 4

class Targets(object):
    player = 0
    enemy = 1


class PrintingStuff(object):
    def __init__(self, text, style = Style.NULL, target = object, damage = 0, status = "none", modifier = 0, modified_stat = "none"):
        self.text = text
        self.style = style
        self.target = target
        self.damage = damage
        self.status = status
        self.modifier = modifier
        self.modified_stat = modified_stat

    def cause_damage(self):
        self.target.hp -= self.damage

    def cause_status_ailment(self):
        self.target.status_counter = 1
        self.target.status_nonvolatile = self.status
        print self.target.status_nonvolatile

        if self.status == "badly poisoned":
            self.target.status_counter = 1

        elif self.status == "alseep":
            self.target.status_counter = randint(1, 3)

        print("caused status")

    def cause_status(self):
        self.target.volatile[self.status] = True

        if self.status == "partially trapped":
            self.target.trapped_counter = randint(2, 5)


    def print_text(self):
        global box5data
        box5data = self.text
        if self.style == Style.damage:
            self.cause_damage()

        elif self.style == Style.status:
            self.cause_status()

        elif self.style == Style.nonvolatile:
            self.cause_status_ailment()

        elif self.style == Style.modify:
            if self.target.stages[self.modified_stat] + self.modifier > 6:
                self.target.stages[self.modified_stat] = 6
            elif self.target.stages[self.modified_stat] + self.modifier < -6:
                self.target.stages[self.modified_stat] = -6
            else:
                self.target.stages[self.modified_stat] += self.modifier


box_data = ["Fight", "Bag", "Pokemon", "Run", "", "", "", "", "", ""] #box 1, 2, 3, 4, a, b, c, d, e, f

box5data = "What would you like to do?"

box_colors = [0, 0, 0, 0, 0, 0]

four_boxes = [0, 0, 0, 0]

party_images = [0, 0, 0, 0, 0, 0]

render_stats = -1

back_button = 0

nonvolatile_test_player = False
nonvolatile_test_enemy = False

six_boxes = [0, 0, 0, 0, 0, 0]

payday_count = 0