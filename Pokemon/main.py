
import random
from name_and_stuff import name_list, trainer_classes_list, pokemon
import pokemon_typings as pt

'''
create a pokemon-like game in python using oop
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
        self.fainted = False

    def battle(self, opponent_pokemon):
        print(f"{self.pokemon} is duelling against {opponent_pokemon.pokemon}!")

    def show_hp(self):
        print(f'{self.pokemon}: {self.hp}')

    def show_exp(self):
        print(f'{self.pokemon}: {self.exp}')

    def show_max_exp(self):
        print(f'{self.pokemon}: {self.max_exp}')

    def type_weaknesses(self):
        if len(self.types) == 1:
            return monotype(self.types[0])[-1]
        else:
            return dualtype(self.types[0], self.types[-1])[-1]

    def type_strengths(self):
        if len(self.types) == 1:
            return monotype(self.types[0])[0]
        else:
            return dualtype(self.types[0], self.types[-1])[0]

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

    def start_duel(self, opponent_player):

        print(f"{self.name} is duelling against {opponent_player.name}!")
        print(f"{self.name.upper()}'s POKEMON: {self.number_of_pokemon}")
        print(f"{opponent_player.name.upper()}'s POKEMON: {opponent_player.number_of_pokemon}")

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

ash = Player(random.randint(1, 6))
gary = Player(random.randint(1, 6))

print(ash)
print(gary)

ash.start_duel(gary)

gary_pokemon = gary.pokemon_team[random.randint(0, gary.number_of_pokemon-1)]
ash_pokemon = ash.pokemon_team[random.randint(0, ash.number_of_pokemon-1)]
gary_pokemon.battle(ash_pokemon)

# create a function or method that can handle all the pokemon fighting [i guess just with the one with the type advantage is the one that wins to make things easy]
def pokemon_battle(trainer1: Player, trainer2: Player):

    '''
    - This will go on until there is no more pokemon on one side
    - Whoever has the type advantage will win for simplicity sake
    - Will have to remove the selected pokemon from the list of available pokemon
    - While True loop obviously
    - will have to use the .type_weakness and .type_strengths for this
    '''
    while True:

        print(trainer1)
        print(trainer2)

        trainer1_random_index = random.randint(0, trainer1.number_of_pokemon-1)
        trainer2_random_index = random.randint(0, trainer2.number_of_pokemon-1)

        trainer1_pokemon = trainer1.pokemon_team[trainer1_random_index]
        trainer2_pokemon = trainer2.pokemon_team[trainer2_random_index]

        print(f"{trainer1.name} sent out {trainer1_pokemon}!")
        print(f"{trainer2.name} sent out {trainer2_pokemon}!")

        one_on_one = []

        one_on_one.append(trainer1_pokemon)
        one_on_one.append(trainer2_pokemon)

        trainer1.pokemon_team.pop(trainer1_random_index)
        trainer1.number_of_pokemon -= 1
        trainer2.pokemon_team.pop(trainer2_random_index)
        trainer2.number_of_pokemon -= 1

        first_move = random.randrange(0,2) # will use this instead of speed stat because I'm lazy
        second_move = 0 if first_move == 1 else 1

        for type in one_on_one[first_move].types:
            strengths = one_on_one[second_move].type_strengths()
            weaknesses = one_on_one[second_move].type_weaknesses()
            if type in weaknesses:
                print(f"{one_on_one[first_move]} won!")
                one_on_one.pop(second_move)
                break
        
        for type in one_on_one[second_move].types:
            strengths = one_on_one[first_move].type_strengths()
            weaknesses = one_on_one[first_move].type_weaknesses()
            if type in weaknesses:
                print(f"{one_on_one[second_move]} won!")
                one_on_one.pop(first_move)
                break

        break

        trainer1_pokemon.battle(trainer2_pokemon)

pokemon_battle(ash, gary)