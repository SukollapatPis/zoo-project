# Lab 15
# Sukollapat Pisuchpen
# 6687052
# Sec 2
import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo()
    # ========================================================================    
    # ======= Boundary value analysis =======
    '''
    Class	            All Cases	                Belonging Cases	        Reduced Class	      Expected Result
    Age < 0	            -1, 0, 1	                -1	                    -1	                  error, Please enter the correct age
    Age 0-12	        0, 1, 11, 12, 13	        0, 1, 11, 12	        0, 12	              50
    Age 13-20	        12, 13, 14, 19 ,20 ,21	    13, 14, 19 ,20	        13, 20	              100
    Age 21-60	        20, 21, 22, 59, 60, 61	    21, 22, 59, 60	        21, 60	              150
    Age 60+	            60, 61	                    61	                    61	                  100
    '''
    # Test Path 1: Age < 0 ::: use -1 ERROR CASE
    def test_get_ticket_price_path1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "error, Please enter the correct age")
    # Test Path 2:  Age 0-12 ::: use 0, 1, 11, 12
    def test_get_ticket_price_path2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    # Test Path 3: Age 13-20 ::: use 13, 14, 19 ,20
    def test_get_ticket_price_path3(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
        self.assertEqual(self.zoo.get_ticket_price(19), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)    
    # Test Path 4: Age 21-60 ::: use 21, 22, 59, 60
    def test_get_ticket_price_path4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(22), 150)
        self.assertEqual(self.zoo.get_ticket_price(59), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    # Test Path 5: Age 60+ ::: use 61
    def test_get_ticket_price_path5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
        
        
        
    # ========================================================================
    # ======= Equivalence class testing ======= 
    '''
    Class	            Representative	Expected Result
    Age < 0 (Invalid)	-2	            error, Please enter the correct age
    Age 0-12	        6	            50
    Age 13-20	        16	            100
    Age 21-60	        30	            150
    Age 60+	            65	            100

    '''
    # Test Path 1: Age < 0 ::: use 2
    def test_get_ticket_price_path6(self):
        self.assertEqual(self.zoo.get_ticket_price(-2), "error, Please enter the correct age")
    # Test Path 2: Age 0-12 ::: use 6
    def test_get_ticket_price_path7(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)
    # Test Path 3: Age 13-20 ::: use 16
    def test_get_ticket_price_path8(self):
        self.assertEqual(self.zoo.get_ticket_price(16), 100)
    # Test Path 4: Age 21-60 ::: use 30
    def test_get_ticket_price_path9(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
    # Test Path 5: Age 60+ ::: use 65
    def test_get_ticket_price_path10(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)
    

    

if __name__ == '__main__':
    unittest.main()
    
