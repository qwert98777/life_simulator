from organism import Organism

class Predator(Organism):
    """Класс хищника."""

    def __init__(self, name: str, health: float) -> None:
        super().__init__(name, health)

    def hunt(self, prey: Organism) -> None:
        """Охота на жертву."""
        damage = self.health * 0.3
        prey.health -= damage
        self.health += damage * 0.7
        print(f"{self.name} атакует {prey.name}!")
