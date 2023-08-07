'''
I think there was a typo in the instructions for this function, it says for this function to print the radius, not circumference.
So I made it return both the radius AND the circumference. 

'''
def print_circum(_radius):
    _pi = 3.14159
    _circumference = 2 * _pi * _radius
    print(f"The radius provided was {_radius}")
    print(f"The circumference would be {_circumference}")
    print(" ")

# These are global variables that define the price of the three items the store sells, and the global total which is updated. 
_item_one_price = 40
_item_two_price = 70
_item_three_price = 100

_total = 0


'''
The add_to_bill function can take as many as three parameters, and as little as one parameter.

It uses if statements to decide whether to apply a discount to the order, and which discount it should be applying.

If there are three item values provided, it will apply the gift pack discount and update total.

If there are two item values provided, it will apply the combo pack discount and update the total.

If there is only one item value provided, it will apply the single item value.

For this function to properly work, you must make sure that you call the function with zero's for the three parameters and 
change only the zero for the item you want to add to the purchase.

For example: If you wanted to purchase Item Two, the call to the function would look like this: 
add_to_bill(0, 1, 0)
'''
def add_to_bill(_item_one=0, _item_two=0, _item_three=0):
    global _total
    if _item_one > 0 and _item_two > 0 and _item_three > 0:
        print(
            f'Gift Pack (Sandals, Sneakers & Boots)         {apply_discount(_item_one, _item_two, _item_three)}')
        _total += apply_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0 and _item_two > 0:
        print(
            f'Combo Pack (Sandals + Sneakers)               {apply_discount(_item_one, _item_two, _item_three)}')
        _total += apply_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0 and _item_three > 0:
        print(
            f'Combo Pack (Sandals + Work Boots)             {apply_discount(_item_one, _item_two, _item_three)}')
        _total += apply_discount(_item_one, _item_two, _item_three)
    elif _item_three > 0 and _item_two > 0:
        print(
            f'Combo Pack (Work Boots + Sneakers)            {apply_discount(_item_one, _item_two, _item_three)}')
        _total += apply_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0:
        print(
            f'Sandals x                                     {_item_one_price * _item_one}')
        _total += (_item_one * _item_one_price)
    elif _item_two > 0:
        print(
            f'Sneakers x                                    {_item_two_price * _item_two}')
        _total += (_item_two * _item_two_price)
    elif _item_three > 0:
        print(
            f'Work Boots                                    {_item_three_price * _item_three}')
        _total += (_item_three * _item_three_price)
        

'''
The apply_discount is a  helper-function to apply the proper discount to the combo/gift packs.

To apply the proper discount, call apply_discount with the correct values corresponding to which products you are purchasing.

For example: 
apply_discount(1, 1, 1) would apply the gift pack discount of 25%
apply_discount(1, 0, 1) would apply the combo pack discount of 10%
'''
def apply_discount(_item_one=0, _item_two=0, _item_three=0):
    _total_before_discount = (_item_one * _item_one_price) + (
        _item_two * _item_two_price) + (_item_three * _item_three_price)
    
    if _item_one > 0 and _item_two > 0 and _item_three > 0:
         return (_total_before_discount - _total_before_discount * .25)
    else:
        return (_total_before_discount - _total_before_discount * .10)



print(" ")
print("- - Part 1 - -")
print_circum(5)
print_circum(10)
print_circum(15)
print(" ")
print("- - Part 2 - -")
print(" ")
print(" Joe's Shoe Shop - Online Store")
print(" ")
print("Products                                      Price") 
print("---------------------------------------------------")
add_to_bill(1, 1, 1)
add_to_bill(1, 0, 1)
add_to_bill(1, 1, 0)
add_to_bill(0, 1, 1)
add_to_bill(1, 0, 0)
add_to_bill(0, 1, 0)
add_to_bill(0, 0, 1)
print("---------------------------------------------------")
print(f"Total                                         {_total}")

