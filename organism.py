class Organism:
    """Базовый класс организма."""
    def __init__(self, name: str, energy: float) -> None:
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float) -> None:
        """Метод питания."""
        self.energy += food_energy
        print(f"{self.name} поел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Проверка состояния жизни."""
        return self.energy > 0
