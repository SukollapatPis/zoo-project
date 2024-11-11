# Lab 15
# Sukollapat Pisuchpen
# 6687052
# Sec 2
import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo()
    # Test Path 1: age < 0 ::: use -1 ERROR CASE
    def test_get_ticket_price_path1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "error, Please enter the correct age")
    # Test Path 2: age >= 0 and age <= 12 ::: use 0, 12
    def test_get_ticket_price_path2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    # Test Path 3: age >= 13 and age <= 20 ::: use 13, 20
    def test_get_ticket_price_path3(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    # Test Path 4: age >= 21 and age <= 60 ::: use 21, 60
    def test_get_ticket_price_path4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    # Test Path 5: age > 60 ::: use 61
    def test_get_ticket_price_path5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    
if __name__ == '__main__':
    unittest.main()
