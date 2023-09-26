import doctest

def get_longer(str1: str, str2:str) -> str:
    """
    Takes two stings and returns the longer of the two, if they are equal in length return the first
    >>> get_longer("123", "12")
    '123'
    >>> get_longer("32", "321")
    '321'
    >>> get_longer("", "321")
    '321'
    >>> get_longer("32", "")
    '32'
    """
    if len(str2) > len(str1):
        return str2
    else: 
        return str1


PST = 0.1
GST = 0.05

def get_tax(food:float, alchohol:float) -> float:
    """
    Preconditions: food >= 0 && alchohol >= 0
    Takes the amount of money spent on food and alchohol and returns the amount of tax owed,
    alchohol needs PST and GST while food only requires GST
    >>> get_tax(1.00, 1.00)
    0.2
    >>> get_tax(0, 0)
    0.0
    >>> get_tax(1.0, 0)
    0.05
    >>> get_tax(0, 1.0)
    0.15000000000000002
    """
    food_tax = food * GST
    alchohol_gst = alchohol * GST
    alchohol_pst = alchohol * PST
    return food_tax + alchohol_gst + alchohol_pst


def get_bill_share(food:float, alchohol:float, people:int) -> float:
    """
    Preconditions: food >= 0, alchohol >= 0, people >= 1
    Takes the amount of money spent on food and alchohol and divides it evenly amoung a given number of people and applies the correct tax
    >>> get_bill_share(100, 100, 2)
    110.0
    >>> get_bill_share(0, 0, 1)
    0.0
    >>> get_bill_share(0, 100, 1)
    115.0
    >>> get_bill_share(100, 0, 1)
    105.0
    """
    tax = get_tax(food, alchohol)
    total = food + alchohol + tax
    share = total / people
    return share




doctest.testmod()