#!/usr/bin/env python3
"""
Дополнительные тесты для увеличения покрытия
"""

import unittest
import os


class TestFileStructure(unittest.TestCase):
    """Тесты структуры файлов проекта"""
    
    def test_main_py_exists(self):
        """Тест: файл main.py существует"""
        self.assertTrue(os.path.exists("main.py"),
                       "Файл main.py должен существовать")
    
    def test_test_file_exists(self):
        """Тест: файл test_app.py существует"""
        self.assertTrue(os.path.exists("test_app.py"),
                       "Файл test_app.py должен существовать")
    
    def test_workflow_file_exists(self):
        """Тест: файл workflow существует"""
        workflow_path = ".github/workflows/ci.yml"
        self.assertTrue(os.path.exists(workflow_path),
                       f"Файл {workflow_path} должен существовать")


class TestCodeQuality(unittest.TestCase):
    """Тесты качества кода"""
    
    def test_no_syntax_errors(self):
        """Тест: отсутствие синтаксических ошибок"""
        try:
            with open("main.py", "r", encoding="utf-8") as f:
                code = f.read()
            compile(code, "main.py", "exec")
            result = True
        except SyntaxError as e:
            result = False
            print(f"Syntax error in main.py: {e}")
        
        self.assertTrue(result, "Код должен быть без синтаксических ошибок")


if __name__ == '__main__':
    unittest.main()