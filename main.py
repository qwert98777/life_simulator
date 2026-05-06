from ecosystem import Ecosystem
from organism import Organism

def main():
    """Главная функция - создание организмов, запуск симуляции, вывод результатов."""
    
    # Создание экосистемы
    eco = Ecosystem()
    
    # Создание экземпляров организмов
    rabbit = Organism("Заяц", 20, is_predator=False)
    fox = Organism("Лиса", 35, is_predator=True)
    plant = Organism("Растение", 50, is_predator=False)
    
    # Добавление в экосистему
    eco.add_organism(rabbit)
    eco.add_organism(fox)
    eco.add_organism(plant)
    
    # Вывод информации о начале симуляции
    print("\n=== ЗАПУСК СИМУЛЯЦИИ ===")
    print(f"Всего организмов: {len(eco.organisms)}")
    
    # Запуск симуляции на 3 дня
    for day in range(1, 4):
        print(f"\n--- ДЕНЬ {day} ---")
        eco.simulate_day()
    
    # Вывод результатов
    print("\n=== РЕЗУЛЬТАТЫ СИМУЛЯЦИИ ===")
    alive_organisms = [org for org in eco.organisms if org.is_alive()]
    print(f"Выжило организмов: {len(alive_organisms)}")
    for org in alive_organisms:
        print(f"  ✓ {org.name} (энергия: {org.energy:.1f})")
    
    if len(alive_organisms) == 0:
        print("  ✗ Все организмы погибли.")

if __name__ == "__main__":
    main()
