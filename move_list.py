'''All of the moves in the game.'''
from move_functions import Attack
from move_functions import OHKO

pound = Attack(
        name = "pound",
        category = "physical",
        power = 40,
        move_type = "normal",
        pp = 35,
        pp_max = 56)

karate_chop = Attack(
        name = "Karate Chop",
        category = "physical",
        power = 40,
        move_type = "fighting",
        pp = 25,
        pp_max = 50,
        increased_crit = True)

double_slap = Attack(
        name = "Double Slap",
        category = "physical",
        power = 15,
        move_type = "normal",
        pp = 10,
        pp_max = 16,
        accuracy = 85,
        multiple_attacks = True)

comet_punch = Attack(
        name = "Comet Punch",
        category = "physical",
        power = 18,
        move_type = "normal",
        pp = 10,
        pp_max = 16,
        accuracy = 85,
        multiple_attacks = True)

mega_punch = Attack(
        name = "Mega Punch",
        category = "physical",
        power = 80,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        accuracy = 85)

pay_day = Attack(
        name = "Pay Day",
        category = "physical",
        power = 40,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        payday = True)

fire_punch = Attack(
        name = "Fire Punch",
        category = "physical",
        power = 75,
        move_type = "fire",
        pp = 15,
        pp_max = 24,
        status = "burned",
        stat_percent = 10)

ice_punch = Attack(
        name = "Ice Punch",
        category = "physical",
        power = 75,
        move_type = "ice",
        pp = 15,
        pp_max = 24,
        status = "frozen",
        stat_percent = 10)

thunder_punch = Attack(
        name = "Thunder Punch",
        category = "physical",
        power = 75,
        move_type = "electric",
        pp = 15,
        pp_max = 24,
        status = "paralyzed",
        stat_percent = 100)

scratch = Attack(
        name = "Scratch",
        category = "physical",
        power = 40,
        move_type = "normal",
        pp = 35,
        pp_max = 56)

vice_grip = Attack(
        name = "Vice Grip",
        category = "physical",
        power = 55,
        move_type = "normal",
        pp = 30,
        pp_max = 48)

guillotine = OHKO(
        name = "Guillotine",
        move_type = "normal",
        contact = True)

razor_wind = Attack(
        name = "Razor Wind",
        category = "special",
        power = 80,
        move_type = "normal",
        pp = 8,
        pp_max = 16,
        contact = False,
        accuracy = 85,
        increased_crit = True) #make this work like fly

swords_dance = Attack(
        name = "Swords Dance",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        contact = False,
        modify_percent = 100,
        modify_list = [2, 0, 0, 0, 0],
        accuracy = 0)

cut = Attack(
        name = "Cut",
        category = "physical",
        power = 50,
        move_type = "normal",
        pp = 30,
        pp_max = 48,
        accuracy = 95,
        field_effect = True) #make better?

gust = Attack(
        name = "Gust",
        category = "special",
        power = 50,
        move_type = "flying",
        pp = 30,
        pp_max = 48,
        contact = False) #double damage on fly/bounce/skydrop

wing_attack = Attack(
        name = "Wing Attack",
        category = "physical",
        power = 60,
        move_type = "flying",
        pp = 35,
        pp_max = 56)

whirlwind = Attack(
        name = "Whirlwind",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        contact = False,
        cause_enemy_switch = True)

fly = Attack(
        name = "Fly",
        category = "physical",
        power = 90,
        move_type = "flying",
        pp = 15,
        pp_max = 24,
        accuracy = 95,
        field_effect = True) #fly

bind = Attack(
        name = "Bind",
        category = "physical",
        power = 15,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        accuracy = 85,
        status = "partially trapped",
        stat_percent = 100)

slam = Attack(
        name = "Slam",
        category = "physical",
        power = 80,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        accuracy = 75)

vine_whip = Attack(
        name = "Vine Whip",
        category = "physical",
        power = 45,
        move_type = "grass",
        pp = 25,
        pp_max = 40)

stomp = Attack(
        name = "Stomp",
        category = "physical",
        power = 65,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        status = "flinch",
        stat_percent = 30) #2x damage and no miss if minimize

