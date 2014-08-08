'''All of the moves in the game.'''
from move_functions import Attack
from move_functions import OHKO

#name, category, power, move_type, pp full, pp max, contact=True, acc=100, priority=0, recoil=0, user mod=[], enemy mod=[], mod perc=0, status=none
confused_attack = Attack("", "physical", 40, "normal", 10000000, 10000000000)
pound = Attack("pound", "physical", 40, "normal", 35, 56)
karate_chop = Attack("Karate Chop", "physical", 40, "fighting", 25, 50, increased_crit = True)
double_slap = Attack("Double Slap", "physical", 15, "normal", 10, 16, accuracy = 85, multiple_attacks = True)
comet_punch = Attack("Comet Punch", "physical", 18, "normal", 10, 16, accuracy = 85, multiple_attacks = True)
mega_punch = Attack("Mega Punch", "physical", 80, "normal", 20, 32, accuracy = 85)
pay_day = Attack("Pay Day", "physical", 40, "normal", 20, 32)
fire_punch = Attack("Fire Punch", "physical", 75, "fire", 15, 24, status = "burned", stat_percent = 100)
ice_punch = Attack("Ice Punch", "physical", 75, "ice", 15, 24, status = "frozen", stat_percent = 100)
thunder_punch = Attack("Thunder Punch", "physical", 75, "electric", 15, 24, status = "paralyzed", stat_percent = 100)
scratch = Attack("Scratch", "physical", 40, "normal", 35, 56)
vice_grip = Attack("Vice Grip", "physical", 55, "normal", 30, 48)
guillotine = OHKO("Guillotine", "normal", True)
razor_wind = Attack("Razor Wind", "special", 80, "normal", 8, 16, contact = False, accuracy = 85, increased_crit = True) #make this work like fly
swords_dance = Attack("Swords Dance", "status", 0, "normal", 20, 32, contact = False, modify_list = [2, 0, 0, 0, 0], accuracy = 0)
cut = Attack("Cut", "physical", 50, "normal", 30, 48, accuracy = 95) #make better?
gust = Attack("Gust", "special", 50, "flying", 30, 48, contact = False) #double damage on fly/bounce/skydrop
wing_attack = Attack("Wing Attack", "physical", 60, "flying", 35, 56)
whirlwind = Attack("Whirlwind", "status", 0, "normal", 20, 32, contact = False) #roar
fly = Attack("Fly", "physical", 90, "flying", 15, 24, accuracy = 95) #fly
bind = Attack("Bind", "physical", 15, "normal", 20, 32, accuracy = 85, status = "partially trapped", stat_percent = 100) #bind
slam = Attack("Slam", "physical", 80, "normal", 20, 32, accuracy = 75)
vine_whip = Attack("Vine Whip", "physical", 45, "grass", 25, 40)
stomp = Attack("Stomp", "physical", 65, "normal", 20, 32, status = "flinch", stat_percent = 30) #2x damage and no miss if minimize
double_kick = Attack("Double Kick", "physical", 30, "fighting", 3, 48, multiple_attacks = True) #class of moves for multi-strike?
mega_kick = Attack("Mega Kick", "physical", 120, "normal", 5, 8, accuracy = 75)
jump_kick = Attack("Jump Kick", "physical", 100, "fighting", 10, 16, accuracy = 95, recoil = 50) #50% player health, not 50% damage dealt
rolling_kick = Attack("Rolling Kick", "physical", 60, "fighting", 15, 24, accuracy = 85, status = "flinch", stat_percent = 30)
sand_attack = Attack("Sand Attack", "status", 0, "ground", 15, 24) #lowers target accuracy by 1 stage
headbutt = Attack("Headbutt", "physical", 70, "normal", 15, 24, status = "flinch", stat_percent = 30)
horn_attack = Attack("Horn Attack", "physical", 65, "normal", 25, 40)
fury_attack = Attack("Fury Attack", "physical", 15, "normal", 20, 32, multiple_attacks = True, accuracy = 85)
horn_drill = OHKO("Horn Drill", "normal", True)
tackle = Attack("Tackle", "physical", 50, "normal", 35, 56)
body_slam = Attack("Body Slam", "physical", 85, "normal", 15, 24, status = "paralyzed", stat_percent = 30)
wrap = Attack("Wrap", "physical", 15, "normal", 20, 32, status = "partially trapped", stat_percent = 100) #make partially trapped random select 2-5 turns
take_down = Attack("Take Down", "physical", 90, "normal", 20, 32, recoil = 25)
thrash = Attack("Thrash", "physical", 120, "normal", 10, 16) #make class for forced repeated moves
double_edge = Attack("Double Edge", "physical", 120, "normal", 15, 24, recoil = 33)
tail_whip = Attack("Tail Whip", "status", 0, "normal", 30, 48, modify_list = [0, -1, 0, 0, 0], modify_target = "enemy", modify_percent = 100)
poison_sting = Attack("Poison Sting", "physical", 15, "poison", 35, 56, status = "poisoned", stat_percent = 30, contact = False)
twineedle = Attack("Twineedle", "physical", 25, "bug", 20, 32, status = "poisoned", stat_percent = 20, contact = False, multiple_attacks = True)
leer = Attack("Leer", "status", 0, "normal", 30, 48, modify_list = [0, -1, 0, 0, 0], modify_target = "enemy", modify_percent = 100, contact = False)
bite = Attack("Bite", "physical", 60, "dark", 25, 40, status = "flinch", stat_percent = 10)
growl = Attack("Growl", "status", 0, "normal", 40, 52, modify_list = [-1, 0, 0, 0, 0], modify_target = "enemy", contact = False)
#roar = Attack("Roar", "status", )
sing = Attack("Sing", "status", 0, "normal", 15, 24, status = "alseep", contact = False)


poison_powder = Attack("Poison Powder", "status", 0, "poison", 35, 54, contact = False, accuracy = 75, status = "poisoned")
confide = Attack("Confide", "status", 0, "normal", 20, 32, modify_list = [0, 0, -1, 0, 0], modify_target = "enemy", contact = False)

will_o_wisp = Attack("Will-O-Wisp", "status", 0, "fire", 15, 24, status = "burned", accuracy = 85)
toxic = Attack("Toxic", "status", 0, "poison", 10, 16, status = "badly poisoned", accuracy = 90)
dragon_dance = Attack("Dragon Dance", "status", 0, "dragon", 20, 32, modify_list = [1, 0, 0, 0, 1], modify_target = "user", accuracy = 0)
hydro_pump = Attack("Hydro Pump", "special", 110, "water", 5, 8, contact = False, accuracy = 80)
hyper_beam = Attack("Hyper Beam", "special", 150, "normal", 5, 8, contact = False, accuracy = 90, cause_skip = True)
confusion = Attack("Confusion", "special", 50, "psychic", 25, 40, contact = False, status = "confused", stat_percent = 100)
giga_impact = Attack("Giga Impact", "physical", 150, "normal", 5, 8, accuracy = 90, cause_skip = True)
absorb = Attack("Absorb", "special", 20, "grass", 20, 32, contact = False, regain_health = True)
arm_thrust = Attack("Arm Thrust", "physical", 15, "fighting", 20, 32, multiple_attacks = True)