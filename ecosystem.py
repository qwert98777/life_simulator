from organism import Organism

class Ecosystem:
    """Класс экосистемы."""

    def __init__(self) -> None:
        self.organisms = []

    def add_organism(self, organism: Organism) -> None:
        """Добавление организма."""
        self.organisms.append(organism)

    def simulate_day(self) -> None:
        """Симуляция дня."""
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f"{org.name} мёртв.")
