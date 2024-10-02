

class Checkout():
    def __init__(self,):
        self.items = {
            'ipd': ['Super iPad', 549.99],
            'mbp': ['MacBook Pro', 1399.99],
            'atv': ['Apple TV', 109.50],
            'vga': ['VGA adapter', 30.00],
        }
        self.scan_collect = {
            'ipd':0,
            'mbp':0,
            'atv':0,
            'vga':0,
         }
        self.total_price = 0


    def scan(self, target:str):
        if target not in self.items:
            print(f'This item is not belong to our inventory')
        else:
            self.scan_collect[target]+=1
            print("Added")

    def total(self, rules: list[str]):
        '''
        This function run all the rules that apply and return the lowest price option
        rules: the list of rule options to applied are 'rule_three_for_two_atv', 'rule_ipad4', 'rule_VGAfree_per_Mac'
        '''
        if 'rule_three_for_two_atv' in rules:
            self.rule_three_for_two_atv()
        if 'rule_ipad4' in rules:
            self.rule_ipad4()
        if 'rule_VGAfree_per_Mac' in rules:
            self.rule_VGAfree_per_Mac()
        
        # Check item left in the collection after promotion applied
        remain_cost = self.scan_collect['ipd']*self.items['ipd'][1] + \
                        self.scan_collect['mbp']*self.items['mbp'][1] + \
                        self.scan_collect['atv']*self.items['atv'][1] + \
                        self.scan_collect['vga']*self.items['vga'][1]
        
        self.total_price += round(remain_cost, 2)
    



    def rule_three_for_two_atv(self):
        num_threes = self.scan_collect['atv']//3 # how many threes-bundles of atv exitst in scanned
        self.total_price += round(self.items['atv'][1]*2*num_threes, 2)

        # remove the checked out items
        self.scan_collect['atv'] -= num_threes*3
        print(f'Promotion: atv 3 for 2 rule applied')
    

    def rule_ipad4(self):
        dropto_price_each = 499.99
        num_fours = self.scan_collect['ipd']//4 # how many fours-bundles of ipd exitst in scanned
        self.total_price += round(num_fours*4*dropto_price_each, 2)

        # remove the checked out items
        self.scan_collect['ipd'] -= num_fours*4
        print(f'Promotion: Super iPad 4 for 499.99 each applied')

    
    def rule_VGAfree_per_Mac(self):
        if self.scan_collect['mbp'] >= self.scan_collect['vga']: # vga are all free
            # remove the checked out items
            self.scan_collect['vga'] = 0
            print(f'Promotion: free VGA per MacBook Pro applied')
        else: 
            num_free_vga = self.scan_collect['mbp'] 
            # remove the checked out items
            self.scan_collect['vga'] -= num_free_vga
            print(f'Promotion: free VGA per MacBook Pro applied')




        


    

if __name__ == "__main__":
    co = Checkout()
    co.scan('mbp')
    co.scan('vga')
    co.scan('ipd')
   
    co.total(['rule_three_for_two_atv',
              'rule_ipad4',
              'rule_VGAfree_per_Mac'])
    print(f'Total Price: {co.total_price}')
 