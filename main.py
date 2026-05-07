from ecosystem import Ecosystem
from organism import Organism
from predator import Predator

def main():
    """Главная функция."""

    eco = Ecosystem()

    rabbit = Organism("Заяц", 20)
    fox = Predator("Лиса", 30)
    plant = Organism("Растение", 50)

    eco.add_organism(rabbit)
    eco.add_organism(fox)
    eco.add_organism(plant)

    print("=== СИМУЛЯЦИЯ ===")

    for day in range(1, 4):
        print(f"\n--- ДЕНЬ {day} ---")
        eco.simulate_day()

if __name__ == "__main__":
    main()
