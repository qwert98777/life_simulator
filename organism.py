class Organism:
    """Базовый класс организма."""
    def __init__(self, name: str, energy: float) -> None:
        self.name = name
        self.health = health

    def eat(self, food_health: float) -> None:
        """Метод питания."""
        self.health += food_health
        print(f"{self.name} поел и получил {food_health} энергии.")

    def is_alive(self) -> bool:
        """Проверка состояния жизни."""
        return self.health > 0
