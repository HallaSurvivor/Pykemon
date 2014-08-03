'''List of all the npc trainers along with their pokemon.'''
from generator import generate
import move_list

class Enemy(object):
    '''Defines an enemy.'''
    def __init__(self, name, party):
        self.name = name
        self.party = party


enemy1 = Enemy("enemy1",
                [
                generate("bulbasaur", [move_list.toxic, move_list.will_o_wisp, move_list.poison_powder, move_list.poison_powder], "enemy1"),
                generate("bulbasaur", [move_list.confusion, move_list.fire_punch, move_list.dragon_dance, move_list.giga_impact], "enemy1")
                ]

        )
