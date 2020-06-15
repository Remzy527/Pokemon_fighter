from Pokemon_Types import Types


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

    def attack(self, other_pokemon):
        if self.type in Types.zero_damage:
            if other_pokemon.type in Types.zero_damage[self.type]:
                damage = 0
        elif self.type in Types.half_damage:
            if other_pokemon.type in Types.half_damage[self.type]:
                damage = 50
        elif self.type in Types.twice_damage:
            if other_pokemon.type in Types.twice_damage[self.type]:
                damage = 200
        else:
            damage = 100

        other_pokemon.lose_health(damage)
        print("{name}'s attack inflicted {damage} damage on {name2}".format(name=self.name, name2=other_pokemon.name,
                                                                            damage=damage))

    class Trainer:
        pass
