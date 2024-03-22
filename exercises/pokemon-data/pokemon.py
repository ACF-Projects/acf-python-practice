class Pokemon:
    """
    This is a class that represents a Pokemon
    with name, type, health, and damage 
    attributes. You do not need to worry about
    the specifities of this class; if you're
    curious, you can create a Pokemon with:

    Pokemon(name, type, health, damage)

    And you can call behaviors on it like:

    p = Pokemon("Pikachu", "electric", 100, 20)
    p.take_damage(10)

    Chances are, we'll learn more about this in
    the future. :)
    """
    def __init__(self, name, type, hp, dmg):
        self.name = name
        self.type = type
        self.health = hp
        self.damage = dmg

    def deal_damage_to(self, other_pokemon):
        """
        Takes a reference to another Pokemon and
        reduces that Pokemon's health by the damage
        this Pokemon stores.

        Returns an integer based on the amount 
        of successful damage dealt. (May be lower
        than damage if the other Pokemon has fainted.)
        """
        prev_hp = other_pokemon.health
        other_pokemon.take_damage(self.damage)
        return prev_hp - other_pokemon.health
    
    def take_damage(self, dmg):
        """
        Makes this Pokemon take `dmg` damage.
        Health caps at a minimum of zero health.
        
        Returns True if Pokemon is still standing,
        or False is Pokemon is knocked out.
        """
        self.health -= dmg
        if self.health <= 0:
            self.health = 0
        return self.is_fainted()
    
    def is_fainted(self):
        """
        Returns True if the Pokemon's health has
        reached a fatal value (<= 0).
        """
        return self.health <= 0
    
def get_pokemon(pokemon_info):
    """
    When given a list of pokemon information:
    [name, type, health, damage], returns a 
    Pokemon object (you do not need to worry 
    about what this is right now!) with behaviors 
    defined in `Pokemon.py`.
    """
    return Pokemon(pokemon_info[0], pokemon_info[1], 
                   int(pokemon_info[2]), int(pokemon_info[3]))