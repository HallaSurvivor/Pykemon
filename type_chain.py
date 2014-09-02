__author__ = "HallaSurvivor"

# basic array for super effective and not very effective.


normal = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": 1, "ground": 1, "rock": .5, "bug": 1,
          "ghost": 0, "steel": .5, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": 1, "ice": 1,
          "dragon": 1, "dark": 1, "fairy": 1}
fighting = {"none": 1, "normal": 2, "fighting": 1, "flying": .5, "poison": .5, "ground": 1, "rock": 2, "bug": .5,
            "ghost": 0, "steel": 2, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": .5, "ice": 2,
            "dragon": 1, "dark": 2, "fairy": .5}
flying = {"none": 1, "normal": 1, "fighting": 2, "flying": 1, "poison": 1, "ground": 1, "rock": .5, "bug": 2,
          "ghost": 1, "steel": .5, "fire": 1, "water": 1, "grass": 2, "electric": .5, "psychic": 1, "ice": 1,
          "dragon": 1, "dark": 1, "fairy": 1}
poison = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": .5, "ground": .5, "rock": .5, "bug": 1,
          "ghost": .5, "steel": 0, "fire": 1, "water": 1, "grass": 2, "electric": 1, "psychic": 1, "ice": 1,
          "dragon": 1, "dark": 1, "fairy": 2}
ground = {"none": 1, "normal": 1, "fighting": 1, "flying": 0, "poison": 2, "ground": 1, "rock": 2, "bug": .5,
          "ghost": 1, "steel": 2, "fire": 2, "water": 1, "grass": .5, "electric": 2, "psychic": 1, "ice": 1,
          "dragon": 1, "dark": 1, "fairy": 1}
rock = {"none": 1, "normal": 1, "fighting": .5, "flying": 2, "poison": 1, "ground": .5, "rock": 1, "bug": 2, "ghost": 1,
        "steel": .5, "fire": 2, "water": 1, "grass": 1, "electric": 1, "psychic": 1, "ice": 2, "dragon": 1, "dark": 1,
        "fairy": 1}
bug = {"none": 1, "normal": 1, "fighting": .5, "flying": .5, "poison": .5, "ground": 1, "rock": 1, "bug": 1,
       "ghost": .5, "steel": .5, "fire": .5, "water": 1, "grass": 2, "electric": 1, "psychic": 2, "ice": 1, "dragon": 1,
       "dark": 2, "fairy": .5}
ghost = {"none": 1, "normal": 0, "fighting": 1, "flying": 1, "poison": 1, "ground": 1, "rock": 1, "bug": 1, "ghost": 2,
         "steel": .5, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": 2, "ice": 1, "dragon": 1, "dark": .5,
         "fairy": 1}
steel = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": 1, "ground": 1, "rock": 2, "bug": 1, "ghost": 1,
         "steel": .5, "fire": .5, "water": .5, "grass": 1, "electric": .5, "psychic": 1, "ice": 2, "dragon": 1,
         "dark": 1, "fairy": 2}
fire = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": 1, "ground": 1, "rock": .5, "bug": 2, "ghost": 1,
        "steel": 2, "fire": .5, "water": .5, "grass": 2, "electric": 1, "psychic": 1, "ice": 2, "dragon": .5, "dark": 1,
        "fairy": 1}
water = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": 1, "ground": 2, "rock": 2, "bug": 1, "ghost": 1,
         "steel": 1, "fire": 2, "water": .5, "grass": .5, "electric": 1, "psychic": 1, "ice": 1, "dragon": .5,
         "dark": 1, "fairy": 1}
grass = {"none": 1, "normal": 1, "fighting": 1, "flying": .5, "poison": .5, "ground": 2, "rock": 2, "bug": .5,
         "ghost": 1, "steel": .5, "fire": .5, "water": 2, "grass": .5, "electric": 1, "psychic": 1, "ice": 1,
         "dragon": .5, "dark": 1, "fairy": 1}
electric = {"none": 1, "normal": 1, "fighting": 1, "flying": 2, "poison": 1, "ground": 0, "rock": 1, "bug": 1,
            "ghost": 1, "steel": 1, "fire": 1, "water": 2, "grass": .5, "electric": .5, "psychic": 1, "ice": 1,
            "dragon": .5, "dark": 1, "fairy": 1}
psychic = {"none": 1, "normal": 1, "fighting": 2, "flying": 1, "poison": 2, "ground": 1, "rock": 1, "bug": 1,
           "ghost": 1, "steel": .5, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": .5, "ice": 1,
           "dragon": 1, "dark": 0, "fairy": 1}
ice = {"none": 1, "normal": 1, "fighting": 1, "flying": 2, "poison": 1, "ground": 2, "rock": 1, "bug": 1, "ghost": 1,
       "steel": .5, "fire": .5, "water": .5, "grass": 2, "electric": 1, "psychic": 1, "ice": .5, "dragon": 2, "dark": 1,
       "fairy": 1}
dragon = {"none": 1, "normal": 1, "fighting": 1, "flying": 1, "poison": 1, "ground": 1, "rock": 1, "bug": 1, "ghost": 1,
          "steel": .5, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": 1, "ice": 1, "dragon": 2, "dark": 1,
          "fairy": 0}
dark = {"none": 1, "normal": 1, "fighting": .5, "flying": 1, "poison": 1, "ground": 1, "rock": 1, "bug": 1, "ghost": 2,
        "steel": .5, "fire": 1, "water": 1, "grass": 1, "electric": 1, "psychic": 2, "ice": 1, "dragon": 1, "dark": .5,
        "fairy": .5}
fairy = {"none": 1, "normal": 1, "fighting": 2, "flying": 1, "poison": .5, "ground": 1, "rock": 1, "bug": 1, "ghost": 1,
         "steel": .5, "fire": .5, "water": 1, "grass": 1, "electric": 1, "psychic": 1, "ice": 1, "dragon": 2, "dark": 1,
         "fairy": 1}

type_comparison = {"normal": normal, "fighting": fighting, "flying": flying, "poison": poison, "ground": ground,
                   "rock": rock, "bug": bug, "ghost": ghost, "steel": steel, "fire": fire, "water": water,
                   "grass": grass, "electric": electric, "psychic": psychic, "ice": ice, "dragon": dragon, "dark": dark,
                   "fairy": fairy}
