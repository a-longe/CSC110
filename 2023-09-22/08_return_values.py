import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

'''
Q0. Design a function that will take two numbers and
returns the sum of those numbers
'''

def sum (num1: float, num2:float) -> float:
    """
    Returns the sum of the two given numbers
    >>> sum(0, 0)
    0
    >>> sum(1, 1)
    2
    >>> sum(-5, -2)
    -7
    >>> sum(2.2, 3.6)
    5.800000000000001
    """
    sum = num1 + num2
    return sum

'''
Q0b. Design a function that will take two numbers and prints the average
of those numbers.
In your function body, call the funtion desiged in Q1a
to practice calling a function from another function.
'''

def print_avg(num1: float, num2:float) -> None:
    """
    Takes two numbers and uses sum to calculate the average of the two numbers
    >>> print_avg(1, 1)
    1.0
    >>> print_avg(2, 2)
    2.0
    >>> print_avg(-3, -3)
    -3.0
    >>> print_avg(0, 0)
    0.0
    >>> print_avg(-10, 3)
    -3.5
    """
    avg = sum(num1, num2) / 2
    return avg

'''
Q0c. If the function you designed in Q0a printed the sum instead of
returning it, would you average function still behave as expected?
'''

# no

'''
Q1. Below is the print_fare function we wrote in a past lecture.
Continuing in this problem domain, design a separate function that takes
the number of children, number of adults and number of seniors
and returns the total fare for those riders.
You function should take into acount a group discount of 10%
for groups of 10 or more.
You can assume the function will not be passed negative values.

NOTICE: print_fare does not return a value, so calling it will not be useful
BUT, there are CONSTANTS defined that might be useful!
'''

def total_fare(children:int, adults:int, seniors:int) -> float:
    """
    Takes The number of each group of people taking a bus and returns the total
    cost
    """
    total_fare:float = 0
    total_fare += children * CHILD_RATE
    total_fare += adults * ADULT_RATE
    total_fare += seniors * SENIOR_RATE
    return total_fare


def print_fare(age: int) -> None:
    """ determines the bus fare for a rider of the given age and prints it
    Precondition: age > 0
    >>> print_fare(0)
    The fare is: $1.50
    >>> print_fare(ADULT-1)
    The fare is: $1.50
    >>> print_fare(ADULT)
    The fare is: $2.50
    >>> print_fare(ADULT+1)
    The fare is: $2.50
    >>> print_fare(SENIOR-1)
    The fare is: $2.50
    >>> print_fare(SENIOR)
    The fare is: $2.00
    >>> print_fare(SENIOR+1)
    The fare is: $2.00
    """
    fare = 0
    if age < ADULT:
        fare = CHILD_RATE
    elif age >= SENIOR:
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE

    print(f'The fare is: ${fare:.2f}')


'''
Q2. design a function that takes the amount of money in a bank account and
the number of children, number of adults and number of seniors.
You can assume the function will not be passed negative values for
number of people, but the account balance can be negative.

The function should print the total fare for all of these people and
the balance left in the bank account after the fare is paid.
The function should return the balance left in the bank account
after the fare is paid.
'''

def print_remaining_balence(balance:float, children:int, adults:int, seniors:int):
    print(balance - total_fare(children,adults,seniors))


''' Q3. Recall we designed the following function in a past lecture.
Update this function so it does not print the roman numeral,
but instead returns it.'''


ROMAN_VALUE_V = 5
ROMAN_VALUE_X = 10

def print_roman_numeral(num: int) -> None:
    """ determines and prints the corresponding roman numeral for the given num
    Precondition: 1 <= num <=10
    >>> print_roman_numeral(1)
    'I'
    >>> print_roman_numeral(2)
    'II'
    >>> print_roman_numeral(3)
    'III'
    >>> print_roman_numeral(4)
    'IV'
    >>> print_roman_numeral(5)
    'V'
    >>> print_roman_numeral(6)
    'VI'
    >>> print_roman_numeral(7)
    'VII'
    >>> print_roman_numeral(8)
    'VIII'
    >>> print_roman_numeral(9)
    'IX'
    >>> print_roman_numeral(10)
    'X'
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
    
    return roman_string