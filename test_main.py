import unittest
from main import PawnshopInventoryService

class TestPawnshopInventoryService(unittest.TestCase):
    def setUp(self):
        """Ініціалізація ломбарду перед кожним тестом."""
        self.service = PawnshopInventoryService()

    def test_add_item_success(self):
        """Тест успішного додавання речі."""
        result = self.service.add_item(1, "Золоте кільце", 500)
        self.assertEqual(result, "Річ успішно додана.")
        self.assertIn(1, self.service.inventory)

    def test_add_item_duplicate(self):
        """Тест спроби додавання речі з уже існуючим ID."""
        self.service.add_item(1, "Золоте кільце", 500)
        result = self.service.add_item(1, "Срібний браслет", 300)
        self.assertEqual(result, "Річ з таким ID вже існує.")
        self.assertEqual(self.service.inventory[1]['name'], "Золоте кільце")

    def test_remove_item_success(self):
        """Тест успішного видалення речі."""
        self.service.add_item(1, "Золоте кільце", 500)
        result = self.service.remove_item(1)
        self.assertEqual(result, "Річ успішно видалена.")
        self.assertNotIn(1, self.service.inventory)

    def test_remove_item_not_found(self):
        """Тест видалення речі, якої немає в інвентарі."""
        result = self.service.remove_item(1)
        self.assertEqual(result, "Річ з таким ID не знайдена.")

    def test_update_item_success(self):
        """Тест успішного оновлення даних про річ."""
        self.service.add_item(1, "Золоте кільце", 500)
        result = self.service.update_item(1, new_name="Срібне кільце", new_value=600)
        self.assertEqual(result, "Річ успішно оновлена.")
        self.assertEqual(self.service.inventory[1]['name'], "Срібне кільце")
        self.assertEqual(self.service.inventory[1]['value'], 600)

    def test_update_item_not_found(self):
        """Тест оновлення речі, якої немає в інвентарі."""
        result = self.service.update_item(1, new_name="Срібне кільце")
        self.assertEqual(result, "Річ з таким ID не знайдена.")

    def test_list_items_empty(self):
        """Тест отримання списку речей, коли інвентар порожній."""
        result = self.service.list_items()
        self.assertEqual(result, "Інвентар порожній.")

    def test_list_items_with_data(self):
        """Тест отримання списку речей, коли в інвентарі є дані."""
        self.service.add_item(1, "Золоте кільце", 500)
        self.service.add_item(2, "Срібний браслет", 300)
        result = self.service.list_items()
        self.assertEqual(len(result), 2)
        self.assertIn(1, result)
        self.assertIn(2, result)

    def test_change_status_success(self):
        """Тест успішної зміни статусу речі."""
        self.service.add_item(1, "Золоте кільце", 500)
        result = self.service.change_status(1, "продано")
        self.assertEqual(result, "Статус успішно змінено.")
        self.assertEqual(self.service.inventory[1]['status'], "продано")

    def test_change_status_not_found(self):
        """Тест зміни статусу речі, якої немає в інвентарі."""
        result = self.service.change_status(1, "продано")
        self.assertEqual(result, "Річ з таким ID не знайдена.")

    def test_check_item_status_success(self):
        """Тест перевірки статусу речі."""
        self.service.add_item(1, "Золоте кільце", 500)
        self.service.change_status(1, "заставлено")
        result = self.service.check_item_status(1)
        self.assertEqual(result, "Статус речі 'Золоте кільце': заставлено")

    def test_check_item_status_not_found(self):
        """Тест перевірки статусу речі, якої немає в інвентарі."""
        result = self.service.check_item_status(1)
        self.assertEqual(result, "Річ з таким ID не знайдена.")

    def test_add_item_with_id_none(self):
        self.assertRaises(TypeError, self.service.add_item, None, "Золоте кільце", 500)


if __name__ == "__main__":
    unittest.main()
