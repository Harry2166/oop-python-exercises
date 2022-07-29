import random

names = open('OOP/Pokemon/first-names.txt')
name_list = []
for line in names:
    name_list.append(line.strip())

trainer_classes = open('OOP/Pokemon/trainer-classes.txt')
trainer_classes_list = []
for line in trainer_classes:
    trainer_classes_list.append(line.strip())

pokemon = {'Bulbasaur' : ['Grass', 'Poison'], 'Ivysaur' : ['Grass', 'Poison'], 'Venusaur' : ['Grass', 'Poison'], 'Charmander' : ['Fire'], 'Charmeleon' : ['Fire'], 
            'Charizard' : ['Fire', 'Flying'], 'Squirtle' : ['Water'], 'Wartortle' : ['Water'], 'Blastoise' : ['Water'], 'Caterpie' : ['Bug'], 'Metapod' : ['Bug'], 
            'Butterfree' : ['Bug', 'Flying'], 'Weedle' : ['Bug', 'Poison'], 'Kakuna' : ['Bug', 'Poison'], 'Beedrill' : ['Bug', 'Poison'], 'Pidgey' : ['Normal', 'Flying'], 
            'Pidgeotto' : ['Normal', 'Flying'], 'Pidgeot' : ['Normal', 'Flying'], 'Rattata' : ['Normal'], 'Raticate' : ['Normal'], 'Spearow' : ['Normal', 'Flying'], 
            'Fearow' : ['Normal', 'Flying'], 'Ekans' : ['Poison'], 'Arbok' : ['Poison'], 'Pikachu' : ['Electric'], 'Raichu' : ['Electric'], 'Sandshrew' : ['Ground'], 
            'Sandslash' : ['Ground'], 'Nidoran♀' : ['Poison'], 'Nidorina' : ['Poison'], 'Nidoqueen' : ['Poison', 'Ground'], 'Nidoran♂' : ['Poison'], 'Nidorino' : ['Poison'], 
            'Nidoking' : ['Poison', 'Ground'], 'Clefairy' : ['Fairy'], 'Clefable' : ['Fairy'], 'Vulpix' : ['Fire'], 'Ninetales' : ['Fire'], 'Jigglypuff' : ['Fairy'], 
            'Wigglytuff' : ['Fairy'], 'Zubat' : ['Poison', 'Flying'], 'Golbat' : ['Poison', 'Flying'], 'Oddish' : ['Grass', 'Poison'], 'Gloom' : ['Grass', 'Poison'], 
            'Vileplume' : ['Grass', 'Poison'], 'Paras' : ['Bug', 'Grass'], 'Parasect' : ['Bug', 'Grass'], 'Venonat' : ['Bug', 'Poison'], 'Venomoth' : ['Bug', 'Poison'], 
            'Diglett' : ['Ground'], 'Dugtrio' : ['Ground'], 'Meowth' : ['Normal'], 'Persian' : ['Normal'], 'Psyduck' : ['Water'], 'Golduck' : ['Water'], 
            'Mankey' : ['Fighting'], 'Primeape' : ['Fighting'], 'Growlithe' : ['Fire'], 'Arcanine' : ['Fire'], 'Poliwag' : ['Water'], 'Poliwhirl' : ['Water'], 
            'Poliwrath' : ['Water', 'Fighting'], 'Abra' : ['Psychic'], 'Kadabra' : ['Psychic'], 'Alakazam' : ['Psychic'], 'Machop' : ['Fighting'], 'Machoke' : ['Fighting'], 
            'Machamp' : ['Fighting'], 'Bellsprout' : ['Grass', 'Poison'], 'Weepinbell' : ['Grass', 'Poison'], 'Victreebel' : ['Grass', 'Poison'], 'Tentacool' : ['Water', 'Poison'], 
            'Tentacruel' : ['Water', 'Poison'], 'Geodude' : ['Rock', 'Ground'], 'Graveler' : ['Rock', 'Ground'], 'Golem' : ['Rock', 'Ground'], 'Ponyta' : ['Fire'], 
            'Rapidash' : ['Fire'], 'Slowpoke' : ['Water', 'Psychic'], 'Slowbro' : ['Water', 'Psychic'], 'Magnemite' : ['Electric', 'Steel'], 'Magneton' : ['Electric', 'Steel'], 
            "Farfetch'd" : ['Normal', 'Flying'], 'Doduo' : ['Normal', 'Flying'], 'Dodrio' : ['Normal', 'Flying'], 'Seel' : ['Water'], 'Dewgong' : ['Water', 'Ice'], 
            'Grimer' : ['Poison'], 'Muk' : ['Poison'], 'Shellder' : ['Water', 'Ice'], 'Cloyster' : ['Water', 'Ice'], 'Gastly' : ['Ghost', 'Poison'], 'Haunter' : ['Ghost', 'Poison'], 
            'Gengar' : ['Ghost', 'Poison'], 'Onix' : ['Rock', 'Ground'], 'Drowzee' : ['Psychic'], 'Hypno' : ['Psychic'], 'Krabby' : ['Water'], 'Kingler' : ['Water'], 
            'Voltorb' : ['Electric'], 'Electrode' : ['Electric'], 'Exeggcute' : ['Grass', 'Psychic'], 'Exeggutor' : ['Grass', 'Psychic'], 'Cubone' : ['Ground'], 'Marowak' : ['Ground'], 
            'Hitmonlee' : ['Fighting'], 'Hitmonchan' : ['Fighting'], 'Lickitung' : ['Normal'], 'Koffing' : ['Poison'], 'Weezing' : ['Poison'], 'Rhyhorn' : ['Rock', 'Ground'], 
            'Rhydon' : ['Rock', 'Ground'], 'Chansey' : ['Normal'], 'Tangela' : ['Grass'], 'Kangaskhan' : ['Normal'], 'Horsea' : ['Water'], 'Seadra' : ['Water'], 
            'Goldeen' : ['Water'], 'Seaking' : ['Water'], 'Staryu' : ['Water', 'Psychic'], 'Starmie' : ['Water', 'Psychic'], 'Mr. Mime' : ['Psychic', 'Fairy'], 
            'Scyther' : ['Bug', 'Flying'], 'Jynx' : ['Ice', 'Psychic'], 'Electabuzz' : ['Electric'], 'Magmar' : ['Fire'], 'Pinsir' : ['Bug'], 'Tauros' : ['Normal'], 
            'Magikarp' : ['Water'], 'Gyarados' : ['Water', 'Flying'], 'Lapras' : ['Water', 'Ice'], 'Ditto' : ['Normal'], 'Eevee' : ['Normal'], 'Vaporeon' : ['Water'], 
            'Jolteon' : ['Electric'], 'Flareon' : ['Fire'], 'Porygon' : ['Normal'], 'Omanyte' : ['Rock', 'Water'], 'Omastar' : ['Rock', 'Water'], 'Kabuto' : ['Rock', 'Water'], 
            'Kabutops' : ['Rock', 'Water'], 'Aerodactyl' : ['Rock', 'Flying'], 'Snorlax' : ['Normal'], 'Articuno' : ['Ice', 'Flying'], 'Zapdos' : ['Electric', 'Flying'], 
            'Moltres' : ['Fire', 'Flying'], 'Dratini' : ['Dragon'], 'Dragonair' : ['Dragon'], 'Dragonite' : ['Dragon', 'Flying'], 'Mewtwo' : ['Psychic'], 'Mew' : ['Psychic']}

print(random.randint(0, 6))