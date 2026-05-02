class Organism:
    def __init__(self, name: str, energy: float, is_predator: bool = False):
        self.name = name
        self.energy = energy
        self.is_predator = is_predator

    def eat(self, food_energy: float) -> None:
        self.energy += food_energy
        print(f"  {self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        return self.energy > 0

    def reproduce(self, offspring_name: str):
        if self.energy >= 20:
            self.energy -= 10
            return Organism(offspring_name, 10, self.is_predator)
        return None
