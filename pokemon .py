import enum


class Types(enum.Enum):
    Normal = 'Normal'
    Fire = 'Fire'
    Water = 'Water'
    Electric = 'Electric'
    Grass = 'Grass'
    Ice = 'Ice'
    Fighting = 'Fighting'
    Poison = 'Poison'
    Ground = 'Ground'
    Flying = 'Flying'
    Psychic = 'Psychic'
    Bug = 'Bug'
    Rock = 'Rock'
    Ghost = 'Ghost'
    Dragon = 'Dragon'
    Dark = 'Dark'
    Steel = 'Steel'
    Fairy = 'Fairy'

    zero_damage = {Normal: [Ghost], Electric: [Ground], Fighting: [Ghost], Poison: [Steel], Ground: [Flying],
                   Psychic: [Dark], Ghost: [Normal], Dragon: [Fairy]}

    half_damage = {Normal: [], Fire: [], Water: [], Electric: [], Grass: [], Ice: [], Fighting: [], Poison: [],
                   Ground: [], Flying: [], Psychic: [], Bug: [], Rock: [], Ghost: [], Dragon: [], Dark: [],
                   Steel: [], Fairy: []}

    twice_damage = {Normal: [], Fire: [], Water: [], Electric: [], Grass: [], Ice: [], Fighting: [], Poison: [],
                    Ground: [], Flying: [], Psychic: [], Bug: [], Rock: [], Ghost: [], Dragon: [], Dark: [],
                    Steel: [], Fairy: []}


class Pokemon:

    def __init__(self, name, level, max_health, pokemon_type=Types.Normal, is_knocked_out=False):
        self.name = name
        self.type = pokemon_type
        self.level = level
        self.max_health = max_health
        self.health = max_health
        self.is_knocked_out = is_knocked_out

    def lose_health(self, amount):
        self.health -= amount
        print('{name} lost {amount} health. Total health is now has {health}'
              .format(name=self.name, amount=amount, health=self.health))

    def gain_health(self, amount):
        self.health += amount
        print('{name} gained {amount} health. Total health is now has {health}'
              .format(name=self.name, amount=amount, health=self.health))

    def knock_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            print('{name} has been knocked out.'.format(name=self.name))

    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.health = self.max_health
            print('{name} has been revived.'.format(name=self.name))

# Build 4 different dictionaries for the types and damage done
# zeros = {Types.Normal: [Types.Ghost], Types.Electric: [Types.Ground], Types.Fighting: [Types.Ghost],
#          Types.Poison: [Types.Steel], Types.Ground: [Types.Flying], Types.Psychic: [Types.Dark],
#          Types.Ghost: [Types.Normal], Types.Dragon: [Types.Fairy]}
#
# halves = {Types.Normal: [], Types.Fire: [], Types.Water}
