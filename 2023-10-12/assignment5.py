import doctest
from math import log
from sys import set_int_max_str_digits
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

# increase max int->str size to accomodate perfect number calculator
set_int_max_str_digits(1_000_000)


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))

    return die


def list_to_string(values:list[int]) -> str:
    string = ''
    for index, value in enumerate(values):
        string += str(value)
        if index != len(values) - 1:
            string += ','
    return string

def get_sequence(min_val:int, increment:int, max_val:int) -> str:
    """
    Similar to the range() function but instead of returning a itterable,
    return a string with commas separating the values
    >>> get_sequence(2, 5, 32)
    '2,7,12,17,22,27,32'
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    >>> get_sequence(1, 1, 7)
    '1,2,3,4,5,6,7'
    """
    # first create an itterable with the required values
    values = list(range(min_val, max_val + 1, increment))
    return list_to_string(values)


def digit_sum(num:int) -> int:
    """
    Returns the sum of the digits of the absolute value of the number
    given
    >>> digit_sum(-517)
    13
    >>> digit_sum(432)
    9
    """
    sum = 0
    abs_val = abs(num)
    while abs_val >= 1:
        sum += abs_val % 10
        abs_val //= 10
    return sum


def get_factors(num:int) -> list:
    """
    takes a number and returns all possible factors in a list, excluding
    the number itself
    >>> get_factors(6)
    [1, 2, 3]
    >>> get_factors(12)
    [1, 2, 3, 4, 6]
    """
    factor_list = []
    for possible_factor in range(1, num//2 + 1):
        if num % possible_factor == 0:
            # possible factor is a factor, add to factor string
            factor_list.append(possible_factor)
    return factor_list


def sum_factors(num:int) -> int:
    """
    Gets the sum of all possible factors of the given number
    excluding the number itself
    >>> sum_factors(6)
    6
    >>> sum_factors(12)
    16
    """
    sum = 0
    for factor in get_factors(num):
        sum += factor
    return sum


def is_perfect(num:int) -> bool:
    """
    Returns True if the number is a perfect number,
    which is true if the sum of it's factors is equal to 
    itself
    >>> is_perfect(6)
    True
    >>> is_perfect(4)
    False
    """
    return sum_factors(num) == num


""" BELOW IS CODE I HAVE PREVIOUSLY WRITTEN FOR ANOTHER PROJECT"""

# Theorem: pn = n (log n + log log n - 1 + (log log (n) - 2)/log n - ((log log (n))2 - 6 log log (n) + 11)/(2 log2 n)).
def nth_prime(n):
    log_n = log(n)
    log_log_n = log(log_n)
    return round(n * (log_n + log(log(n-1)) + (log_log_n - 2) / log_n - ((log_log_n) * 2 - 6 * log_log_n + 11) / (2 * log(n, 2))))


def get_multiples(num:int, to:int) -> list:
    num_multiples = to // num
    multiples = []
    for i in range(2, num_multiples + 1):
        multiples.append(num * i)
    return multiples


def find_n_primes(num_primes) -> list:
    if num_primes < 1000:
        n = 1000
    else: n = num_primes
    array_len = nth_prime(n)
    return seive_of_eratosthenes(array_len, False)[:num_primes]


def seive_of_eratosthenes(to_num:int, do_debug:bool) -> list:
    # first insstaciate array with len n with increasing numbers from 1
    is_prime:list = [True for i in range(to_num)]

    # create a list of possible factors for all numbers up to to_num
    largest_possible_factor = int(0.5 * to_num)+1
    possible_factors = [factor for factor in range(2, largest_possible_factor)]
    if do_debug: print("All Possible Factors:", possible_factors)

    # loop through each possible_factor and for each possible_factor loop through
    # each multiple of that number to set respective index to false in is_prime
    # list
    for possible_factor in possible_factors:
        # if possible_factor is already determined to not be prime,
        # Do not need to check all of it's multiples because they must have
        # already been determined to not be prime
        if not is_prime[possible_factor - 1]:
            # skip this itteration of possible factors, move onto next
            if do_debug: print("skipped", possible_factor)


        multiples = get_multiples(possible_factor, to_num)
        for multiple in multiples:
            multiple_index = multiple - 1
            if do_debug: print(possible_factor, multiple, "is not prime")
            is_prime[multiple_index] = False

    primes:list = []
    # now we have a list of booleans that repersent which numbers are is_prime
    # convert this to a list of numbers
    for index, bool in enumerate(is_prime):
        if bool:
            primes.append(index + 1)

    return primes[1:]

"""ABOVE IS PREVIOUSLY WRITEN CODE FOR ANOTHER PROJECT"""    

def old_n_perfect_numbers(num_perfects:int) -> str:
    perfects = []
    testing = 1
    while len(perfects) < num_perfects:
        if sum_factors(testing) == testing:
            perfects.append(testing)
        testing += 1
    return list_to_string(perfects)

def n_perfect_numbers(num_perfect_numbers:int) -> list[int]:
    """
    Precondition: num_perfect_numbers <= 914
    finds the first n perfect numbers and returns them as a list
    Done by finding the first n prime numbers and applying the formula
    2^(p-1)(2^p - 1) to each prime to find the perfect numbers
    """
    # Find n primes
    primes = find_n_primes(num_perfect_numbers)
    perfect = lambda prime : (2 ** (prime - 1)) * ((2 ** prime) - 1)
    perfects = list(map(perfect, primes))
    return list_to_string(perfects)
    # largest value returned was 100_000 digits long

    
    