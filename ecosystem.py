from organism import Organism
from config_loader import Configuration

class Ecosystem:
    """ Класс симулирующий экосистему """
    def __init__(self):
        self.config = Configuration
        self.consumption = self.config.get("simulation", "energy_consumption")
        self.organisms = []

    """ Добавление организма в экосистему """
    def add_organism(self, organism: Organism):
        self.organisms.append(organism)

    """ Симуляция дня, проверка жив ли организм """ 
    def simulate_day(self):
        for org in self.organisms:
            if org.is_alive():
                org.eat(-self.consumption)
            else:
                print(f"{org.name} мёртв.")
