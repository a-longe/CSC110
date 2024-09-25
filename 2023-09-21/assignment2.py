import doctest

def check_funds(balance: float, purchase: float):
    """
    Takes your bank balence and a purchace ammount and prints
    how much money you will have left, if you are short money,
    prints how much you are hort and if you are in debt, it will
    tell you that you have a negative bank balance
    >>> check_funds(100, 10)
    you will have $ 90.00 left after this purchase
    >>> check_funds(100, 100)
    you will have $ 0.00 left after this purchase
    >>> check_funds(-10, 0)
    you have a negative balance
    >>> check_funds(100, 120)
    you are short $ 20.00
    """

    remaining_balance = balance - purchase

    if balance < 0:
        print("you have a negative balance")
    elif remaining_balance < 0:
        print(f"you are short $ {abs(remaining_balance):.2f}")
    else:
        print(f"you will have $ {remaining_balance:.2f} left after this purchase")


def print_biggest(num1:float ,num2:float ,num3:float):
    """
    Takes three floating point numbers and calculates which one is the largest
    >>> print_biggest(1,2,3)
    3
    >>> print_biggest(2,3,1)
    3
    >>> print_biggest(3,2,1)
    3
    >>> print_biggest(3,1,2)
    3
    >>> print_biggest(1,3,2)
    3
    >>> print_biggest(2,1,3)
    3
    >>> print_biggest(0,0,1)
    1
    >>> print_biggest(1,-1,-2)
    1
    >>> print_biggest(0,0,0)
    0
    """

    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3:
        # not nessisary to check if num1 > num2 because even if that is true,
        # it means that num3 is greater than num1 and num2 and the conditionals will work
        print(num2)
    else:
        print(num3)


INCHES_IN_FOOT = 12
INCHES_IN_MILE = 5280 * INCHES_IN_FOOT
INCHES_IN_YARD = 3 * INCHES_IN_FOOT


def convert_inches(inches: float):
    """
    Takes a number of inches and converts it to a combinatoion
    of feet, yards and meters
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    """

    miles:int = 0
    yards:int = 0
    feet:int = 0

    miles = inches // INCHES_IN_MILE # find how many miles there are
    inches -= miles * INCHES_IN_MILE # subtract the number of miles as inches
    yards = inches // INCHES_IN_YARD # how many feet are there in the remaining inches
    inches -= yards * INCHES_IN_YARD # subtract that number of feet as inches
    feet = inches // INCHES_IN_FOOT # repeat
    inches -= feet * INCHES_IN_FOOT # ^

    print(f"{miles} mi, {yards} yd, {feet} ft, {inches} in")


def is_multiple_of(num1:int, num2:int):
    """
    Takes two numbers, and determines if the first number is a multiple of the second
    >>> is_multiple_of(8, 2)
    8 is a multiple of 2
    >>> is_multiple_of(9, 2)
    9 is not a multiple of 2
    >>> is_multiple_of(0, 2)
    0 is a multiple of 2
    >>> is_multiple_of(0, 0)
    0 is a multiple of 0
    """
    # if the remainder of one number divided by another number is 0,
    # the first number is a multiple of the second
    if num1 == 0 or num2 == 0 or num1 % num2 == 0:
        print(f"{num1} is a multiple of {num2}")
    else:
        print(f"{num1} is not a multiple of {num2}")


# Discount Codes
FIRST_PURCHASE = "FIRST_PURCHASE"
FIRST_PURCHASE_DISCOUNT = 10
FREQUENT_BUYER = "FREQUENT_BUYER"
FREQUENT_BUYER_DISCOUNT = 2
SHIPPING_RATE = 0.1

def display_charges(purchase_price: float, tax_percentage: float, is_member:bool, discount_code: float, shipping_country:str):
    """
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

    tax:float
    shipping:float
    discounted_price:float = 0
    total_charge:float

    # Calculate price w. discount codes
    if discount_code == FIRST_PURCHASE:
        discounted_price = purchase_price - FIRST_PURCHASE_DISCOUNT
    elif discount_code == FREQUENT_BUYER and is_member:
        discounted_price = purchase_price - FREQUENT_BUYER_DISCOUNT
    else:
        discounted_price = purchase_price

    # quick check to make sure discount_price is not below 0, if it is set discount_price to zero
    if discounted_price < 0:
        discounted_price = 0

    # Calculate tax
    tax = discounted_price * (tax_percentage / 100)

    # Calculate shipping
    if is_member or shipping_country == "Canada":
        shipping = 0
    else:
        shipping = purchase_price * SHIPPING_RATE


    total_charge = discounted_price + tax + shipping

    # Print Result
    print(f"price: $ {discounted_price:.2f}")
    print(f"tax: $ {tax:.2f}")
    print(f"shipping: $ {shipping:.2f}")
    print(f"total charge: $ {total_charge:.2f}")


