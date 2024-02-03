import os
from pokemon import get_pokemon, Pokemon
import random

"""
When we're dealing with lots of data (especially
in a video game!), it's tedious to write out all
of the data line-by-line in our code.

In this case, we need to find a better way to store
this information, and then write some code to
retrieve it from where we've stored it!

In this assignment, we've provided an entire working
game loop for a Pokemon-spinoff. The only problem is
the way the data is actually stored. 

You'll be tasked with writing a script that parses a
file called `pokemon.info` and converts the lines into
a list of information, where each list represents the
stored information of a Pokemon.
"""

def parse_file(file_name):
    """
    Given a file name, reads the file and returns
    a list of lists, where each list represents
    the information of a Pokemon. (see the
    pokemon.info file for detailed information.)

    Ignore all lines that have a # as the first
    character.
    """
    # Your code here
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line[0] != '#']
        lines = [line.split(',') for line in lines]
        return lines

# Populates the list with the valid Pokemon objects using 
# the `parse_file` function! 
pokemon_list = []
for pokemon_info in parse_file(os.path.dirname(__file__) + "/../pokemon.info"):
    pokemon_list.append(get_pokemon(pokemon_info))

# Game loop for the actual Pokemon game, simulating an
# encounter between two random Pokemon (one that you play
# and one that is wild.)
random.shuffle(pokemon_list)
your_pokemon = pokemon_list.pop()
enemy_pokemon = pokemon_list.pop()
turn_number = 0
print(f"Your {your_pokemon.name} is fighting a wild {enemy_pokemon.name}!")
while not your_pokemon.is_fainted() and not enemy_pokemon.is_fainted():
    your_dmg = your_pokemon.deal_damage_to(enemy_pokemon)
    enemy_dmg = enemy_pokemon.deal_damage_to(your_pokemon)
    turn_number += 1
    print(f"{turn_number}: Your {your_pokemon.name} took {enemy_dmg} damage! ({your_pokemon.health} HP left.)")
    print(f"{turn_number}: The wild {enemy_pokemon.name} took {your_dmg} damage! ({enemy_pokemon.health} HP left.)")

if your_pokemon.is_fainted():
    print(f"Your {your_pokemon.name} has fainted!")
if enemy_pokemon.is_fainted():
    print(f"The wild {enemy_pokemon.name} has fainted!")