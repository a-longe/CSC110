import doctest

'''
Q1. Design a function that will take a whole number and
prints the number and prints whether it is odd or not
'''

def print_is_odd(num:int):
    """
    Takes a whole number and prints out odd or not odd
    >>> print_is_odd(5)
    5 is odd
    >>> print_is_odd(2)
    2 is not odd
    """
    is_odd = (num % 2) != 0
    if is_odd:
        print(f"{num} is odd")
    else:
        print(f"{num} is not odd")


'''
Q2. Design a function that takes two numbers and prints
the smallest value.  Do not use the builtin min function.
'''

def print_min_value(value1: float, value2:float):
    """
    Takes two numbers and prints the smallest value
    >>> print_min_value(1, 2)
    1
    >>> print_min_value(76.2, 68.9)
    68.9
    >>> print_min_value(5, 5)
    5
    """
    if value1 > value2:
        print(value2)
    else:
        print(value1)


'''
Q3. Design a function that takes one argument: a person's age
and determines and prints the cost of
riding the bus based on that given age.
Your function should assume age is not negative.

If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.
'''

YOUTH_FARE = 1.50
SENIOR_FARE = 2.00
ADULT_FARE = 2.50

YOUTH_MAX_AGE = 18
SENIOR_MIN_AGE = 65

def print_bus_fare(age:float):
    """
    Takes a persons age and prints out how much a bus ticket will cost: < 18 is $1.50, > 65 is $2.00 and anything else is $2.50
    >>> print_bus_fare(17)
    $1.50
    >>> print_bus_fare(18)
    $2.50
    >>> print_bus_fare(70)
    $2.00
    >>> print_bus_fare(65)
    $2.00
    """

    if (age < YOUTH_MAX_AGE):
        fare = YOUTH_FARE
    elif (age >= SENIOR_MIN_AGE):
        fare = SENIOR_FARE
    else:
        fare = ADULT_FARE
    
    print(f"${fare:.2f}")


'''
Q4. Design a function that takes a number within the range of 1 through 10.
The function should assume it will only be called with numbers 1 to 10.
The function should display the Roman numeral version of that number.
The following list shows the Roman numerals for the numbers 1 through 10:

Number:	Roman Numeral
1	I
2	II
3	III
4	IV
5	V
6	VI
7	VII
8	VIII
9	IX
10	X
'''

ROMAN_VALUE_X = 10
ROMAN_VALUE_V = 5
ROMAN_VALUE_I = 1

def print_roman_from_int(num:int):
    """
    Precondition: 1 <= num <= 10
    Takes an integer (1-10) and prints the roman number equivilant
    >>> print_roman_from_int(9)
    IX
    >>> print_roman_from_int(6)
    VI
    >>> print_roman_from_int(5)
    V
    >>> print_roman_from_int(3)
    III
    >>> print_roman_from_int(1)
    I
    """

    roman_string = ""

    # convert num to a string with num Is
    roman_string = ("I" * num)

    # replace 10 Is with X
    roman_string = roman_string.replace(("I" * ROMAN_VALUE_X), "X")

    # replace 5 I's with V
    roman_string = roman_string.replace(("I" * ROMAN_VALUE_V), "V")

    # replace VIIII with IX
    roman_string = roman_string.replace("VIIII", "IX")

    # replace IIII with IV
    roman_string = roman_string.replace("IIII", "IV")
    
    print(roman_string)

doctest.testmod()


