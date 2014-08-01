__author__ = 'HallaSurvivor'
from move_functions import Attack

#name, category, power, move_type, pp full, pp max, contact=True, acc=100, priority=0, recoil=0, user mod=[], enemy mod=[], mod perc=0, status=none
confused_attack = Attack("", "physical", 40, "normal", 10000000, 10000000000)
poison_powder = Attack("Poison Powder", "status", 0, "poison", 35, 54, contact = False, accuracy = 75, status = "poisoned")
confide = Attack("Confide", "status", 0, "normal", 20, 32, modify_list = [0, 0, -1, 0, 0], modify_target = "enemy", contact = False)
growl = Attack("Growl", "status", 0, "normal", 40, 52, modify_list = [-1, 0, 0, 0, 0], modify_target = "enemy", contact = False)
swords_dance = Attack("Swords Dance", "status", 0, "normal", 20, 32, contact = False, modify_list = [2, 0, 0, 0, 0], accuracy = 0)
will_o_wisp = Attack("Will-O-Wisp", "status", 0, "fire", 15, 24, status = "burned", accuracy = 85)
toxic = Attack("Toxic", "status", 0, "poison", 10, 16, status = "badly poisoned", accuracy = 90)
dragon_dance = Attack("Dragon Dance", "status", 0, "dragon", 20, 32, modify_list = [1, 0, 0, 0, 1], modify_target = "user", accuracy = 0)
tackle = Attack("Tackle", "physical", 50, "normal", 35, 56)
fire_punch = Attack("Fire Punch", "physical", 75, "fire", 15, 24, status = "burned", stat_percent = 100)
hydro_pump = Attack("Hydro Pump", "special", 110, "water", 5, 8, contact = False, accuracy = 80)
takedown = Attack("Takedown", "physical", 85, "normal", 24, 32, recoil = 30)
hyper_beam = Attack("Hyper Beam", "special", 150, "normal", 5, 8, contact = False, accuracy = 90, cause_skip = True)
confusion = Attack("Confusion", "special", 50, "psychic", 25, 40, contact = False, status = "confused", stat_percent = 100)
giga_impact = Attack("Giga Impact", "physical", 150, "normal", 5, 8, accuracy = 90, cause_skip = True)
bind = Attack("Bind", "physical", 15, "normal", 20, 32, accuracy = 85, status = "partially trapped", stat_percent = 100)
absorb = Attack("Absorb", "special", 20, "grass", 20, 32, contact = False, regain_health = True)