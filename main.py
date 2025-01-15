class PawnshopInventoryService:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, item_value):
        """Додає річ до інвентаря."""
        if item_id is None:
	        raise TypeError("Item id cannot be None")
        if item_id in self.inventory:
            return "Річ з таким ID вже існує."
        self.inventory[item_id] = {
            'name': item_name,
            'value': item_value,
            'status': 'available'
        }
        return "Річ успішно додана."

    def remove_item(self, item_id):
        """Видаляє річ з інвентаря."""
        if item_id not in self.inventory:
            return "Річ з таким ID не знайдена."
        del self.inventory[item_id]
        return "Річ успішно видалена."

    def update_item(self, item_id, new_name=None, new_value=None):
        """Оновлює дані про річ."""
        if item_id not in self.inventory:
            return "Річ з таким ID не знайдена."
        if new_name:
            self.inventory[item_id]['name'] = new_name
        if new_value:
            self.inventory[item_id]['value'] = new_value
        return "Річ успішно оновлена."

    def list_items(self):
        """Повертає список усіх речей у ломбарді."""
        if not self.inventory:
            return "Інвентар порожній."
        return self.inventory

    def change_status(self, item_id, new_status):
        """Змінює статус речі (наприклад, 'продано' чи 'заставлено')."""
        if item_id not in self.inventory:
            return "Річ з таким ID не знайдена."
        self.inventory[item_id]['status'] = new_status
        return "Статус успішно змінено."

    def check_item_status(self, item_id):
        """Перевіряє статус речі за її ID."""
        if item_id not in self.inventory:
            return "Річ з таким ID не знайдена."
        item = self.inventory[item_id]
        return f"Статус речі '{item['name']}': {item['status']}"

# Приклад використання
service = PawnshopInventoryService()
print(service.add_item(1, "Золоте кільце", 500))
print(service.add_item(2, "Срібний браслет", 300))
print(service.list_items())
print(service.update_item(1, new_value=550))
print(service.change_status(2, "продано"))
print(service.list_items())
print(service.check_item_status(2))  # Перевіряє статус срібного браслета
print(service.remove_item(1))
print(service.list_items())
