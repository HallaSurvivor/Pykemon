'''All of the functions dealing with moves, as well as its overarching class.'''

from random import randint
from random import uniform
from math import floor
import type_chain
import required_lists



class Attack(object):

    def __init__(self,

            name = "", pp = 0, pp_max = 0, category = "physical", power = 0,

            move_type = "normal", contact = True, accuracy = 100,

            priority = 0, recoil = 0, modify_list = [0, 0, 0, 0, 0],

            modify_percent = 0, modify_target = "none", status = "none",

            stat_percent = 0, cause_skip = False, multiple_attacks = 1,

            regain_health = False, increased_crit = False, payday = False,

            field_effect = False, cause_enemy_switch = False,

            cause_player_switch = False, sound_based = False,

            set_damage = False, cause_disable = False, fix_move = False):

        self.name = name
        self.pp_full = pp
        self.pp_max = pp_max
        self.category = category
        self.power = power
        self.move_type = move_type
        self.contact = contact
        self.accuracy = accuracy
        self.priority = priority
        self.recoil = recoil
        self.modify_list = modify_list
        self.modify_percent = modify_percent
        self.modify_target = modify_target
        self.status = status
        self.stat_percent = stat_percent
        self.cause_skip = cause_skip
        self.multiple_attacks = multiple_attacks #0 if random between 2 and 5
        self.regain_health = regain_health
        self.increased_crit = increased_crit
        self.payday = payday
        self.field_effect = field_effect
        self.cause_enemy_switch = cause_enemy_switch
        self.cause_player_switch = cause_player_switch
        self.sound_based = sound_based
        self.set_damage = set_damage
        self.cause_disable = cause_disable
        self.fix_move = fix_move

    def modify_stats(self, target):
        '''Modifies stats and prints the change to the screen.'''
        #printing
        print "called modify stats"
        for i in range(5):
            if self.modify_list[i] == 1:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == 6:
                    required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} rose".format(target.name, required_lists.stat_list[i]))

            elif self.modify_list[i] == 2:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == 6:
                    required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} sharply rose".format(target.name, required_lists.stat_list[i]))

            elif self.modify_list[i] == 3:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == 6:
                    required_lists.to_print.append("{0}'s {1} won't go any higher!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} drastically rose".format(target.name, required_lists.stat_list[i]))


            elif self.modify_list[i] == -1:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == -6:
                    required_lists.to_print.append("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} fell".format(target.name, required_lists.stat_list[i]))

            elif self.modify_list[i] == -2:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == -6:
                    required_lists.to_print.append("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} harshly fell".format(target.name, required_lists.stat_list[i]))

            elif self.modify_list[i] == -3:
                required_lists.to_damage.append("NULL")
                if target.stages[i] == -6:
                    required_lists.to_print("{0}'s {1} won't go any lower!".format(target.name, required_lists.stat_list[i]))
                else:
                    required_lists.to_print.append("{0}'s {1} drastically fell".format(target.name, required_lists.stat_list[i]))

        #calculation
        for i in range(5):
            if target.stages[i] + self.modify_list[i] > 6:
                target.stages[i] = 6
            elif target.stages[i] + self.modify_list[i] < -6:
                target.stages[i] = -6
            else:
                target.stages[i] += self.modify_list[i]


    def cause_status(self, target):
        '''Induces a status effect on the target.'''
        for i in range(len(required_lists.nonvolatile)):
            if self.status == required_lists.nonvolatile[i]:
                if target.status_nonvolatile == "healthy":

                    target.status_counter = 1 #status_counter is used for a variety of things depending upon the status
                    target.status_nonvolatile = self.status
                    required_lists.to_print.append("{0} was {1}".format(target.name, self.status))
                    if target.trainer =="player":
                        required_lists.to_damage.append("player status")
                    else:
                        required_lists.to_damage.append("enemy status")
                else:
                    required_lists.to_print.append("{0} is already {1}".format(target.name, target.status_nonvolatile))
                    required_lists.to_damage.append("NULL")

        for i in range(len(required_lists.volatile)):
            if self.status == required_lists.volatile[i]:
                if target.volatile[self.status] == False:
                    target.volatile[self.status] = True
                    if self.status != "flinch":
                        required_lists.to_print.append("{0} was {1}".format(target.name, self.status))
                        required_lists.to_damage.append("NULL")
                else:
                    required_lists.to_print.append("{0} was already {1}".format(target.name, self.status))
                    required_lists.to_damage.append("NULL")

        if self.status == "badly poisoned":
            target.status_counter = 1

        if self.status == "partially trapped":
            target.trapped_counter = randint(2, 5)

        elif self.status == "alseep":
            target.status_counter = randint(1, 3)


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


    def calc_recoil(self, damage):
        '''Calculates the recoil that a move will deal to the user.'''
        return int(float(self.recoil)/100*damage)

    def calc_confused_damage(self, user):
        '''Calculates the damage if the user is confused and hits istelf.'''
        if self.move_type == (user.type1 or user.type2):
            stab = 1.5
        else:
            stab = 1
        if user.type1 != "ghost":
            type_bonus1 = type_chain.type_comparison[self.move_type][user.type1]
        else:
            type_bonus1 = 1

        if user.type2 != "ghost":
            type_bonus2 = type_chain.type_comparison[self.move_type][user.type2]
        else:
            type_bonus2 = 1

        net_type_bonus = type_bonus1 * type_bonus2

        if user.crit_stage == 0:
            crit_percent = .0625
        elif user.crit_stage == 1:
            crit_percent = .125
        elif uesr.crit_stage == 2:
            crit_percent = .50
        else:
            crit_percent = 1.00

        if uniform(0, 1) <= crit_percent:
            crit = 1.5
        else:
            crit = 1


        modifier = stab * net_type_bonus * crit * uniform(.85, 1)
        damage_ratio = float(user.battle_atk) / float(user.battle_defs)

        damage = int(floor( ( (2 * user.level + 10) * damage_ratio * 40 + 2) * modifier / float(250) ) )
        return damage


    def use(self, user, target):
        P = int(float(self.accuracy) * float(user.accuracy) / float(target.evasion) )
        required_lists.to_print.append("{0} used {1}!".format(user.name, self.name))
        required_lists.to_damage.append("NULL")
        use_state = "set last move"

        while use_state != "end":
            print use_state

            if use_state == "set last move":
                user.previous_move = self
                use_state = "check flinch"
            if use_state == "check flinch":
                if user.volatile["flinch"] == True:
                    print "user flinched"
                    required_lists.to_print.append("{0} flinched!".format(user.name))
                    required_lists.to_damage.append("NULL")
                    user.volatile["flinch"] = False
                    use_state = "end"
                else:
                    use_state = "check confusion"


            if use_state == "check confusion":
                if user.volatile["confused"] == False:
                    use_state = "check status"
                else:
                    if randint(0, 1) == 0:
                        use_state = "check status"
                    else:
                        use_state = "use confused move"

            elif use_state == "use confused move":
                damage = self.calc_confused_damage(user)
                required_lists.to_print.append("{0} hurt itself in its confusion!".format(user.name))
                required_lists.to_damage.append("NULL")
                required_lists.to_print.append("")
                required_lists.to_damage.append(user.trainer)
                required_lists.to_damage_count.append(damage)
                use_state = "end"


            elif use_state == "check status":
                if user.status_nonvolatile == "healthy":
                    use_state = "use move"
                else:
                    if user.status_nonvolatile == "frozen":
                        required_lists.to_print.append("{0} was frozen and unable to move!".format(user.name))
                        required_lists.to_damage.append("NULL")
                        use_state = "end"
                    elif user.status_nonvolatile == "alseep":
                        required_lists.to_print.append("{0} was sleeping and unable to move!".format(user.name))
                        required_lists.to_damage.append("NULL")
                        use_state = "end"
                    elif user.status_nonvolatile == "paralyzed":
                        if user.status_counter == 1:
                            required_lists.to_print.append("{0} was paralyzed and unable to move!".format(user.name))
                            required_lists.to_damage.append("NULL")
                            use_state = "end"

                        else:
                            use_state = "use move"
                    else:
                        use_state = "use move"


            elif use_state == "use move":
                if user.pp_list[user.pp_names[self.name]] > 0: #Figure out how to tell which spot in the list the attack is
                    user.calculate_in_battle_stats()
                    target.calculate_in_battle_stats()
                    user.lower_pp(self.name)
                    use_state = "check payday"
                else:
                    required_lists.to_print.append(self.name + " has no PP left")
                    required_lists.to_damage.append("NULL")
                    use_state = "end"


            elif use_state == "check payday":
                if self.payday == True:
                    required_lists.payday_count += 1
                use_state = "check accuracy"


            elif use_state == "check accuracy":
                if randint(1, 100) <= P or P == 0:
                    use_state = "check skip turn"

                else:
                    required_lists.to_print.append("It missed!")
                    required_lists.to_damage.append("NULL")
                    use_state = "end"


            elif use_state == "check skip turn":
                if self.cause_skip == True:
                    user.skip_turn = True
                use_state = "check category"


            elif use_state == "check category":
                if self.category == "status":
                    use_state = "modify status"
                else:
                    use_state = "attack stuff"


            elif use_state == "modify status":
                if self.stat_percent == 0:
                    use_state = "modify stats"

                else:
                    if randint(0, 100) <= self.stat_percent:
                        self.cause_status(target)
                        print"causd status"
                    use_state = "modify stats"


            elif use_state == "modify stats":
                if self.modify_percent != 0:
                    if randint(0, 100) <= self.modify_percent:
                        print "should modify stats"
                        if self.modify_target == "user":
                            self.modify_stats(user)
                        elif self.modify_target == "enemy":
                            self.modify_stats(target)
                use_state = "end"



            elif use_state == "attack stuff":
                if self.multiple_attacks == 0:
                    if randint(0, 1000) <= 333:
                        number_attacks = 2
                    elif 333 < randint(0, 1000) <= 666:
                        number_attacks = 3
                    elif 666 < randint(0, 1000) <= 833:
                        number_attacks = 4
                    elif 833 < randint(0, 1000) <= 1000:
                        number_attacks = 5

                    required_lists.to_print.append("It hit {0} times!".format(number_attacks))
                    required_lists.to_damage.append("NULL")
                    use_state = "cause damage"

                elif self.multiple_attacks > 1:
                    number_attacks = self.multiple_attacks

                    required_lists.to_print.append("It hit {0} times!".format(number_attacks))
                    required_lists.to_damage.append("NULL")
                    use_state = "cause damage"

                else:
                    number_attacks = 1
                    use_state = "cause damage"


            elif use_state == "cause damage":
                if number_attacks == 1:
                    damage = self.calc_damage(user, target)
                    required_lists.to_print.append("")
                    required_lists.to_damage.append(target.trainer)
                    required_lists.to_damage_count.append(damage)

                else:
                    for i in range(number_attacks):
                        damage = self.calc_damage(user, target)
                        required_lists.to_print.append("")
                        required_lists.to_damage.append(target.trainer)
                        required_lists.to_damage_count.append(damage)

                use_state = "calc recoil"

            elif use_state == "calc recoil":
                recoil_damage = self.calc_recoil(damage)
                if recoil_damage != 0:
                    required_lists.to_print.append("{0} was hurt by recoil!".format(user.name))
                    required_lists.to_damage_count.append(recoil_damage)
                    required_lists.to_damage.append(user.trainer)
                use_state = "check regain health"

            elif use_state == "check regain health":
                if self.regain_health == True:
                    regained_health = int(float(damage) / 2)
                    required_lists.to_print.append("{0} had its energy drained".format(target.name))
                    required_lists.to_damage.append(user.trainer)
                    required_lists.to_damage_count.append(-regained_health)
                use_state = "modify status"




class OHKO(Attack): #make OHKO an enclosing if statement in Attack?
    def __init__(self, name, move_type, contact):
        super(OHKO, self).__init__(name = name, pp = 5, pp_max = 8, category = "physical", power = 100, move_type = move_type)
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

'''
class TwoTurn(Attack):
    def __init__()
    def use(self, user, target):

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







