from organism import Organism

class Ecosystem:
    def __init__(self):
        self.organisms = []

    def add_organism(self, organism: Organism) -> None:
        self.organisms.append(organism)

    def simulate_day(self) -> None:
        print("\n--- Новый день ---")
        new_organisms = []

        for org in self.organisms[:]:
            if not org.is_alive():
                print(f"{org.name} мёртв и удалён.")
                self.organisms.remove(org)
                continue

            if org.is_predator:
                prey = next((o for o in self.organisms if not o.is_predator and o.is_alive()), None)
                if prey:
                    print(f"{org.name} (хищник) охотится на {prey.name}!")
                    prey.energy -= 15
                    if not prey.is_alive():
                        print(f"  {prey.name} погиб.")
                        self.organisms.remove(prey)
                    org.eat(15)
                else:
                    org.eat(5)
            else:
                org.eat(8)

            baby = org.reproduce(f"детёныш_{org.name}")
            if baby:
                new_organisms.append(baby)
                print(f"  {org.name} произвёл потомство: {baby.name}")

        self.organisms.extend(new_organisms)
