from doctest import testmod as test


'''
Q1. Design a function that takes a string and 2 numbers
representing height and width.
The function should print a rectangular pattern using the given string
that is of dimension width by height.
You can assume that height and width are not negative and the string is not empty
Example. if the string is '*#' and height is 4 and width is 3, it should print:
*#*#*#
*#*#*#
*#*#*#
*#*#*#
You must not use the * operator to repeat your string.
'''

def get_string(string:str, times:int) -> str:
    return string * times

def print_pattern(string:str, width:int, height:int) -> None:
    """
    Takes a string and prints it width number of times on a row and prints height number of rows
    >>> print_pattern('*#', 3, 4)
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
    """
    for row in range(height):
        print(get_string(string, width), end="")
        print("\n", end="")

'''
Q2. Design a function that will take a number representing height and it
should print a right angle triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
*
**
if ht is 3, prints:
*
**
***
'''

def print_asterisk_triangle(height:int) -> None:
    """
    Takes a height parameter and prints out a astrisk reperentation of a right angle triangle using '*'
    >>> print_asterisk_triangle(2)
    *
    **
    >>> print_asterisk_triangle(3)
    *
    **
    ***
    """
    for row in range(1, height+1):
        print(get_string("*", row))


'''
Q3. Design a fucntion that takes a non-negative number that represents a size
and prints a number pattern according to the size.
You can assume that size is greater than or equal to 0
Examples:
if the size is 3 it prints...
3
32
321
if the size is 5 it prints...
5
54
543
5432
54321
'''
def print_decreasing_num_pattern(num:int) -> None:
    """
    Takes a number and prints the below pattern
    >>> print_decreasing_num_pattern(3)
    3
    32
    321
    >>> print_decreasing_num_pattern(5)
    5
    54
    543
    5432
    54321
    """

    for row in range(1, num+1):
        for index in range(row):
            print(num - index, end="")
        print("\n", end="")
            

'''
Q4. Design a function that will take a number representing height and it
should print an isosceles triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
TIP: to get the stars to appear centered, think about how many space (' ')
characters to print on a row before you print the * characters.
Examples:
if ht is 2, prints:
 *
***
if ht is 3, prints:
  *
 ***
*****
'''

def print_asterisk_isosceles(height:int) -> None:
    """
    creates an isosceles triangle out of asterisks and prints it out
    >>> print_asterisk_isosceles(2)
     *
    ***
    >>> print_asterisk_isosceles(3)
      *
     ***
    *****
    """
    for row in range(height):
        num_asterisks = 1 + row * 2
        num_spaces = height - 1 - row
        print(get_string(' ', num_spaces), get_string('*', num_asterisks), sep="")
   


'''
Q5. Design a function that will take a number representing height and it
should print a diamond using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
 *
***
 *
if ht is 3, prints:
  *
 ***
*****
 ***
  *
'''

def print_mirrored_asterisk_isosceles(height:int, shift_right:int=0) -> None:
    """
    prints a upside down isosceles triangle with given height
    >>> print_mirrored_asterisk_isosceles(3)
    *****
     ***
      *
    >>> print_mirrored_asterisk_isosceles(2)
    ***
     *
    """
    for row in range(1, height+1):
        num_asterisks = (height-row) * 2 + 1
        num_spaces = row - 1
        print((" " * shift_right), get_string(' ', num_spaces), get_string('*', num_asterisks), sep="")


def print_asterisk_diamond(height:int) -> None:
    print_asterisk_isosceles(height)
    print_mirrored_asterisk_isosceles(height - 1, shift_right=1)