"""
Тесты для приложения
"""

import unittest
import io
import sys

# Импортируем main из нашего файла
from main import main

class TestApp(unittest.TestCase):
    """Тестовый класс для приложения"""
    
    def test_main_output(self):
        """Тестирование вывода основной функции"""
        # Перехватываем вывод
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Запускаем main функцию
        main()
        
        # Восстанавливаем стандартный вывод
        sys.stdout = sys.__stdout__
        
        # Получаем выведенный текст
        output = captured_output.getvalue()
        
        # Проверяем наличие ключевых фраз
        self.assertIn("Hello, CI!", output)
        self.assertIn("This is a simple Python application", output)
        self.assertIn("Author:", output)

if __name__ == '__main__':
    unittest.main()