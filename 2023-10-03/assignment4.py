from doctest import testmod as test

def get_factors(num:int) -> str:
    """
    Get a string containing all the factors up to a given value
    >>> get_factors(12)
    '1,2,3,4,6,12'
    >>> get_factors(3)
    '1,3'
    """
    factor_string = '1,'
    for possible_factor in range(2, num//2 + 1):
        if num % possible_factor == 0:
            # possible factor is a factor, add to factor string
            factor_string += str(possible_factor) + ','
    return factor_string + str(num)


def get_range_factors(start_num:int, end_num:int) -> str:
    """
    Get the factors for all the numbers between start_num (inc.) and end_num (exc.)
    !>>> get_range_factors(10, 13)
    '1,2,5,10\n1,11\n1,2,3,4,6,12\n'
    """
    factors_string = ''
    for num in range(start_num, end_num):
        factors_string += get_factors(num) + '\n'
    return factors_string

def get_fibonacci_sequence(max_depth:int) -> list:
    """
    The fibonacci sequnece is a sequence where the next number in the sequence is the sum of the previous two numbers
    >>> get_fibonacci_sequence(0)
    []
    >>> get_fibonacci_sequence(1)
    [0]
    >>> get_fibonacci_sequence(2)
    [0, 1]
    >>> get_fibonacci_sequence(5)
    [0, 1, 1, 2, 3]
    >>> get_fibonacci_sequence(9)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    fibonacci_list = [0, 1]
    fibonacci_string = ''
    # create sequence as a list
    for depth in range(max_depth):
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)
    return fibonacci_list[:max_depth]

def sum_fibonacci_sequence(max_depth:int) -> int:
    """
    Return the sum of the fibonacci sequence to a given depth:
    The fibonacci sequnece is a sequence where the next number in the sequence is the sum of the previous two numbers
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(2)
    1
    >>> sum_fibonacci_sequence(5)
    7
    >>> sum_fibonacci_sequence(9)
    54
    """
    sequence = get_fibonacci_sequence(max_depth)
    sum = 0
    for num in sequence:
        sum += num
    return sum

# PART 2

def print_tail(width:int) -> str:
    """
    Precondition: width > 0
    Prints the tail of a rocket with a given width
    """
    print("//   " + ("/\   " * width) + r"\\")


def print_bottom_string(width:int) -> None:
    """
    In between rocket segments there will be a bottom sting to denote this, this function will print it
    as a helper function
    >>> print_bottom_string(10)
    +=*=*=*=*+
    """
    pattern_count = (width - 2) // 2
    print('+' + ('=*' * pattern_count) + '+')


INNER_DIAMOND_PATTERN_TOP = r"\/"
def print_top_booster(width:int) -> None:
    rows = width + 1
    for row in range(rows):
        dots = '.' * (width - row)
        print(f"|{dots}/{INNER_DIAMOND_PATTERN_TOP * row}\\{dots * 2}/{INNER_DIAMOND_PATTERN_TOP * row}\\{dots}|")

