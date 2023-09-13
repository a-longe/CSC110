import math

PST = 0.07
GST = 0.05

test_variable = 100


# def print_bill(price: float):
#     """ print the bill breakdown for an item of given price
#     >>> print_bill(0)
#     item:	$   0.00
#     PST:	$   0.00
#     GST:	$   0.00
#     total:	$   0.00
#     >>> print_bill(43.99)
#     item:	$  43.99
#     PST:	$   3.08
#     GST:	$   2.20
#     total:	$  49.27
#     """
#     pst_charge = price * PST
#     gst_charge = price * GST
#     total = price + pst_charge + gst_charge

#     print(f'item:  ${price}')
#     print(f'PST:   ${pst_charge}')
#     print(f'GST:   ${gst_charge}')
#     print(f'total: ${total}')


'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
Fix it so the prices to print to 2 decimal places.
'''

def print_bill(price: float):
    """ print the bill breakdown for an item of given price
    >>> print_bill(0)
    item:	$   0.00
    PST:	$   0.00
    GST:	$   0.00
    total:	$   0.00
    >>> print_bill(43.99)
    item:	$  43.99
    PST:	$   3.08
    GST:	$   2.20
    total:	$  49.27
    """
    pst_charge = price * PST
    gst_charge = price * GST
    total = price + pst_charge + gst_charge

    print(f'item:  ${price:.2f}')
    print(f'PST:   ${pst_charge:.2f}')
    print(f'GST:   ${gst_charge:.2f}')
    print(f'total: ${total:.2f}')

'''
Q1b.
If I uncomment each of the following lines what will the output be?
'''
# print_bill(43.99)
# >>> print_bill(43.99)
# ==> item:  $43.99
#     PST:   $3.08
#     GST:   $2.20
#     total: $49.27
# >>> print(GST)
# ==> 0.05
# >>> print(PST)
# ==> 0.07
# >>> print(pst_charge)
# ==> NameError: name 'pst_charge' is not defined
# >>> print(gst_charge)
# ==> NameError: name 'gst_charge' is not defined


'''
Q2a. What is the output if the function foo is called?
Documentation and type hints ommitted for demonstration purposes.
Q2b. What happens if we remove the following line from foo: test_variable = 1
Q2c. What happens if we remove the following line from bar: x = 5.5
'''


def foo():
    x = 4.5
    # test_variable = 1
    bar()
    print('in foo:', x, test_variable)


def bar():
    global test_variable
    test_variable = 500
    x = 5.5
    print('in bar:', x, test_variable)

# 2a:
# in bar: 5.5 500
# in foo: 4.5 1

# 2b:
# in bar: 5.5 500
# in foo: 4.5 500

# 2c:
# NameError: name 'x' is not defined

'''
Q3. What is the output if the function baz is called
Documentation and type hints ommitted for demonstration purposes.
'''


def goo(y):
    x = 5.5
    y += 2
    print('in goo:', x, y)


def baz():
    x = 4.5
    y = 10
    goo(x)
    print('in baz:', x, y)

"""
in goo: 5.5 6.5
in baz: 4.5 10
"""


'''
Q4. Design a function that takes a temperature in Celcius as a whole number
and calculates the corresponding temperature in Farenheit
and prints the result rounded down to the nearest whole number
Recall: degrees farenheit = 9 / 5 * degrees celcius + 32
'''

C_TO_F_CONVERSION_RATE = 9/5
C_TO_F_CONVERSION_OFFSET = 32

def celcius_To_Farenheit(c:int):
    """
    Takes a whole number in degrees celcius and returns the corrosponding farenheit value
    >>> celcius_To_Farenheit(1)
    ==> 33.8
    >>> celcius_To_Farenheit(o)
    ==> 32.0
    """
    farenheit = ((C_TO_F_CONVERSION_RATE) * c) + C_TO_F_CONVERSION_OFFSET
    print(f"{farenheit:.0f}")

'''
Q5. Design a function that takes the length of the hypotenuse of a right angle
triangle and one of the non-90 degree angle measurements in the triangle.
The function should calculate the length of side adjacent to the given angle
and print the result to the screen.

RECALL: cos(angle in degrees) = adjacent / hypotenuse

You will want to use the cos function from the math library!
Use the help function to find the documentation for math.cos
and remember to import the math library
by adding the following line to the top of this file:
import math

RECALL: 1 degree = PI/180 radians
Use the dir function to see what other useful functions
the math module has by typing dir(math) in your shell
NOTE: the math module also has a radians function that you can use
instead of using the formula above to convert degrees to radians!

here is a calculator to help you come up with examples for testing:
https://www.calculator.net/right-triangle-calculator.html
'''

RADIAN_CONVERSION = math.pi/180

def get_adjacent_length(hyp:float, angle:float):
    """
    Take the length of the hypotenuse and one non-90 degree angle, then calculate and print the adjacent side length
    >>> get_adjacent_length(2 ** 0.5, 45)
    ==> 1.0
    >>> get_adjacent_length(2, 30)
    ==> 1.7320508075688772
    """

    # cos(angle(radians)) = adj/hyp
    # adj = cos(angle(radians)) * hyp

    # 1 degree = pi/180 radians
    # radians = degrees * (pi/180)

    angle_in_radians = angle * RADIAN_CONVERSION
    adj = math.cos(angle_in_radians) * hyp
    print(adj)


'''
Q6. Design a function that takes an item weight in kilograms and
calculates the corresponding weight in pounds and prints the
result with 2 decimal places on the screen.
We assume a conversion rate of 2.2 pounds per kilogram.
'''

KG_TO_LB_CONVERSION_RATE = 2.2

def kg_to_lb(kg:float):
    """
    Takes a number of kilograms and converts it into pounds
    >>> kg_to_lb(1)
    ==> 2.20
    >>> kg_to_lb(100)
    ==> 220.00
    """
    lb = kg * KG_TO_LB_CONVERSION_RATE
    print(f'{lb:.2f}')