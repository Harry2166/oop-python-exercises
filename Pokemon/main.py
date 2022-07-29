
import random
from name_and_stuff import name_list, trainer_classes_list, pokemon
import pokemon_typings as pt

'''
create a pokemon-like game in python using oop
https://github.com/yurecouto/PyPokemon
-> WILL HAVE TO ADJUST THE POKEMON_TYPINGS.PY!!!!!!!!!!
-> pokemon class (name, type, hp, stats?, level)
--> have methods here that like simulate a pokemon game (you know what this is bruh)
METHODS:
---> battle ✓
---> do moves
---> heal, items
---> show exp ✓
---> show max exp ✓
---> run away
---> show hp ✓
---> show max hp ✓
ATTRIBUTES:
---> hp (should be same as max hp until it isnt)
---> max hp (random) ✓
---> max exp and exp (random) ✓
---> What kind of pokemon they have (probably have to use a dictionary in order to connect the name and typing) ✓

-> player class
--> so the player would have slots and all those slots would be a pokemon class, respectively
ATTRIBUTES:
---> name (randomly taken from a file full of names)
---> trainer class
---> amount of pokemon
---> catch
--> so will i also have patches of grass that will spawn pokemon???? idk

for the type matchups:

    -> get type1 and type2 for each pokemon
    -> let it run through the functions twice
    -> check if one of them is in there in order to determine the winner of the duel

'''

class Pokemon():

    '''
    This is meant to represent a singular pokemon and its own singular qualities that were adapted from the pokemon games
    '''
    def __init__(self):

        self.max_hp = random.randint(100, 201)
        self.hp = self.max_hp
        self.lvl = random.randint(1, 11)
        self.max_exp = random.randint(100, 201)
        self.exp = 0

        is_shiny = random.randint(1, 8193)
        if is_shiny == 8192:
            self.shiny = True
        self.shiny = False

        self.pokemon = random.choice(list(pokemon.keys()))
        self.types = pokemon.get(self.pokemon)

    def battle(self, opponent_pokemon):
        print(f"{self.pokemon} is duelling against {opponent_pokemon.pokemon}!")

    def show_hp(self):
        print(f'{self.pokemon}: {self.hp}')

    def show_exp(self):
        print(f'{self.pokemon}: {self.exp}')

    def show_max_exp(self):
        print(f'{self.pokemon}: {self.max_exp}')

    def __str__(self):
        return f'{self.pokemon}'
        
class Player():

    '''
    This is meant to represent the players that were adapted from the pokemon games
    '''
    def __init__(self, number_of_pokemon=random.randint(1,6), name = None, trainer_class = None):

        self.number_of_pokemon = number_of_pokemon
        self.name = name
        self.trainer_class = trainer_class

        if name == None:
            self.name = random.choice(name_list)
            self.trainer_class = random.choice(trainer_classes_list)

        self.pokemon_team = list()

        for i in range(number_of_pokemon):
            self.pokemon_team.append(Pokemon())

    def duel(self, opponent_player):

        print(f"{self.name} is duelling against {opponent_player.name}!")

    def __str__(self):

        return f'I am {self.trainer_class} {self.name} and I have {self.number_of_pokemon} pokemon. They are {", ".join(str(v) for v in self.pokemon_team)}.'

def monotype(type1):
    if type1 in pt.types:
        index_monotype = pt.types.index(type1)

        overall_strength = pt.strength[index_monotype]
        overall_weakness = pt.weakness[index_monotype]

        return [overall_strength, overall_weakness]

def dualtype(type1, type2):
    if type1 in pt.types and type2 in pt.types:

        overall_weakness = [] # stores the overall weaknesses of the dual type
        overall_strength = [] # stores the overall strengths of the dual type
        
        resistance_immunities = [] # stores the overall resistances & immunities

        index_dualtype1 = pt.types.index(type1)
        index_dualtype2 = pt.types.index(type2)

        for typing in pt.strength[index_dualtype1]: # loop that adds all strengths from the primary type to the overall strengths list
            overall_strength.append(typing)

        for typing in pt.strength[index_dualtype2]: # loop that adds all strengths from the secondary type to the overall strengths list
            overall_strength.append(typing)

        for typing in pt.weakness[index_dualtype1]: # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing) 

        for typing in pt.weakness[index_dualtype2]: # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing)

        for typing in overall_weakness: # this for loop goes through all typings in the overall_weakness list and checks out the resistances and immunities that each
            if typing in pt.immunities[index_dualtype1] or typing in pt.immunities[index_dualtype2]: # types has. If it is present in the resistances or immunities, then it
                resistance_immunities.append(typing) # would be added to the resistances and immunities list
            elif typing in pt.resistances[index_dualtype1] or typing in pt.resistances[index_dualtype2]:
                resistance_immunities.append(typing)
                
        overall_strength = list((set(overall_strength)))
        overall_weakness = list((set(overall_weakness)) - set(resistance_immunities))

        return [overall_strength, overall_weakness]

# wow = (random.choice(list(pokemon.keys())))
# print(wow)
# print(pokemon.get(wow))

# if len(pokemon.get(wow)) > 1:
#     print(pokemon.get(wow)[0])
#     print(pokemon.get(wow)[-1])

ash = Player(random.randint(1, 6))
gary = Player(random.randint(1, 6))

print(ash)
print(gary)

ash.duel(gary)

print(f'GARY: {gary.number_of_pokemon}')
print(f'ASH: {ash.number_of_pokemon}')

gary_pokemon = gary.pokemon_team[random.randint(0, gary.number_of_pokemon-1)]
ash_pokemon = ash.pokemon_team[random.randint(0, ash.number_of_pokemon-1)]
gary_pokemon.battle(ash_pokemon)

if len(gary_pokemon.types) == 1:
    gary_type_pokemon = monotype(gary_pokemon.types[0])
else:
    gary_type_pokemon = dualtype(gary_pokemon.types[0], gary_pokemon.types[-1])
    
if len(ash_pokemon.types) == 1:
    ash_type_pokemon = monotype(ash_pokemon.types[0])
else:
    ash_type_pokemon = dualtype(ash_pokemon.types[0], ash_pokemon.types[-1])

# for types in ash_type_pokemon[-1]:
#     print(types)

for type in gary_pokemon.types:
    if type in ash_type_pokemon[-1]:
        print(f"{gary.name}'s has won against {ash.name} using a {gary_pokemon} to beat {ash.name}'s {ash_pokemon}!")
        break
    else:
        print(f"{ash.name}'s has won against {gary.name} using a {ash_pokemon} to beat {gary.name}'s {gary_pokemon}!")
        break

# the above logic is currently wrong, will fix soon
