import doctest
import math


'''
Q1. This is a function I left you to complete in a previous lecture
Update this function so it returns the length of the adjacent side.
Design a second function that will return the length of the opposite side.
'''


def get_adjacent_length(hypotenuse: float, angle: float) -> float:
    """ calculates and prints the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    Precondition: hypotenuse and angle > 0
    >>> get_adjacent_length(13.2, 60)
    6.600000000000001
    >>> get_adjacent_length(28.7, 29.8)
    24.904868511688246
    """
    radians = math.radians(angle)  # using built-in radians function
    adjacent = math.cos(radians) * hypotenuse
    return adjacent


'''
Q2. Design a new function that takes the length the hypotenuse of a triangle
and the angle (in degrees) of one of the non-right angles,
and calculates and returns the perimeter of the triangle.
'''

def get_triangle_perimeter(hypotenuse:float, angle:float) -> float:
    """
    Takes the length of the hypotenuse and an angle in degrees to find all the side lengths 
    and add them together to find the perimeter
    >>> get_triangle_perimeter(1.4142135623730951, 45)
    3.414213562373096
    >>> get_triangle_perimeter(2, 30)
    4.732050807568878
    """
    # we know two angles of this triangle so we can also wind the final angle because
    # all the angles must add to 180
    angle1 = angle
    angle2 = 90 - angle # 180 - 90(right angle tirangle) - angle

    side1 = get_adjacent_length(hypotenuse, angle1)
    side2 = get_adjacent_length(hypotenuse, angle2)

    return hypotenuse + side1 + side2

'''
Q3. Design a new function that takes the length of the hypotenuse of a triangle
and the angle in degrees of one of the non-right angles, and prints the
name of the longest side other than the hypotenuse.

The function should print:
-adjacent if the side adjacent to the given angle
 is the longest side after the hypotenuse
-opposite if the side opposite to the given angle
 is the longest side after the hypotenuse
-equal if the adjacent and opposite sides to the given angle
 are less than 0.01 different from each other
'''

EQUALITY_THRESHOLD = 0.01

def print_longest_triangle_side(hypotenuse:float, angle:float) -> None:
    """
    Precondition: angle < 90
    Takes the hypotenusre and an angle and prints where the longest side is in relation to the angle given
    >>> print_longest_triangle_side(1.4142135623730951, 45)
    equal
    >>> print_longest_triangle_side(2, 30)
    adjacent
    >>> print_longest_triangle_side(2, 60)
    opposite
    """

    primary_angle = angle
    secondary_angle = 90 - angle

    adjacent_length = get_adjacent_length(hypotenuse, primary_angle)
    opposite_length = get_adjacent_length(hypotenuse, secondary_angle)

    difference = adjacent_length - opposite_length
    if abs(difference) <= EQUALITY_THRESHOLD:
        print("equal")
    elif adjacent_length > opposite_length:
        print("adjacent")
    else:
        print("opposite")

'''
Q4. Design a function that takes two strings and returns the
result of those two strings joined together.
'''
def join_string(str1:str, str2:str) -> str:
    return str1 + str2


"""
Q5. Design a function that takes a string and two integers
The integers repersent the start and end point (inclusive) of a substring with the given string
The functuon should return the substring with the given start and end points
"""

def get_substring(string:str, start:int, end:int) -> str:
    """
    Preconditions: start >= 0, end >= start
    Returns the substring with given start and end points (inclusive)
    >>> get_substring("hello world", 3, 7)
    'lo wo'
    """
    return string[start:end+1]