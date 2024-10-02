import unittest
from main import Checkout

# By default, only functions whose name that start with test are run

class TestPromotion(unittest.TestCase):
    def test_rule_three_for_two_atv(self):
        print('Test 1: 3 for 2 promotion on atv - consider 3 atv')
        co = Checkout()
        co.scan('atv')
        co.scan('atv')
        co.scan('atv')
        co.total(['rule_three_for_two_atv'])
        self.assertEqual(co.total_price , 109.50*2)
    
    def test_rule_ipad4(self):
        print('Test 2: ipad>4 discount to 499.99 each - consider 5 ipd')
        co = Checkout()
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.total(['rule_ipad4'])
        self.assertEqual(co.total_price , 499.99*5)

    
    def test_rule_VGAfree_per_Mac(self):
        co = Checkout()
        print('Test 3: vga free paired with every mbp - consider 2 vga and 3 mbp')
        co.scan('vga')
        co.scan('vga')
        co.scan('mbp')
        co.scan('mbp')
        co.scan('mbp')
        co.total(['rule_VGAfree_per_Mac'])
        self.assertEqual(co.total_price , 1399.99*3)
        
if __name__ == '__main__':
    unittest.main()