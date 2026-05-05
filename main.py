from ecosystem import Ecosystem
from organism import Organism

def main():
    # Создание 3-х объектов
    eco = Ecosystem()
    rabbit = Organism("Заяц", 20)
    fox = Organism("Лиса", 30)
    plant = Organism("Растение", 30)

    # Добавление
    eco.add_organism(rabbit)
    eco.add_organism(fox)
    eco.add_organism(plant)

    # Старт симуляции
    eco.simulate_day()

if __name__ == "__main__":
    main()
