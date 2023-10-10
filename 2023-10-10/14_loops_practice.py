import doctest
VOWELS = ["a", "e", "i", "o", "u"]


'''
Q1. Design a function called num_chars_before_vowel that takes a string
and counts and returns the number of characters in that string up to the
first vowel encountered.
NOTE: we are calling the following vowels - a,e,i,o,u

Use a while loop in your solution!
'''

def num_chars_before_vowel(string:str) -> int:
    """
    takes a string and counts the number of characters before the first vowel
    >>> num_chars_before_vowel("hello world")
    1
    >>> num_chars_before_vowel('arbitrary')
    0
    >>> num_chars_before_vowel("   this is a test")
    5
    """
    index = 0
    while string[index].lower() not in VOWELS:
        index += 1
    return index

'''
Q2. Design a function that takes an integer and determines whether
it is prime or not.
NOTE: a number is prime if it is a positive number
divisible by 2 unique numbers, 1 and itself.
1 is not considered a prime number.
'''

def get_factors(num:int) -> list:
    """
    takes a number and returns all possible factors in a list
    """
    factor_list = []
    for possible_factor in range(1, num//2 + 1):
        if num % possible_factor == 0:
            # possible factor is a factor, add to factor string
            factor_list.append(possible_factor)
    factor_list.append(num)
    return factor_list

def is_prime(num:int) -> bool:
    factors = get_factors(num)
    return len(factors) == 2

'''
Q3. Design a function that takes an integer n and prints the first n prime
numbers that exist with a comma between each.
Your function can assume n is not negative.
'''

def get_n_primes(num_primes:int) -> str:
    prime_str = ''
    prime_counter = 0
    num_testing = 1
    while prime_counter < num_primes:
        if is_prime(num_testing):
            if prime_counter != num_primes - 1: prime_str += f'{str(num_testing)},'
            else: prime_str += str(num_testing)
            prime_counter+=1
        num_testing+=1
    return prime_str




'''
Q4. Design a function that will take a number representing the size
and prints a pattern of slashes as demonstrated in the examples below
relative to the given size.
You can assume that size is greater than 0
Examples:
if size is 1, prints:
/
if size is 3, prints:
///
//\
/\\
if size is 4, prints:
////
///\
//\\
/\\\
'''


'''
Q5. Design a function that takes a non-negative number and
produces the given pattern as output:

if given 3 the following is printed:
123
234
345

if given 5 the following is printed:
12345
23456
34567
45678
56789
'''
