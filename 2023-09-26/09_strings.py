import doctest
import math

'''
Q0.These functions appear to have similar behaviours but are very different.
'''

# Q0a. What is the difference between the expected output in the
# tests for these 2 functions?

# ONe of them returns a string while the other does not return anything but prints the string

def string_return() -> str:
    """ demonstrate returning a string
    >>> string_return()
    'error'
    """
    value = 'error'
    return value


def string_print() -> None:
    """ demonstrate printing a string
    >>> string_print()
    error
    """
    value = 'error'
    print(value)

# The differences become much more clear when you call them....

# Q0b. if I execute the following code what is printed:
# returned_value = string_return()
# print(returned_value)
# error

# Q0c. given your answer above, can I do this:
# sliced_str = returned_value[0:4]
# print(sliced_str)
# erro


# Q0d. if I execute the following code what is printed:
# returned_value = string_print()
# print(returned_value)
# error
# None

# Q0e. given your answer above, can I do this:
# sliced_str = returned_value[0:4]
# print(sliced_str)
# yes


'''
Q1. Design a function that will take a word and determine whether
it is plural or not (ends with the letter s)
Assume any word that ends with s is plural (ie. pass is considered plural)
'''

def is_plural(string:str) -> bool:
    """
    Takes a string and determines if the last letter in the string is 's'
    If it is, the string is plural, otherwise the string is not plural
    >>> is_plural("pass")
    True
    >>> is_plural("train")
    False
    >>> is_plural("")
    False
    >>> is_plural("trains")
    True
    """
    return len(string) > 0 and string[-1] == 's'
        

'''
Q2. Design a function that pluralizes a word if it is not already plural
The function should return a pluralized word (s added to the end).
We are going to assume anything with an s at the end is already pluralized.
'''

def pluralize(string:str) -> str:
    """
    If the given string does not end with the letter s, add the letter s and return if it is already plural
    return the string anyway
    >>> pluralize("pass")
    'pass'
    >>> pluralize("train")
    'trains'
    >>> pluralize("")
    's'
    >>> pluralize("trains")
    'trains'
    """
    if is_plural(string):
        return string
    else:
        return string + 's'

'''
Q3. Design a function that takes a string and determines whether it
is composed of exactly 2 repeating strings ie. 'abcabc' is a repeating string.
'''

def is_two_repeating_strings(string:str) -> bool:
    """
    If the string is made of two repeating strings return true, otherwise return false
    >>> is_two_repeating_strings("abcabc")
    True
    >>> is_two_repeating_strings("")
    True
    >>> is_two_repeating_strings("a")
    False
    >>> is_two_repeating_strings("aba")
    False
    >>> is_two_repeating_strings("abab")
    True
    """
    half_index = len(string) // 2
    first_half = string[:half_index]
    second_half = string[half_index:]
    return first_half == second_half

'''
Q4. Design a function that takes the amount of time an
object takes to fall after being dropped in seconds.
The function calculates and returns the distance the object fell in meters,
where the formula for distance is:
        d = 1/2 gt^2
        where t is the time in seconds and
        g is gravitational acceleration constant at 9.8 m/s^2
        d is in meters
If the function is passed a negative value for time it should
return the value -1 to indicate an error.
'''
FORCE_OF_GRAVITY = 9.8
ERROR_VALUE = -1

def distance_fallen(sec:float) -> float:
    """
    Takes the time is seconds that it took for the object to fall, calculate the distance using kinetics equasions
    >>> distance_fallen(-5)
    -1
    >>> distance_fallen(0)
    0.0
    >>> distance_fallen(1)
    4.9
    """
    if sec < 0:
        return ERROR_VALUE
    
    # Formula: d = 1/2 * g * t^2
    distance = 0.5 * FORCE_OF_GRAVITY * (sec ** 2)
    return distance

'''
Q5. Design another function that takes the distance in meters from a point
to the ground and a time in seconds.  The function should determine whether
the object will hit the ground in the given time.
The function should assume that both time and distance are not negative.
Make use of the previous function!
'''

def is_hit_ground(sec:float, height:float) -> bool:
    """
    Precondition sec >= 0, height >= 0  
    Takes the amount of time in the air and the height of the object and determines if the object hit the ground
    >>> is_hit_ground(0, 0)
    True
    >>> is_hit_ground(0, 10)
    False
    >>> is_hit_ground(10, 0)
    True
    """
    return distance_fallen(sec) >= height