double_kick = Attack(
        name = "Double Kick",
        category = "physical",
        power = 30,
        move_type = "fighting",
        pp = 30,
        pp_max = 48,
        multiple_attacks = True)

mega_kick = Attack(
        name = "Mega Kick",
        category = "physical",
        power = 120,
        move_type = "normal",
        pp = 5,
        pp_max = 8,
        accuracy = 75)

jump_kick = Attack(
        name = "Jump Kick",
        category = "physical",
        power = 100,
        move_type = "fighting",
        pp = 10,
        pp_max = 16,
        accuracy = 95,
        recoil = 50) #recoil is 50% player health, not 50% damage dealt

rolling_kick = Attack(
        name = "Rolling Kick",
        category = "physical",
        power = 60,
        move_type = "fighting",
        pp = 15,
        pp_max = 24,
        accuracy = 85,
        status = "flinch",
        stat_percent = 30)

sand_attack = Attack(
        name = "Sand Attack",
        category = "status",
        move_type = "ground",
        pp = 15,
        pp_max = 24) #lowers target accuracy by 1 stage

headbutt = Attack(
        name = "Headbutt",
        category = "physical",
        power = 70,
        move_type = "normal",
        pp = 15,
        pp_max = 24,
        status = "flinch",
        stat_percent = 30) #field effect?

horn_attack = Attack(
        name = "Horn Attack",
        category = "physical",
        power = 65,
        move_type = "normal",
        pp = 25,
        pp_max = 40)

fury_attack = Attack(
        name = "Fury Attack",
        category = "physical",
        power = 15,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        multiple_attacks = True,
        accuracy = 85)

horn_drill = OHKO(
        name = "Horn Drill",
        move_type = "normal",
        contact = True)

tackle = Attack(
        name = "Tackle",
        category = "physical",
        power = 50,
        move_type = "normal",
        pp = 35,
        pp_max = 56)

body_slam = Attack(
        name = "Body Slam",
        category = "physical",
        power = 85,
        move_type = "normal",
        pp = 15,
        pp_max = 24,
        status = "paralyzed",
        stat_percent = 30)

wrap = Attack(
        name = "Wrap",
        category = "physical",
        power = 15,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        status = "partially trapped",
        stat_percent = 100)

take_down = Attack(
        name = "Take Down",
        category = "physical",
        power = 90,
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        recoil = 25)

thrash = Attack(
        name = "Thrash",
        category = "physical",
        power = 120,
        move_type = "normal",
        pp = 10,
        pp_max = 16) #forced repetition

double_edge = Attack(
        name = "Double Edge",
        category = "physical",
        power = 120,
        move_type = "normal",
        pp = 15,
        pp_max = 24,
        recoil = 33)

tail_whip = Attack(
        name = "Tail Whip",
        category = "status",
        move_type = "normal",
        pp = 30,
        pp_max = 48,
        modify_list = [0, -1, 0, 0, 0],
        modify_target = "enemy",
        modify_percent = 100)

poison_sting = Attack(
        name = "Poison Sting",
        category = "physical",
        power = 15,
        move_type = "poison",
        pp = 35,
        pp_max = 56,
        status = "poisoned",
        stat_percent = 30,
        contact = False)

twineedle = Attack(
        name = "Twineedle",
        category = "physical",
        power = 25,
        move_type = "bug",
        pp = 20,
        pp_max = 32,
        status = "poisoned",
        stat_percent = 20,
        contact = False,
        multiple_attacks = True)

leer = Attack(
        name = "Leer",
        category = "status",
        move_type = "normal",
        pp = 30,
        pp_max = 48,
        modify_list = [0, -1, 0, 0, 0],
        modify_target = "enemy",
        modify_percent = 100,
        contact = False)

bite = Attack(
        name = "Bite",
        category = "physical",
        power = 60,
        move_type = "dark",
        pp = 25,
        pp_max = 40,
        status = "flinch",
        stat_percent = 100)

growl = Attack(
        name = "Growl",
        category = "status",
        move_type = "normal",
        pp = 40,
        pp_max = 52,
        modify_list = [-1, 0, 0, 0, 0],
        modify_target = "enemy",
        contact = False,
        modify_percent = 100)

