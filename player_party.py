'''The player's party of pokemon.'''
import generator
import move_list


Creighton = generator.generate("bulbasaur", [move_list.confusion, move_list.tackle, move_list.toxic, move_list.hydro_pump], "player")
Creighton.name = "Creighton"

Jessica = generator.generate("bulbasaur", [move_list.swords_dance, move_list.giga_impact, move_list.toxic, move_list.absorb], "player")
Jessica.name ="Jessica"

Mary = generator.generate("bulbasaur", [move_list.hyper_beam, move_list.bind, move_list.fire_punch, move_list.takedown], "player")
Mary.name = "Mary"

Jason = generator.generate("mudkip", [move_list.absorb, move_list.hydro_pump, move_list.dragon_dance], "player")
Jason.name = "Jason"

player_party = [Mary, Creighton, Jessica, Jason]
