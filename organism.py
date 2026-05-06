class Organism:
    """Базовый класс организма."""
    
    def __init__(self, name: str, energy: float, is_predator: bool = False) -> None:
        self.name = name
        self.energy = energy
        self.is_predator = is_predator

    def eat(self, food_energy: float) -> None:
        """Метод питания."""
        self.energy += food_energy
        print(f"{self.name} поел и получил {food_energy} энергии.")

    def take_damage(self, damage: float) -> None:
        """Метод получения урона."""
        self.energy -= damage
        print(f"{self.name} получил {damage:.1f} урона.")

    def is_alive(self) -> bool:
        """Проверка состояния жизни."""
        return self.energy > 0
