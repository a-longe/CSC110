import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

NUM_BUNS_PER_PACK = 8
NUM_DOGS_PER_PACK = 12

'''
Q1. You were asked to design a function that determines the cost of
riding the bus based on the value of the argument age of type int.
If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.

A friend of yours submitted the following code but was deducted marks for:
-inappropriate use of branching constructs
-redundant Boolean expressions
-magic numbers
-insufficient test coverage
-missing units in output

Edit the function in light of the feedback from the marker.
'''

def print_fare(age: int):
    """ determines the bus fare for a rider of the given age and prints it

    Precondition: age > 0
    >>> print_fare(15)
    $1.50
    """

    if (age < ADULT):
        fare = CHILD_RATE
    elif (age >= SENIOR):
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE
    
    print(f"${fare:.2f}")


'''
Q2. The following function design fails some of the given
example tests but there is more than one problem with it.
Find and fix the problems.
'''


def print_roman_numeral(num: int):
    """ determines and prints the corresponding roman numeral for the given num

    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(6)
    VI
    >>> print_roman_numeral(7)
    VII
    >>> print_roman_numeral(8)
    VIII
    >>> print_roman_numeral(9)
    IX
    >>> print_roman_numeral(10)
    X
    """
    roman_numeral = ''

    if num == 1:
        roman_numeral = 'I'
    elif num == 2:
        roman_numeral = 'II'
    elif num == 3:
        roman_numeral = 'III'
    elif num == 4:
        roman_numeral = 'IV'
    elif num == 6:
        roman_numeral = 'VI'
    elif num == 7:
        roman_numeral = 'VII'
    elif num == 8:
        roman_numeral = 'VIII'
    elif num == 9:
        roman_numeral = 'IX'
    else:
        roman_numeral = 'X'

    print(roman_numeral)


'''
Q3. Design a function that takes 2 numbers representing an (x,y) point on a
graph and prints what quadrant it is in.  RECALL:  quadrants are numbered
1 through 4 counter clockwise starting at the upper right quadrant.

The function should print: '(x# , y#)' where x# and y# are the x,y arguments
if x and y are zero it should then print 'at center'
otherwise if x or y are zero it should print which axis it is on:
'on x-axis' or 'on y-axis'
otherwise it should print 'Q#' where # is the quadrant number it is in
'''

def print_location_from_point(x:float, y:float):
    """
    Find where a point on a cartisian plane is
    First determine if it is in a quadrant
    Then test if it is on a axis
    Else must be in the centre
    >>> print_location_from_point(0, 0)
    (0 , 0) at centre
    >>> print_location_from_point(1, 0)
    (1 , 0) on x-axis
    >>> print_location_from_point(-1, 0)
    (-1 , 0) on x-axis
    >>> print_location_from_point(0, 1)
    (0 , 1) on y-axis
    >>> print_location_from_point(0, -1)
    (0 , -1) on y-axis
    >>> print_location_from_point(1, 1)
    (1 , 1) Q1
    >>> print_location_from_point(-1, -1)
    (-1 , -1) Q3
    >>> print_location_from_point(-1, 1)
    (-1 , 1) Q2
    >>> print_location_from_point(1, -1)
    (1 , -1) Q4
    """

    suffix = ""

    if x == 0 and y == 0:
        suffix = "at centre"
    elif x == 0:
        suffix = "on y-axis"
    elif y == 0:
        suffix = "on x-axis"
    else:
        # must be in a quadrant
        if x > 0:
            # must be Q1 or Q4
            if y > 0:
                # Must be Q1
                suffix = "Q1"
            else:
                # Must be Q4
                suffix = "Q4"
        else:
            # must be Q2 or Q3
            if y > 0:
                # must be Q2
                suffix = "Q2"
            else:
                # must be Q3
                suffix = "Q3"
    
    print(f"({x} , {y}) {suffix}")




'''
Q4. Design a function that takes two numbers:
one for air temperature (in degrees Celsius) and
one for air pressure(in pounds per square inch, psi) inside a mechanical device
The function should print the message "Error: data not valid",
if the pressure is negative, and then terminates
otherwise it should print a message about the machine's operation
according to the following:
If the temperature is above 300 degrees C or below 5 degrees C, or if the
pressure is above 150psi, the machine is not operating under normal conditions.

If the temperature is above 250 degrees C and the pressure is above 100psi,
the machine is not operating under normal conditions.
Otherwise, the machine is operating under normal conditions.

TIP: the temperature and pressure thresholds are all constant value
that should not change during your program.  How/where should you define them?
'''

THRESHOLD_PRESSURE_ERROR = 0
LOWER_TEMPATURE_ISOLATED_THRESHOLD = 5
UPPER_TEMPATURE_ISOLATED_THRESHOLD = 300
UPPER_PRESSURE_ISOLATED_THRESHOLD = 150
UPPER_TEMPATURE_PARTNERED_THRESHOLD = 250
UPPER_PRESSURE_PARTNERED_THRESHOLD = 100

def print_machine_status(tempature: float, pressure:float):
    """
    Takes air pressure and air pressure to determine the operating status of the machine
    >>> print_machine_status(-5, -1)
    Error: data not valid
    >>> print_machine_status(50, 50)
    Machine operating in normal conditions
    >>> print_machine_status()
    """
    if pressure < THRESHOLD_PRESSURE_ERROR:
        print("Error: data not valid")
    elif tempature > UPPER_TEMPATURE_ISOLATED_THRESHOLD or tempature < LOWER_TEMPATURE_ISOLATED_THRESHOLD or pressure > UPPER_PRESSURE_ISOLATED_THRESHOLD or (tempature > UPPER_TEMPATURE_PARTNERED_THRESHOLD and pressure > UPPER_PRESSURE_PARTNERED_THRESHOLD):
        print("Machine operating outside of normal conditions")
    else:
        print("Machine operating in normal conditions") 


'''
Q5. Write a function that takes the number of people coming
    to a picnic and prints the nubmer of packages of hot dogs and buns to buy
    assume: each person will eat 2 hot dogs and
    the number of buns in a package is NUM_BUNS_PER_PACK and
    the number of dogs in a package is NUM_DOGS_PER_PACK and
Tip: if you know you need 16 hot dogs and there are 8 buns per pack and
12 dogs per pack, you need to know how many whole bags of each you need,
plus an extra bag if the whole bags are not quite enough.
Think about how the results of the following expressions help:
16 // 8
16 % 8
16 // 12
16 % 12
'''

HOT_DOGS_PER_PERSON = 2

def print_needed_hot_dog_and_buns_packages(ppl: int):
    hd_needed = ppl * HOT_DOGS_PER_PERSON
    buns_needed = ppl * HOT_DOGS_PER_PERSON

    hd_packages = hd_needed // NUM_DOGS_PER_PACK
    bun_packages = buns_needed // NUM_BUNS_PER_PACK
    print(f"we need {hd_packages} hot dog pakages and {bun_packages} packages of buns")
