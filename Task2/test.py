import unittest
from unittest import TestCase
from main import put_folder


class TestMain(TestCase):
    def test_put_folder_1(self):
        self.assertEqual(put_folder('папка'), 201)

# тест с ошибкой
    def test_put_folder_2(self):
        self.assertEqual(put_folder('папка'), 201)
    
    
    def test_put_folder_3(self):
        self.assertEqual(put_folder('папка'), 409)
