import doctest

def get_biggest(num1:float, num2:float, num3:float) -> float:
    """
    Takes three float values and returns the largest
    >>> get_biggest(1,2,3)
    3
    >>> get_biggest(1,3,2)
    3
    >>> get_biggest(2,1,3)
    3
    >>> get_biggest(2,3,1)
    3
    >>> get_biggest(3,1,2)
    3
    >>> get_biggest(3,2,1)
    3
    >>> get_biggest(0,0,0)
    0
    >>> get_biggest(1,1,1)
    1
    """