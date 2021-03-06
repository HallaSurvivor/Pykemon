'''The player's party of pokemon.'''
import generator
import move_list


Creighton = generator.generate("bulbasaur",
                               [move_list.confusion, move_list.arm_thrust, move_list.toxic, move_list.hydro_pump],
                               "player")
Creighton.name = "Creighton"

Jessica = generator.generate("bulbasaur",
                             [move_list.swords_dance, move_list.giga_impact, move_list.bind, move_list.absorb],
                             "player")
Jessica.name = "Jessica"

Mary = generator.generate("bulbasaur",
                          [move_list.hyper_beam, move_list.bind, move_list.fire_punch, move_list.take_down], "player")
Mary.name = "Mary"

Jason = generator.generate("mudkip",
                           [move_list.vice_grip, move_list.ice_punch, move_list.fire_punch, move_list.guillotine],
                           "player")
Jason.name = "Jason"

Cameron = generator.generate("ivysaur", [move_list.growl, move_list.tackle, move_list.bite], "player")
Cameron.name = "Cameron"

player_party = [Creighton, Cameron, Jason, Jessica, Mary]
