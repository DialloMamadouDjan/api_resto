import unittest
from fonctions import read_csv 


df = read_csv('rest_hours.csv')


class TestMethods(unittest.TestCase):


    def test_read_csv(self):
        self.assertNotIsInstance('rest_hours.csv', tuple)
        self.assertIsNotNone(read_csv('rest_hours.csv'))
        self.assertIsInstance(read_csv('rest_hours.csv'), list)
        














if __name__ == '__main__':
    unittest.main()