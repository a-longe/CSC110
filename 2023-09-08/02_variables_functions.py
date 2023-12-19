#!/usr/bin/env python3

'''
Q0. The following code attempts to print the total price
of a group of items I would like to buy followed by
the amount of money I will have left in my wallet.
My wallet started with 200 dollars.
There are a few things wrong with this program.
What do you think is wrong and how would you fix it?
'''

CURRENCY_GLYPH = "$"

wallet = 200
cost_of_items = 3+4+6+14
wallet -= cost_of_items

print('total of item prices:', CURRENCY_GLYPH , wallet)
print('wallet balance:', CURRENCY_GLYPH , 200 - wallet)


'''
Q1a. Recall from your math classes that the equation for
the lengths of the sides in a right triangle is:
  a^2 + b^2 = c^2
- using the ^ to indicate "raise to the power of" in the description
- how is "raise to the power of" represented in Python?

Write the code that will print the length of side c of
a right triangle with side a length as 3 and side length b as 4.
'''

import math

a = 3
b = 4
# c = (a**2 + b**2)**0.5  # 0.5 is equivialnt to square root
c = (a**2 + b**2) ** 0.5
print("hypotenuse length:", c)

'''
Q1b. Update the program you just wrote so
it is contained within a function.
Test the function by calling it from the shell.
'''

def hyp(a, b):
    c = math.sqrt(a**2 + b**2)
    print("hypotenuse:", c)
    return c

'''
Q1c. complete the function below so it prints the lengths
of all sides of the right triangle.
Try to avoid re-writing code you have already written!

Test the function by calling it from the shell.
Your output should look something like this...

Dimensions of this right triangle:
the short sides are length: 3 and 4
the hypotenuse is length:  5.0
'''


def print_right_triangle_dimensions():
    a = 3
    b = 4
    c = hyp(a, b)
    print("Sides of the triangle:", a, b, c)

'''
Q2. What does the following code print when uncommented?
Rewrite this code so that it is contained in a function
and both the code and the output makes it more clear
what the program is doing.
Test your function by calling it from the shell
'''
#print(3.14 * 3.4 ** 2, ',', 2 * 3.14 * 3.4)

# print the circumference and area of a circle given it's radius
def print_area_circumference_circle(r):
    PI = 3.14
    area = PI * r**2
    circumference = 2 * PI * r
    print("area:", area, "circumference:", circumference)

'''
Q3. Design a function that prints the area of
a 5.7 acre plot of land in square metres
Assume that 1 acre is 4046.85642 square metres
'''

acres = 5.7
ACRE = 4046.85642

print("5.7 acres -> square metres:", ACRE * acres)


if __name__ == "__main__":
    hyp(3, 4)
    print_right_triangle_dimensions()
    print_area_circumference_circle(3.4)