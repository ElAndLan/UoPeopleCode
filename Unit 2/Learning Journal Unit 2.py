print(" ")
print("- - Part 1 - -")


def print_circum(radius):
    print(radius)


print_circum(5)
print_circum(10)
print_circum(15)

_item_one_price = 40
_item_two_price = 70
_item_three_price = 100

_total = 0


def add_to_bill(_item_one=0, _item_two=0, _item_three=0):
    global _total
    if _item_one > 0 and _item_two > 0 and _item_three > 0:
        print(
            f'Gift Pack (Sandals, Sneakers & Boots)         {apply_gift_discount(_item_one, _item_two, _item_three)}')
        _total += apply_gift_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0 and _item_two > 0:
        print(
            f'Combo Pack (Sandals + Sneakers)               {apply_combo_discount(_item_one, _item_two, _item_three)}')
        _total += apply_combo_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0 and _item_three > 0:
        print(
            f'Combo Pack (Sandals + Work Boots)             {apply_combo_discount(_item_one, _item_two, _item_three)}')
        _total += apply_combo_discount(_item_one, _item_two, _item_three)
    elif _item_three > 0 and _item_two > 0:
        print(
            f'Combo Pack (Work Boots + Sneakers) {apply_combo_discount(_item_one, _item_two, _item_three)}')
        _total += apply_combo_discount(_item_one, _item_two, _item_three)
    elif _item_one > 0:
        print(
            f'Sandals x {_item_one}                                   {_item_one_price * _item_one}')
        _total += (_item_one * _item_one_price)
    elif _item_two > 0:
        print(
            f'Sneakers x {_item_two}                                  {_item_two_price * _item_two}')
        _total += (_item_two * _item_two_price)
    elif _item_three > 0:
        print(
            f'Work Boots x {_item_three}                                {_item_three_price * _item_three}')
        _total += (_item_three * _item_three_price)


def apply_combo_discount(_item_one=0, _item_two=0, _item_three=0):
    _total_before_discount = (_item_one * _item_one_price) + (
        _item_two * _item_two_price) + (_item_three * _item_three_price)
    return (_total_before_discount - _total_before_discount * .10)


def apply_gift_discount(_item_one=0, _item_two=0, _item_three=0):
    _total_before_discount = (_item_one * _item_one_price) + (
        _item_two * _item_two_price) + (_item_three * _item_three_price)
    return (_total_before_discount - _total_before_discount * .25)


print(" ")
print("- - Part 2 - -")
print(" ")
print(" Joe's Shoe Shop")
print(" ")
add_to_bill(1, 1, 1)
add_to_bill(1, 0, 1)
add_to_bill(1, 1, 0)
add_to_bill(1, 0, 0)
add_to_bill(0, 1, 0)
add_to_bill(0, 0, 1)
print(" ")
print(f"Total:                                        {_total}")
