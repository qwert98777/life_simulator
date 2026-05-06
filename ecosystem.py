from organism import Organism
from config_loader import load_config

class Ecosystem:
    """Класс, симулирующий экосистему."""
    
    def __init__(self, config_path: str = "config.json") -> None:
        self.config = load_config(config_path)
        self.organisms = []

    def add_organism(self, organism: Organism) -> None:
        """Добавление организма в экосистему."""
        self.organisms.append(organism)

    def simulate_day(self) -> None:
        """Симуляция дня, проверка жив ли организм."""
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f"{org.name} мёртв.")
