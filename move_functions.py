'''All of the functions dealing with moves, as well as its overarching class.'''

from random import randint
from random import uniform
from math import floor
import type_chain
import required_lists as r
import printing as p



class Attack(object):

    def __init__(self,

            name = "", pp = 0, pp_max = 0, category = "physical", power = 0,

            move_type = "normal", contact = True, accuracy = 100,

            priority = 0, recoil = 0, modify_list = [0, 0, 0, 0, 0],

            modify_percent = 0, modify_target = "none", status = "none",

            status_percent = 0, status_target = "none", cause_skip = False,

            multiple_attacks = 1, regain_health = False, increased_crit = False,

            payday = False, field_effect = False, cause_enemy_switch = False,

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
        self.status_percent = status_percent
        self.status_target = status_target
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

    def modify_stats(self, user, target):
        '''Modifies stats and prints the change to the screen.'''
        for i in range(5):
                mod = self.modify_list[i]

                if mod > 0:
                    if target.stages[i] == 6:
                        p.add_to_print_buffer("{name}'s {stat} won't go any higher!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target])

                    elif mod == 1:
                        p.add_to_print_buffer("{name}'s {stat} rose!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = 1, modified_stat = i)

                    elif mod == 2:
                        p.add_to_print_buffer("{name}'s {stat} sharply rose!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = 2, modified_stat = i)

                    elif mod == 3:
                        p.add_to_print_buffer("{name}'s {stat} drastically rose!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = 3, modified_stat = i)

                elif mod < 0:
                    if target.stages[i] == -6:
                        p.add_to_print_buffer("{name}'s {stat} won't go any lower!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target])

                    elif mod == -1:
                        p.add_to_print_buffer("{name}'s {stat} fell!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = -1, modified_stat = i)

                    elif mod == -2:
                        p.add_to_print_buffer("{name}'s {stat} harshly fell!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = -2, modified_stat = i)

                    elif mod == -3:
                        p.add_to_print_buffer("{name}'s {stat} drastically fell!".format(name = target.name, stat = r.stat_list[i]), required_pokemon = [user, target], style = r.Style.modify, target = target, modifier = -3, modified_stat = i)


    def cause_status(self, target_position, user, battle_target):
        '''Induces a status effect on the target.'''
        if target_position == "player":
            target = user
        else:
            target = battle_target

        for i in range(len(r.nonvolatile)):
            if self.status == r.nonvolatile[i]:

                if target.status_nonvolatile == "healthy":
                    p.add_to_print_buffer("{pokemon} was {status}".format(pokemon = target.name, status = self.status), required_pokemon = [user, target], style = r.Style.nonvolatile, target = target, status = self.status)
                else:
                    p.add_to_print_buffer("{pokemon} was already {status}".format(pokemon = target.name, status = target.status_nonvolatile), required_pokemon = [user, target])

        for i in range(len(r.volatile)):
            if self.status == r.volatile[i]:
                if target.volatile[self.status] == False:
                    if self.status == "partially trapped":
                        target.caused_bind = self.name
                    if self.status != "flinch":
                       p.add_to_print_buffer("{pokemon} was {status}".format(pokemon = target.name, status = self.status), required_pokemon = [user, target], target = target, style = r.Style.status, status = self.status)
                else:
                    p.add_to_print_buffer("{pokemon} was already {status}".format(pokemon = target.name, status = self.status), required_pokemon = [user, target])


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
            p.add_to_print_buffer("It was super effective!", required_pokemon = [user])
        elif net_type_bonus < 1:
            p.add_to_print_buffer("It was not very effective!", required_pokemon = [user])

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
            p.add_to_print_buffer("It was a critical hit!", required_pokemon = [user])
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
        if "normal" == (user.type1 or user.type2):
            stab = 1.5
        else:
            stab = 1
        if user.type1 != "ghost":
            type_bonus1 = type_chain.type_comparison["normal"][user.type1]
        else:
            type_bonus1 = 1

        if user.type2 != "ghost":
            type_bonus2 = type_chain.type_comparison["normal"][user.type2]
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
        p.add_to_print_buffer("{pokemon} used {move}!".format(pokemon = user.name, move = self.name), required_pokemon = [user])
        use_state = "set last move"

        while use_state != "end":
            #print use_state

            if use_state == "set last move":
                user.previous_move = self
                use_state = "check flinch"


            if use_state == "check flinch":
                if user.volatile["flinch"] == True:
                    p.add_to_print_buffer("{pokemon} flinched!".format(pokemon = user.name), required_pokemon = [user])
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
                p.add_to_print_buffer("{pokemon} hurt itself in its confusion!".format(pokemon = user.name), style = r.Style.damage, target = user, damage = damage, required_pokemon = [user])
                use_state = "end"


            elif use_state == "check status":
                if user.status_nonvolatile == "healthy":
                    use_state = "use move"
                else:
                    if user.status_nonvolatile == "frozen":
                        p.add_to_print_buffer("{pokemon} was frozen and unable to move!".format(pokemon = user.name), required_pokemon = [user])
                        use_state = "end"
                    elif user.status_nonvolatile == "alseep":
                        p.add_to_print_buffer("{pokemon} was sleeping and unable to move!".format(pokemon = user.name), required_pokemon = [user])
                        use_state = "end"
                    elif user.status_nonvolatile == "paralyzed":
                        if user.status_counter == 1:
                            p.add_to_print_buffer("{pokemon} was paralyzed and unable to move!".format(pokemon = user.name), required_pokemon = [user])
                            use_state = "end"

                        else:
                            use_state = "use move"
                    else:
                        use_state = "use move"


            elif use_state == "use move": #put this in battle_mech so that using a move with no PP doesn't waste your turn
                if user.pp_list[user.pp_names[self.name]] > 0:
                    user.calculate_in_battle_stats()
                    target.calculate_in_battle_stats()
                    user.lower_pp(self.name)
                    use_state = "check payday"
                else:
                    p.add_to_print_buffer("{move} has no PP left!".format(move = self.name), required_pokemon = [user])
                    use_state = "end"


            elif use_state == "check payday":
                if self.payday == True:
                    r.payday_count += 1
                use_state = "check accuracy"


            elif use_state == "check accuracy":
                if randint(1, 100) <= P or P == 0:
                    use_state = "check skip turn"

                else:
                    p.add_to_print_buffer("It missed!", required_pokemon = [user])
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
                if self.status_percent == 0:
                    use_state = "modify stats"

                else:
                    if randint(0, 100) <= self.status_percent:
                        self.cause_status(self.status_target, user, target)
                    use_state = "modify stats"


            elif use_state == "modify stats":
                if self.modify_percent != 0:
                    if randint(0, 100) <= self.modify_percent:
                        print("should modify stats")
                        if self.modify_target == "user":
                            self.modify_stats(user, user)
                        elif self.modify_target == "enemy":
                            self.modify_stats(user, target)
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

                    p.add_to_print_buffer("It hit {number} times!".format(number = self.multiple_attacks), required_pokemon = [user])
                    use_state = "cause damage"

                elif self.multiple_attacks > 1:
                    number_attacks = self.multiple_attacks

                    p.add_to_print_buffer("It hit {number} times!".format(number = self.multiple_attacks), required_pokemon = [user])
                    use_state = "cause damage"

                else:
                    number_attacks = 1
                    use_state = "cause damage"


            elif use_state == "cause damage":
                if number_attacks == 1:
                    damage = self.calc_damage(user, target)
                    p.add_to_print_buffer(" ", style = r.Style.damage, target = target, damage = damage, required_pokemon = [user])

                else:
                    for i in range(number_attacks):
                        damage = self.calc_damage(user, target)
                        p.add_to_print_buffer(" ", style = r.Style.damage, target = target, damage = damage, required_pokemon = [user])

                use_state = "calc recoil"

            elif use_state == "calc recoil":
                recoil_damage = self.calc_recoil(damage)
                if recoil_damage != 0:
                    p.add_to_print_buffer("{pokemon} was hurt by recoil!".format(pokemon = user.name), style = r.Style.damage, target = user, damage = recoil_damage, required_pokemon = [user])
                use_state = "check regain health"

            elif use_state == "check regain health":
                if self.regain_health == True:
                    regained_health = int(float(damage) / 2)
                    p.add_to_print_buffer("{pokemon} had its energy drained!".format(pokemon = target.name), style = r.Style.damage, target = user, damage = -regained_health, required_pokemon = [user])
                use_state = "modify status"




class OHKO(Attack): #make OHKO an enclosing if statement in Attack?
    def __init__(self, name, move_type, contact):
        super(OHKO, self).__init__(name = name, pp = 5, pp_max = 8, category = "physical", power = 100, move_type = move_type)
        self.contact = contact

    def use(self, user, target):
        P = 30 + (user.level - target.level)

        r.to_do.append("{0} used {1}!".format(user.name, self.name))
        r.to_damage.append("NULL")

        if randint(1, 100) <= P:
            r.to_do.append("It's a one-hit KO!")
            r.to_damage.append("NULL")
            damage = target.hp

            if user.trainer == "player":
                r.to_damage.append("enemy")
            else:
                r.to_damage.append("player")
            r.to_damage_count.append(damage)

        else:
            r.to_do.append("It missed!")
            r.to_damage.append("NULL")

'''
class TwoTurn(Attack):
    def __init__()
    def use(self, user, target):

        P = int(float(self.accuracy) * float(user.accuracy) / float(target.evasion) )
        r.to_do.append("{0} used {1}!".format(user.name, self.name))
        r.to_damage.append("NULL")

                    r.to_do.append("It hit {0} times!".format(number_attacks))

                damage = calc_damage(user, target, self)

                if user.trainer == "player":
                    r.to_damage.append("enemy")
                else:
                    r.to_damage.append("player")
                r.to_damage_count.append(damage)

            if self.cause_skip == True:
                user.skip_turn = True

    else:
        r.to_do.append("It missed!")
        r.to_damage.append("NULL")
'''







