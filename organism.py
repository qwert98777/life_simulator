

class Organism:
    """Базовый класс организма с жизненной логикой."""
    
    def __init__(self, name: str, energy: float, is_predator: bool = False) -> None:
        self.name = name
        self.energy = energy
        self.is_predator = is_predator

    def eat(self, food_energy: float) -> None:
        """Метод питания - увеличивает энергию."""
        self.energy += food_energy
        print(f"{self.name} поел и получил {food_energy} энергии. Энергия: {self.energy:.1f}")

    def take_damage(self, damage: float) -> None:
        """Метод получения урона - уменьшает энергию."""
        self.energy -= damage
        print(f"{self.name} получил {damage:.1f} урона. Осталось энергии: {self.energy:.1f}")

    def is_alive(self) -> bool:
        """Проверка состояния жизни."""
        return self.energy > 0

    def __str__(self) -> str:
        return f"{self.name} (энергия: {self.energy:.1f}, хищник: {self.is_predator})"х
