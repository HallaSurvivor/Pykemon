'''All of the functions dealing with moves, as well as its overarching class.'''

from random import randint
from random import uniform
from math import floor
import type_chain
import required_lists



def modify_stats(move, target):
    '''Modifies stats and prints the change to the screen.'''
    #printing
    for i in range(5):

        if move.modify_list[i] == 1:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == 6:
                required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} rose".format(target.name, required_lists.stat_list[i]))

        elif move.modify_list[i] == 2:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == 6:
                required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} sharply rose".format(target.name, required_lists.stat_list[i]))

        elif move.modify_list[i] == 3:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == 6:
                required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} drastically rose".format(target.name, required_lists.stat_list[i]))


        elif move.modify_list[i] == -1:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == -6:
                required_lists.to_print.append("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} fell".format(target.name, required_lists.stat_list[i]))

        elif move.modify_list[i] == -2:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == -6:
                required_lists.to_print.append("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} harshly fell".format(target.name, required_lists.stat_list[i]))

        elif move.modify_list[i] == -3:
            required_lists.to_damage.append("NULL")
            if target.stages[i] == -6:
                required_lists.to_print("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
            else:
                required_lists.to_print.append("{0}'s {1} drastically fell".format(target.name, required_lists.stat_list[i]))

    #calculation
    for i in range(5):
        if target.stages[i] + move.modify_list[i] > 6:
            target.stages[i] = 6
        elif target.stages[i] + move.modify_list[i] < -6:
            target.stages[i] = -6
        else:
            target.stages[i] += move.modify_list[i]



def cause_status(move, target):
    '''Induces a status effect on the target.'''
    for i in range(len(required_lists.nonvolatile)):
        if move.status == required_lists.nonvolatile[i]:
            if target.status_nonvolatile == "healthy":

                target.status_counter = 1 #status_counter is used for a variety of things depending upon the status
                target.status_nonvolatile = move.status
                required_lists.to_print.append("{0} was {1}".format(target.name, move.status))
                if target.trainer =="player":
                    required_lists.to_damage.append("player status")
                else:
                    required_lists.to_damage.append("enemy status")
            else:
                required_lists.to_print.append("{0} is already {1}".format(target.name, target.status_nonvolatile))
                required_lists.to_damage.append("NULL")

    for i in range(len(required_lists.volatile)):
        if move.status == required_lists.volatile[i]:
            if target.volatile[move.status] == False:
                target.volatile[move.status] = True
                required_lists.to_print.append("{0} was {1}".format(target.name, move.status))
                required_lists.to_damage.append("NULL")
            else:
                required_lists.to_print.append("{0} was already {1}".format(target.name, move.status))
                required_lists.to_damage.append("NULL")

    if move.status == "badly poisoned":
        target.status_counter = 1

    elif move.status == "alseep":
        target.status_counter = randint(1, 3)




class Attack(object):

    def __init__(self, name, category, power, move_type, pp_full, pp_max,
                contact = True, accuracy = 100, priority = 0, recoil = 0,
                modify_list = [0, 0, 0, 0, 0],
                modify_percent = 0, modify_target = "user", status = "none", stat_percent = 0,
                cause_skip = False, multiple_attacks = False, regain_health = False, increased_crit = False):

        self.name = name
        self.category = category
        self.power = power
        self.move_type = move_type
        self.pp_full = pp_full
        self.pp_max = pp_max
        self.contact = contact
        self.accuracy = accuracy
        self.priority = priority
        self.recoil = recoil
        self.modify_list = modify_list
        self.modify_perect = modify_percent
        self.modify_target = modify_target
        self.status = status
        self.stat_percent = stat_percent
        self.cause_skip = cause_skip
        self.multiple_attacks = multiple_attacks
        self.regain_health = regain_health
        self.increased_crit = increased_crit



    def calc_recoil(self, damage):
        '''Calculates the recoil that a move will deal to the user.'''
        return int(float(self.recoil)/100*damage)

    def calc_damage(self, user, target):
        '''Calculates the damage of a move.'''
        if self.move_type == (user.type1 or user.type2):
            stab = 1.5
        else:
            stab = 1
        type_bonus1 = type_chain.type_comparison[self.move_type][target.type1]
        type_bonus2 = type_chain.type_comparison[self.move_type][target.type2]
        net_type_bonus = type_bonus1 * type_bonus2
        if net_type_bonus > 1:
            required_lists.to_print.append("It was super effective!")
            required_lists.to_damage.append("NULL")
        elif net_type_bonus < 1:
            required_lists.to_print.append("It was not very effective!")
            required_lists.to_damage.append("NULL")

        crit_stage = user.crit_stage
        if self.increased_crit == True:
            crit_stage += 1

        if crit_stage == 0:
            crit_percent = .0625
        elif crit_stage == 1:
            crit_percent = .125
        elif crit_stage == 2:
            crit_percent = .50
        else:
            crit_percent = 1.00

        if uniform(0, 1) <= crit_percent:
            crit = 1.5
            required_lists.to_print.append("It was a critical hit!")
            required_lists.to_damage.append("NULL")
        else:
            crit = 1


        modifier = stab * net_type_bonus * crit * uniform(.85, 1)
        #implement items, abilities, etc. later

        if self.category == "physical":
            damage_ratio = float(user.battle_atk) / float(target.battle_defs)

        elif self.category == "special":
            damage_ratio = float(user.battle_sp_atk) / float(target.battle_sp_defs)

        damage = int(floor( ( (2 * user.level + 10) * damage_ratio * self.power + 2) * modifier / float(250) ) )
        return damage


    def use(self, user, target):
        P = int(float(self.accuracy) * float(user.accuracy) / float(target.evasion) )
        required_lists.to_print.append("{0} used {1}!".format(user.name, self.name))
        required_lists.to_damage.append("NULL")

        if self.name == "Pay Day":
            required_lists.payday_count += 1

        if randint(1, 100) <= P or P == 0:
            if self.category == "status":
                if self.status != "none":
                    cause_status(self, target)
                else:
                    if self.modify_target == "user":
                        modify_stats(self, user)
                    else:
                        modify_stats(self, target)

            else:
                if self.multiple_attacks == False:
                    number_attacks = 1
                else:
                    if randint(0, 1000) <= 333:
                        number_attacks = 2
                    elif 333 < randint(0, 1000) <= 666:
                        number_attacks = 3
                    elif 666 < randint(0, 1000) <= 833:
                        number_attacks = 4
                    elif 833 < randint(0, 1000) <= 1000:
                        number_attacks = 5
                    for i in range(number_attacks):
                        required_lists.to_print.append("It hit {0} times!".format(number_attacks))

                for i in range(number_attacks):
                    damage = self.calc_damage(user, target)

                    recoil_damage = self.calc_recoil(damage)
                    if user.trainer == "player":
                        required_lists.to_damage.append("enemy")
                    else:
                        required_lists.to_damage.append("player")
                    required_lists.to_damage_count.append(damage)

                    if recoil_damage != 0:
                        required_lists.to_print.append("{0} was hurt by recoil!".format(user.name))
                        required_lists.to_damage_count.append(recoil_damage)
                        required_lists.to_damage.append(user.trainer)

                    if self.modify_perect != 0:
                        if randint(0, 100) <= self.modify_perect:
                            if self.modify_target == "user":
                                modify_stats(self, user)
                            else:
                                modify_stats(self, target)

                    if self.stat_percent != 0:
                        if randint(0, 100) <= self.stat_percent:
                            cause_status(self, target)

                    if self.regain_health == True:
                        regained_health = int(float(damage) / 2)
                        required_lists.to_print.append("{0} had its energy drained".format(target.name))
                        required_lists.to_damage.append(user.trainer)
                        required_lists.to_damage_count.append(-regained_health)

                if self.cause_skip == True:
                    user.skip_turn = True

        else:
            required_lists.to_print.append("It missed!")
            required_lists.to_damage.append("NULL")


class OHKO(Attack):
    def __init__(self, name, move_type, contact):
        super(OHKO, self).__init__(name, "physical", 100, move_type, 5, 8)
        self.contact = contact

    def use(self, user, target):
        P = 30 + (user.level - target.level)

        required_lists.to_print.append("{0} used {1}!".format(user.name, self.name))
        required_lists.to_damage.append("NULL")

        if randint(1, 100) <= P:
            required_lists.to_print.append("It's a one-hit KO!")
            required_lists.to_damage.append("NULL")
            damage = target.hp

            if user.trainer == "player":
                required_lists.to_damage.append("enemy")
            else:
                required_lists.to_damage.append("player")
            required_lists.to_damage_count.append(damage)

        else:
            required_lists.to_print.append("It missed!")
            required_lists.to_damage.append("NULL")

#class TwoTurn(Attack):
#def use(self, user, target):
'''
        P = int(float(self.accuracy) * float(user.accuracy) / float(target.evasion) )
        required_lists.to_print.append("{0} used {1}!".format(user.name, self.name))
        required_lists.to_damage.append("NULL")

                    required_lists.to_print.append("It hit {0} times!".format(number_attacks))

                damage = calc_damage(user, target, self)

                if user.trainer == "player":
                    required_lists.to_damage.append("enemy")
                else:
                    required_lists.to_damage.append("player")
                required_lists.to_damage_count.append(damage)

            if self.cause_skip == True:
                user.skip_turn = True

    else:
        required_lists.to_print.append("It missed!")
        required_lists.to_damage.append("NULL")
'''







