import unittest
from main import Checkout

class TestPromotion(unittest.TestCase):
    def test_rule_three_for_two_atv(self):
        co = Checkout()
        co.scan('atv')
        co.scan('atv')
        co.scan('atv')
        co.total(['rule_three_for_two_atv'])
        self.assertEqual(co.total_price , 109.50*2)
    
    def rule_ipad4(self):
        co = Checkout()
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.scan('ipd')
        co.total(['rule_ipad4'])
        self.assertEqual(co.total_price , 549.99*5)

    
    def rule_VGAfree_per_Mac(self):
        co = Checkout()
        co.scan('vga')
        co.scan('vga')
        co.scan('mbp')
        co.scan('mbp')
        co.scan('mbp')
        co.total(['rule_ipad4'])
        self.assertEqual(co.total_price , 1399.99*3)
        
if __name__ == '__main__':
    unittest.main()