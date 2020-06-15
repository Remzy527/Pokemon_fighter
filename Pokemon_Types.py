import enum


class Types(enum.Enum):
    # Enumerations of the Pokemon Types
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

    # Built 4 different dictionaries for the types and percentage of damage done.
    # The key: value pair in the format AttackingPokemon : [List of Pokemons attacked]
    zero_damage = {Normal: [Ghost], Electric: [Ground], Fighting: [Ghost], Poison: [Steel], Ground: [Flying],
                   Psychic: [Dark], Ghost: [Normal], Dragon: [Fairy]}

    half_damage = {Normal: [Rock, Steel], Fire: [Fire, Water, Rock, Dragon], Water: [Water, Grass, Dragon],
                   Electric: [Electric, Grass, Dragon], Grass: [Fire, Grass, Poison, Flying, Bug, Dragon, Steel],
                   Ice: [Fire, Water, Ice, Steel], Fighting: [Poison, Flying, Psychic, Bug, Fairy],
                   Poison: [Poison, Ground, Rock, Ghost], Ground: [Grass, Bug], Flying: [Electric, Rock, Steel],
                   Psychic: [Psychic, Steel], Bug: [Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy],
                   Rock: [Fighting, Ground, Steel], Ghost: [Dark], Dragon: [Steel], Dark: [Fighting, Dark, Fairy],
                   Steel: [Fire, Water, Electric, Steel], Fairy: [Fire, Poison, Steel]}

    twice_damage = {Fire: [Grass, Ice, Bug, Steel], Water: [Fire, Ground, Rock], Electric: [Water, Flying],
                    Grass: [Water, Ground, Rock], Ice: [Grass, Ground, Flying, Dragon],
                    Fighting: [Normal, Ice, Rock, Dark, Steel], Poison: [Grass, Fairy],
                    Ground: [Fire, Electric, Poison, Rock, Steel], Flying: [Grass, Fighting, Bug],
                    Psychic: [Fighting, Poison], Bug: [Grass, Psychic, Dark], Rock: [Fire, Ice, Flying, Bug],
                    Ghost: [Ghost, Psychic], Dragon: [Dragon], Dark: [Psychic, Ghost], Steel: [Ice, Rock, Fairy],
                    Fairy: [Fighting, Dragon, Dark]}

