from organism import Organism
from predator import Predator

class Ecosystem:
    """Класс, симулирующий экосистему."""

    def __init__(self) -> None:
        self.organisms = []

    def add_organism(self, organism: Organism) -> None:
        """Добавление организма."""
        self.organisms.append(organism)

    def simulate_day(self) -> None:
        """Симуляция одного дня."""
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f"{org.name} мёртв.")
