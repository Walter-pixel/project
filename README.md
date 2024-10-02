# Datarock code sample


## Dataset
1. The project builds a checkout system. In our inventory, we have 4 types of products shown in below with their 3 attributes: SKU, Name, Price.

        | SKU     | Name        | Price    |
        | --------|:-----------:| --------:|
        | ipd     | Super iPad  | $549.99  |
        | mbp     | MacBook Pro | $1399.99 |
        | atv     | Apple TV    | $109.50  |
        | vga     | VGA adapter | $30.00   |

## Checkout() Class
1. To keep it simple, the main function in ``main.py'' mimic the item scaning procedure by passing item's SKU into the 'Checkout() class instance'. For example, when checking out MacBook Pro, VGA adapter, Super iPad, we run the following scanning commend.
    ```
    co = Checkout()
    co.scan('mbp')
    co.scan('vga')
    co.scan('ipd')
    ```
2. Then we have 3 promotion rules defined by manager as instructed in https://github.com/DiUS/coding-tests/blob/master/dius_shopping.md. To calculate the final cost with applied promotion , we call the ``total'' method inherent in the 'Checkout' class with a list of promption name (in string format), and it will return you the final cost a customor need to pay. Here, the 3 promotion options are:
```
'rule_three_for_two_atv'
'rule_ipad4'
'rule_VGAfree_per_Mac'
```
If you want to apply all 3 promotion, simply put all promotion names into a list as input variable for the 'total' function, that is:
```
co.total(['rule_three_for_two_atv',
              'rule_ipad4',
              'rule_VGAfree_per_Mac'])
```
then it will return you the final cost after applying 3 promotions. Note that the order of promotion name does not matter.
You can also apply only selected promotion instead of all 3. For example, if I only want to apply 'rule_ipad4', then do:
```
co.total(['rule_ipad4'])
```
then it will return you the final cost after applying only 'rule_ipad4' promotion.

==================================================================================
## Unit Test