import json

def load_config(config_path: str = "config.json") -> dict:
    """Загрузка конфигурации из JSON файла."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {config_path} не найден. Использую стандартные настройки.")
        return {
            "simulation_days": 7,
            "food_energy": 10
        }