roar = Attack(
        name = "Roar",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        accuracy = 0,
        cause_enemy_switch = True,
        sound_based = True,
        priority = -6) #make cause enemy switch work


sing = Attack(
        name = "Sing",
        category = "status",
        move_type = "normal",
        pp = 15,
        pp_max = 24,
        status = "alseep",
        contact = False,
        sound_based = True)

supersonic = Attack(
        name = "Supersonic",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        accuracy = 55,
        contact = False,
        sound_based = True,
        status = "confused",
        stat_percent = 100)

sonic_boom = Attack(
        name = "Sonic Boom",
        category = "special",
        move_type = "normal",
        power = 20,
        set_damage = True,
        pp = 20,
        pp_max = 32,
        accuracy = 90,
        contact = False) #make set damage work

disable = Attack(
        name = "Disable",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        contact = False,
        cause_disable = True) #make this work

acid = Attack(
        name = "Acid",
        category = "special",
        move_type = "poison",
        pp = 30,
        pp_max = 48,
        power = 40,
        contact = False,
        modify_list = [0, -1, 0, 0, 0],
        modify_target = "enemy",
        modify_percent = 10)

ember = Attack(
        name = "Ember",
        category = "special",
        move_type = "fire",
        power = 40,
        pp = 25,
        pp_max = 40,
        contact = False,
        status = "burned",
        stat_percent = 10)

flamethrower = Attack(
        name = "Flamethrower",
        category = "special",
        move_type = "fire",
        power = 90,
        pp = 15,
        pp_max = 24,
        contact = False,
        status = "burned",
        stat_percent = 10)

mist = Attack() #make this do things



#=====

poison_powder = Attack(
        name = "Poison Powder",
        category = "status",
        move_type = "poison",
        pp = 35,
        pp_max = 54,
        contact = False,
        accuracy = 75,
        status = "poisoned",
        stat_percent = 100)

confide = Attack(
        name = "Confide",
        category = "status",
        move_type = "normal",
        pp = 20,
        pp_max = 32,
        modify_list = [0, 0, -1, 0, 0],
        modify_target = "enemy",
        contact = False)

will_o_wisp = Attack(
        name = "Will-O-Wisp",
        category = "status",
        move_type = "fire",
        pp = 15,
        pp_max = 24,
        status = "burned",
        accuracy = 85,
        stat_percent = 100)

toxic = Attack(
        name = "Toxic",
        category = "status",
        move_type = "poison",
        pp = 10,
        pp_max = 16,
        status = "badly poisoned",
        accuracy = 90,
        stat_percent = 100)

dragon_dance = Attack(
        name = "Dragon Dance",
        category = "status",
        move_type = "dragon",
        pp = 20,
        pp_max = 32,
        modify_list = [1, 0, 0, 0, 1],
        modify_target = "user",
        modify_percent = 100,
        accuracy = 0)

hydro_pump = Attack(
        name = "Hydro Pump",
        category = "special",
        power = 110,
        move_type = "water",
        pp = 5,
        pp_max = 8,
        contact = False,
        accuracy = 80)

hyper_beam = Attack(
        name = "Hyper Beam",
        category = "special",
        power = 150,
        move_type = "normal",
        pp = 5,
        pp_max = 8,
        contact = False,
        accuracy = 90,
        cause_skip = True)

confusion = Attack(
        name = "Confusion",
        category = "special",
        power = 50,
        move_type = "psychic",
        pp = 25,
        pp_max = 40,
        contact = False,
        status = "confused",
        stat_percent = 100)

giga_impact = Attack(
        name = "Giga Impact",
        category = "physical",
        power = 150,
        move_type = "normal",
        pp = 5,
        pp_max = 8,
        accuracy = 90,
        cause_skip = True)

absorb = Attack(
        name = "Absorb",
        category = "special",
        power = 20,
        move_type = "grass",
        pp = 20,
        pp_max = 32,
        contact = False,
        regain_health = True)

arm_thrust = Attack(
        name = "Arm Thrust",
        category = "physical",
        power = 15,
        move_type = "fighting",
        pp = 20,
        pp_max = 32,
        multiple_attacks = True)