import doctest

def get_biggest(num1:float, num2:float, num3:float) -> float:
    """
    Takes three float values and returns the largest
    >>> get_biggest(1,2,3)
    3
    >>> get_biggest(1,3,2)
    3
    >>> get_biggest(2,1,3)
    3
    >>> get_biggest(2,3,1)
    3
    >>> get_biggest(3,1,2)
    3
    >>> get_biggest(3,2,1)
    3
    >>> get_biggest(0,0,0)
    0
    >>> get_biggest(1,1,1)
    1
    """
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    

def get_smallest(num1:float, num2:float, num3:float) -> float:
    """
    Takes three float values and returns the smallest
    >>> get_smallest(1,2,3)
    1
    >>> get_smallest(1,3,2)
    1
    >>> get_smallest(2,1,3)
    1
    >>> get_smallest(2,3,1)
    1
    >>> get_smallest(3,1,2)
    1
    >>> get_smallest(3,2,1)
    1
    >>> get_smallest(0,0,0)
    0
    >>> get_smallest(1,1,1)
    1
    """
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3:
        return num2
    else:
        return num3
    

def is_multiple_of(num1:float, num2:float) -> bool:
    """
    Returns a boolean repersenting if num1 is a multiple of num2
    >>> is_multiple_of(8, 2)
    True
    >>> is_multiple_of(9, 2)
    False
    >>> is_multiple_of(0, 2)
    True
    >>> is_multiple_of(0, 0)
    True
    >>> is_multiple_of(12, 0)
    False
    """
    if num1 != 0 and num2 == 0: return False
    else: return (num2 == 0 and num1 == 0) or num1 % num2 == 0


def is_biggest_multiple_of_smallest(num1:float, num2:float, num3:float) -> bool:
    """
    Takes three numbers and determines if the biggest number amoung these is a multiple of the smallest
    >>> is_biggest_multiple_of_smallest(2, 5, 6)
    True
    >>> is_biggest_multiple_of_smallest(2, 2, 2)
    True
    >>> is_biggest_multiple_of_smallest(3, 5, 7)
    False
    >>> is_biggest_multiple_of_smallest(1, 0, 0)
    False
    """
    biggest = get_biggest(num1,num2,num3)
    smallest = get_smallest(num1,num2,num3)
    return is_multiple_of(biggest, smallest)


FIRST_PURCHASE_CODE = "FIRST_PURCHASE"
FIRST_PURCHASE_DISCOUNT = 10.0
FREQUENT_BUYER_CODE = "FREQUENT_BUYER"
FREQUENT_BUYER_DISCOUNT = 2.0

def get_discount(code:str, is_member:bool) -> float:
    """
    Takes the given discount code and a membership flag to determine the possible discount
    >>> get_discount("FAKE_CODE", True)
    0.0
    >>> get_discount("NO_DISCOUNT", False)
    0.0
    >>> get_discount("FIRST_PURCHASE", True)
    10.0
    >>> get_discount("FIRST_PURCHASE", False)
    10.0
    >>> get_discount("FREQUENT_BUYER", True)
    2.0
    >>> get_discount("FREQUENT_BUYER", False)
    0.0
    """

    if code == FIRST_PURCHASE_CODE:
        return FIRST_PURCHASE_DISCOUNT
    elif code == FREQUENT_BUYER_CODE and is_member:
        return FREQUENT_BUYER_DISCOUNT
    else:
        return 0.0
    

def get_discounted_price(code:str, price:float, is_member:bool) -> float:
    """
    Takes the given discount code and a membership flag to determine the possible discount
    >>> get_discounted_price("FAKE_CODE", 10, True)
    10.0
    >>> get_discounted_price("NO_DISCOUNT", 0, False)
    0.0
    >>> get_discounted_price("FIRST_PURCHASE", 5, True)
    0.0
    >>> get_discounted_price("FIRST_PURCHASE", 20, False)
    10.0
    >>> get_discounted_price("FREQUENT_BUYER", 15.7, True)
    13.7
    >>> get_discounted_price("FREQUENT_BUYER", 100, False)
    100.0
    """
    discount = get_discount(code, is_member)
    discounted_price = price - discount
    if discounted_price < 0:
        return 0.0
    else: 
        return discounted_price


SHIPPING_RATE = 0.1

def get_shipping(is_member:bool, country:str, price:float) -> float:
    """
    Calculates the shipping cost, shipping is 10% of price before discounts or tax and shipping is free if 
    you are in Canada or you are a member
    >>> get_shipping(True, "Canada", 10.0)
    0.0
    >>> get_shipping(True, "Mexico", 10.0)
    0.0
    >>> get_shipping(False, "Canada", 10.0)
    0.0
    >>> get_shipping(False, "USA", 10.0)
    1.0
    """
    if country == "Canada" or is_member:
        return 0.0
    else:
        return SHIPPING_RATE * price
    
TAX_RATE = 0.08

def display_charges(price:float, tax_rate:float, is_member:bool, discount_code:str, country:str) -> None:
    """
    Preconditions: price >= 0, tax >= 0
    Takes price, tax rate a membership flag, discount code and coutry to ship to and displays a full
    recipt breakdown with tax, shipping, price and a total cost.
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    >>> display_charges(10.0, 5, True, 'TAX_FREE', 'USA')
    price: $ 10.00
    tax: $ 0.50
    shipping: $ 0.00
    total charge: $ 10.50
    >>> display_charges(10, 13, False, 'FREQUENT_BUYER', 'Benin')
    price: $ 10.00
    tax: $ 1.30
    shipping: $ 1.00
    total charge: $ 12.30
    >>> display_charges(1.00, 5, True, 'FREQUENT_BUYER', 'Zambia')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    """
    shipping = get_shipping(is_member, country, price)
    discounted_price = get_discounted_price(discount_code, price, is_member)
    tax = discounted_price * (tax_rate / 100)
    total = discounted_price + tax + shipping
    print(f"price: $ {discounted_price:.2f}")
    print(f"tax: $ {tax:.2f}")
    print(f"shipping: $ {shipping:.2f}")
    print(f"total charge: $ {total:.2f}")