'''List of functions required to generate a new pokemon.'''
import pokemon_list
import move_list
from random import randint


def choose_iv():
    '''Randomly choose the ivs of a pokemon.'''
    new_iv_hp = randint(0,31)
    new_iv_atk = randint(0, 31)
    new_iv_defs = randint(0, 31)
    new_iv_sp_atk = randint(0, 31)
    new_iv_sp_defs = randint(0, 31)
    new_iv_speed = randint(0, 31)
    return [new_iv_hp, new_iv_atk, new_iv_defs, new_iv_sp_atk, new_iv_sp_defs, new_iv_speed]


def generate(wild_pokemon, moveset = [move_list.poison_powder, move_list.growl, move_list.swords_dance, move_list.tackle], trainer = "wild"):
    '''Generate a pokemon of type wild_pokemon with a movoeset of moveset (list of moves from move_list).'''
    if wild_pokemon == "mudkip":
                            new_pokemon = pokemon_list.Bulbasaur("mudkip", 5, 5, moveset,
                            choose_iv(), trainer)
    elif wild_pokemon == "bulbasaur":
                            new_pokemon = pokemon_list.Bulbasaur("bulbasaur", 5, 5, moveset,
                            choose_iv(), trainer)

    elif wild_pokemon == "ivysaur":
                            new_pokemon = pokemon_list.Ivysaur("ivysaur", 5, 5, moveset, choose_iv(), trainer)
    new_pokemon.get_pp()
    return new_pokemon
