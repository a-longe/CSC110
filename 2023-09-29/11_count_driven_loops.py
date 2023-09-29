from doctest import testmod as test

'''
Q1. Design a function that takes an integer n and prints
print the squares of numbers from 0 to n separated by commas.
Your function should assume n is not negative.
'''
        

def print_squares(num_to:int) -> None:
    """
    Precondition: num_to >= 0
    Takes a number to find all the squares of the numbers in between 0 and that given number
    >>> print_squares(5)
    0, 1, 4, 9, 16, 25
    >>> print_squares(0)
    0
    """
    for count in range(0, num_to + 1):
        sqr_num = count ** 2
        print(sqr_num, end="")
        if count < num_to: print(", ", end="")
    print("\n", end="")



'''
Q2. Design a function that takes an integer n and returns
the sum of the squares of numbers from 0 to n.
Your function should assume n is not negative.
'''

def get_sum_squares(num_to:int) -> int:
    """
    Precondition: num_to >= 0
    Takes a number to find all the squares of the numbers in between 0 and that given number, adds them
    together and returns the result
    >>> get_sum_squares(5)
    55
    >>> get_sum_squares(0)
    0
    """
    sum:int = 0
    for count in range(0, num_to + 1):
        sqr_num = count ** 2
        sum += sqr_num
    return sum
        

'''
Q3. Design a function that takes an integer n and returns
a string with the squares of all the numbers from 0 to limit inclusive,
where numbers are separated by commas.
'''

def get_string_squares(num_to:int) -> str:
    """
    Precondition: num_to >= 0
    Returns a tring off all the squares up to a number
    >>> get_string_squares(5)
    '0, 1, 4, 9, 16, 25'
    >>> get_string_squares(0)
    '0'
    """
    string:str = ""
    for count in range(0, num_to + 1):
        sqr_num = count ** 2
        if count < num_to: string += str(sqr_num) + ", "
        else: string += str(sqr_num)
        
    return string

'''
Q4. Design a function that takes an integer n and prints
prints the number n down to 1 followed by 'BLASTOFF!'
Your function should assume n is greater than 0.
'''

EXCLAMATION_STRING = "BLASTOFF!"

def print_countdown(num_to:int) -> None:
    """
    Precondition: num_to >= 0
    Prints a countdown followed by BLASTOFF!
    >>> print_countdown(5)
    5, 4, 3, 2, 1, BLASTOFF!
    >>> print_countdown(1)
    1, BLASTOFF!
    """
    for count in range(num_to, 0, -1):
        print(count, end=", ")
        if count == 1: print(EXCLAMATION_STRING)

'''
Q5. Design a function that takes an integer n and a string and
prints that string n times with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''

def print_string(times:int, string:str) -> None:
    """
    Precondition: num_to >= 0
    Prints a string times number of times with no spaces or newlines
    >>> print_string(5, "ok")
    okokokokok
    >>> print_string(1, "hello")
    hello
    """
    for count in range(times):
        print(string, end="")

'''
Q6. Design a function that takes an integer n and a string and
returns a new string that has the given string repeated n times
with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''

def get_repeating_string(times:int, string:str) -> str:
    """
    Precondition: num_to >= 0
    Returns a string with a substring repeating times number of times
    >>> get_repeating_string(5, "ok")
    'okokokokok'
    >>> get_repeating_string(1, "hello")
    'hello'
    """
    end_string:str = ""
    for count in range(times):
        end_string += string
    return end_string