from doctest import testmod as test

def compute_harmonic_series(largest_denominator:int) -> float:
    """
    Precondition n >= 0
    Takes a number and computes the sum of the sequence 1/1 + 1/2 + 1/3 ... 1/largest_denominator
    >>> compute_harmonic_series(1)
    1.0
    >>> compute_harmonic_series(2)
    1.5
    >>> compute_harmonic_series(3)
    1.8333333333333333
    >>> compute_harmonic_series(0)
    0
    """
    sum = 0
    for denominator in range(1, largest_denominator+1):
        sum += 1/denominator
    return sum

def get_fibonacci_sequence(max_depth:int) -> str:
    """
    The fibonacci sequnece is a sequence where the next number in the sequence is the sum of the previous two numbers
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(2)
    '0, 1'
    >>> get_fibonacci_sequence(5)
    '0, 1, 1, 2, 3'
    >>> get_fibonacci_sequence(9)
    '0, 1, 1, 2, 3, 5, 8, 13, 21'
    """
    fibonacci_list = [0, 1]
    fibonacci_string = ''
    # create sequence as a list
    for depth in range(max_depth):
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)
    # convert list to string
    print(fibonacci_list)
    for index in range(max_depth):
        fibonacci_string += f'{fibonacci_list[index]}, '
    return fibonacci_string[:-2]

def get_string(string:str, times:int) -> str:
    """
    print a given string times number of times
    >>> get_string("test", 5)
    'testtesttesttesttest'
    >>> get_string('&&', 0) 
    ''
    """
    return string * times

def print_pattern(height:int, width:int, string1:str, string2:str) -> None:
    """
    Preconditions: height > 0, width > 0
    Print a rectangle with a repeating pattern with the even rows starting with string1 and odd rows starting with string2
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    """
    for row in range(height):
        if not row % 2: # equivilant to row % 2 == 0 because 0 is equ. to false
            # even number row
            print(get_string((string1 + string2), width))
        else:
            # odd number row
            print(get_string((string2 + string1), width))