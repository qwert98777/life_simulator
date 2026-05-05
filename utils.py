import random


events = [None, "Засуха", "Высокая урожайность", "Дождь", "Плохая погода"]
chances = [65, 5, 5, 18, 7]

def event():
    """Выбирает случайное событие из доступных"""
    return random.choices(events, weights=chances, k=1)[0]
