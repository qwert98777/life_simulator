from ecosystem import Ecosystem
from organism import Organism
from predator import Predator

def main():
    """Главная функция запуска симуляции."""
    eco = Ecosystem()

    rabbit = Organism("Заяц", 20)
    fox = Predator("Лиса", 30)
    plant = Organism("Растение", 50)

    eco.add_organism(rabbit)
    eco.add_organism(fox)
    eco.add_organism(plant)

    print("=== ЗАПУСК СИМУЛЯЦИИ ===")
    print(f"Всего организмов: {len(eco.organisms)}")

    for day in range(1, 4):
        print(f"\n--- ДЕНЬ {day} ---")
        eco.simulate_day()

    print("\n=== РЕЗУЛЬТАТЫ ===")
    for org in eco.organisms:
        if org.is_alive():
            print(f"{org.name} выжил со здоровьем {org.health}")
        else:
            print(f"{org.name} погиб")

if __name__ == "__main__":
    main()
