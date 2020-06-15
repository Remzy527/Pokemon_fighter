from pokemon import Pokemon


class Trainers:
    def __init__(self, name, potions, pokemons, is_turn):
        self.name = name
        self.current_pokemon = pokemons[0]
        self.potions = potions
        self.pokemons = pokemons
        self.is_turn

    def heal_pokemon(self):
        self.current_pokemon.gain_health()
        print("{trainer_name} healed {pokemon_name} with a potion.".format(trainer_name=self.name,
                                                                           pokemon_name=self.current_pokemon.name))

    def attack(self, other_trainer):
        self.current_pokemon.attack(other_trainer.current_pokemon)

    def switch_current_pokemon(self, index):
        previous_pokemon = self.current_pokemon.name
        self.current_pokemon = self.pokemons[index]
        print("{trainer} switched active pokemon from {pokemon_1} to {pokemon_2}".format(trainer=self.name,
                                                                                         pokemon_1=previous_pokemon,
                                                                                         pokemon_2=self.current_pokemon.name))
