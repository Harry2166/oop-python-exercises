# This program is to present all the strengths, weaknesses, immunities of each pokemon type combination

types = ['Bug', 'Dark', 'Dragon',
        'Electric', 'Fairy', 'Fighting',
        'Fire',	'Flying',	'Ghost',
        'Grass', 'Ground',	'Ice',
       'Normal', 'Poison',	'Psychic',
        'Rock', 'Steel', 'Water'] # List of all typings in Pokemon as of Generation 8 arranged in alphabetical order

strength = [['Dark','Grass', 'Psychic'], ['Ghost', 'Psychic'], ['Dragon'], ['Flying', 'Water'], ['Dark', 'Dragon', 'Fighting'], ['Dark', 'Ice', 'Normal', 'Rock', 'Steel'],
            ['Bug', 'Grass', 'Ice', 'Steel'], ['Bug', 'Fighting', 'Grass'], ['Ghost', 'Psychic'], ['Ground', 'Rock', 'Water' ], ['Electric', 'Fire', 'Poison', 'Rock', 'Steel'],
            ['Dragon', 'Flying', 'Grass', 'Ground'], [], ['Fairy', 'Grass'], ['Fighting', 'Poison'], ['Bug', 'Fire', 'Flying', 'Ice'], ['Fairy', 'Ice', 'Rock'], 
            ['Fire', 'Ground', 'Rock']] # List of all the strenghts that each pokemon typing has against each other arranged in alphabetical order

weakness = [['Fire', 'Flying', 'Rock'], ['Bug','Fairy','Fighting'], ['Dragon', 'Fairy', 'Ice'], ['Ground'], ['Poison', 'Steel'], ['Fairy', 'Flying', 'Psychic'], 
            ['Ground', 'Rock', 'Water'], ['Electric', 'Ice', 'Rock'], ['Dark', 'Ghost'], ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'], ['Grass', 'Ice', 'Water'],
            ['Fighting', 'Fire', 'Rock', 'Steel'], ['Fighting'], ['Ground', 'Psychic'], ['Bug', 'Dark', 'Ghost'], ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'], 
            ['Fighting', 'Fire', 'Ground'], ['Electric', 'Grass']] # List of all the weaknesses that each pokemon typing has against each other arranged in alphabetical order

resistances = [['Fighting', 'Grass', 'Ground'], ['Dark', 'Ghost'], ['Electric', 'Fire', 'Grass', 'Water'], ['Electric', 'Flying', 'Steel'], ['Bug', 'Dark', 'Fighting'], 
            ['Bug', 'Dark', 'Rock'], ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'], ['Bug', 'Fighting', 'Grass'], ['Bug', 'Poison'], ['Electric', 'Grass', 'Ground', 'Water'],
            ['Poison', 'Rock'], ['Ice'], [], ['Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'], ['Fighting', 'Psychic'], ['Fire', 'Flying', 'Normal', 'Poison'], 
            ['Bug', 'Fairy', 'Dragon', 'Grass', 'Ice', 'Flying', 'Normal', 'Psychic', 'Rock', 'Steel'], ['Fire', 'Ice', 'Steel', 'Water']]
            #this list shows all resistances that each pokemon type has

immunities = [[], ['Psychic'], [], [], ['Dragon'], [], [], ['Ground'], ['Normal', 'Fighting'], [], ['Electric'], [], ['Ghost'], [], [], [], ['Poison'], []]
            #this list shows all immunities that each pokemon type has


# number_of_types = input("Will it be a monotype or a dualtype? Enter m for monotyping, d for dualtyping, all to see all typings, or q for quit\n")

# if number_of_types == 'q':
#     quit()

# elif number_of_types == 'all':
#     print(", ".join(types))

# elif number_of_types == 'm':
#     what_monotype = input("What typing would you like to see?\n").title()

#     if what_monotype in types:
#         index_monotype = types.index(what_monotype)
#         print(f"Strengths: {', '.join(strength[index_monotype])}\nWeaknesses: {', '.join(weakness[index_monotype])}")
#     else:
#         print("Please input a valid Pokemon typing.")

# elif number_of_types == 'd':
#     what_dualtype1 = input("What is the primary typing?\n").title()
#     what_dualtype2 = input("What is the secondary typing?\n").title()

#     if what_dualtype1 == what_dualtype2:
#         print("Please ensure that the two typings are not the same.")
#         quit()

#     if what_dualtype1 in types and what_dualtype2 in types:

#         overall_weakness = [] # stores the overall weaknesses of the dual type
#         overall_strength = [] # stores the overall strengths of the dual type
        
#         resistance_immunities = [] # stores the overall resistances & immunities

#         index_dualtype1 = types.index(what_dualtype1)
#         index_dualtype2 = types.index(what_dualtype2)

#         for typing in strength[index_dualtype1]: # loop that adds all strengths from the primary type to the overall strengths list
#             overall_strength.append(typing)

#         for typing in strength[index_dualtype2]: # loop that adds all strengths from the secondary type to the overall strengths list
#             overall_strength.append(typing)

#         for typing in weakness[index_dualtype1]: # loop that adds all weaknesses from the primary type to the overall weaknesses list
#             overall_weakness.append(typing) 

#         for typing in weakness[index_dualtype2]: # loop that adds all weaknesses from the primary type to the overall weaknesses list
#             overall_weakness.append(typing)

#         # for typing in overall_strength:
#         #     if typing == types[2] or typing == types[8]:
#         #         pass
#         #     elif typing in overall_weakness:
#         #         new_overall_strength.append(typing)
#         #         resistance_immunities.append(typing)
        
#         for typing in overall_weakness: # this for loop goes through all typings in the overall_weakness list and checks out the resistances and immunities that each
#             if typing in immunities[index_dualtype1] or typing in immunities[index_dualtype2]: # types has. If it is present in the resistances or immunities, then it
#                 resistance_immunities.append(typing) # would be added to the resistances and immunities list
#             elif typing in resistances[index_dualtype1] or typing in resistances[index_dualtype2]:
#                 resistance_immunities.append(typing)
                
#         print(f"Strengths: {', '.join(list((set(overall_strength))))}")
#         print(f"Weaknesses: {', '.join(list((set(overall_weakness)) - set(resistance_immunities)))}") # this was set like this as it removes all types that were included in the
#                                                                                                     #resistances and immunities and just prints a list that has all weaknesses.
#     else:
#         print("Please input the valid typing/s.")

# else:
#     print("Please enter a valid input.")

# # created by Harry2166