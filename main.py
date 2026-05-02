from ecosystem import Ecosystem
from organism import Organism

def main():
    eco = Ecosystem()
    rabbit = Organism("Заяц", 25, is_predator=False)
    fox = Organism("Лиса", 30, is_predator=True)
    eco.add_organism(rabbit)
    eco.add_organism(fox)

    days = 5
    for day in range(1, days + 1):
        print(f"\nДень {day}")
        eco.simulate_day()

        if sum(1 for o in eco.organisms if o.is_alive()) == 0:
            print("Все организмы погибли. Симуляция завершена.")
            break
    else:
        print(f"\nСимуляция завершена. Выжившие организмы: {[o.name for o in eco.organisms if o.is_alive()]}")

if __name__ == "__main__":
    main()
