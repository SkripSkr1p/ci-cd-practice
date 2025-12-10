#!/usr/bin/env python3
"""
Тесты для приложения с расширенным покрытием
"""

import unittest
import io
import sys
from main import main


class TestApp(unittest.TestCase):
    """Тестовый класс для приложения"""

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.original_stdout = sys.stdout
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """Очистка после каждого теста"""
        sys.stdout = self.original_stdout

    def test_main_output_contains_hello(self):
        """Тест: вывод содержит приветствие"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("Hello, CI!", output, 
                     "Сообщение должно содержать 'Hello, CI!'")

    def test_main_output_contains_description(self):
        """Тест: вывод содержит описание приложения"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("This is a simple Python application", output,
                     "Сообщение должно содержать описание приложения")

    def test_main_output_contains_author(self):
        """Тест: вывод содержит имя автора"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("Author:", output,
                     "Сообщение должно содержать имя автора")

    def test_main_returns_none(self):
        """Тест: функция main возвращает None"""
        result = main()
        self.assertIsNone(result, "Функция main должна возвращать None")

    def test_output_format(self):
        """Тест: проверка общего формата вывода"""
        main()
        output = self.captured_output.getvalue()
        
        # Проверяем что вывод не пустой
        self.assertTrue(len(output) > 0, "Вывод не должен быть пустым")
        
        # Проверяем что вывод заканчивается переносом строки
        self.assertTrue(output.endswith('\n'), 
                       "Вывод должен заканчиваться переносом строки")
        
        # Считаем количество строк
        lines = output.strip().split('\n')
        self.assertGreaterEqual(len(lines), 3,
                              "Вывод должен содержать минимум 3 строки")


class TestEdgeCases(unittest.TestCase):
    """Тесты крайних случаев"""
    
    def test_import_main(self):
        """Тест: корректность импорта функции main"""
        from main import main as imported_main
        self.assertTrue(callable(imported_main),
                       "main должна быть вызываемой функцией")
    
    def test_module_docstring_exists(self):
        """Тест: наличие документации модуля"""
        import main
        self.assertIsNotNone(main.__doc__,
                           "Модуль должен иметь документацию")
        self.assertTrue(len(main.__doc__) > 10,
                       "Документация модуля должна быть не пустой")


if __name__ == '__main__':
    # Запуск с генерацией подробного отчета
    unittest.main(verbosity=2)