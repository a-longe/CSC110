import doctest

def get_powers(nums:list[int], power) -> list:
    """
    Takes a list and a given power and returns a new list with all
    the elements in the list raised to the given power
    >>> get_powers([1,2,3], 3)
    [1, 8, 27]
    >>> get_powers([1,2,3], 4)
    [1, 16, 81]
    >>> get_powers([1,2,3], 2)
    [1, 4, 9]
    >>> get_powers([1,2,3], 1)
    [1, 2, 3]
    """
    new_nums:list = []
    for num in nums:
        new_nums.append(num ** power)
    return new_nums


def concatenate(strings:list[str]) -> str:
    """
    Takes a list of strings and returns a string with all the elements
    in a single string separated by spaces
    >>> concatenate(['ab', 'cd', 'e'])
    'ab cd e'
    >>> concatenate(['ab', 'cd', '', 'xyz'])
    'ab cd  xyz'
    >>> concatenate(['this', 'is', 'a', 'test'])
    'this is a test'
    """
    string = ''
    for index, element in enumerate(strings):
        string += element
        if index != len(strings) - 1: string += ' '
    return string


def is_multiple(smaller_num:int, larger_num:int) -> bool:
    """
    Tests if one number is a multiple of another number
    is larger num a multiple of smaller num
    >>> is_multiple(2, 4)
    True
    >>> is_multiple(3, 12)
    True
    >>> is_multiple(3, 4)
    False
    >>> is_multiple(0, 4)
    False
    >>> is_multiple(4, 0)
    True
    >>> is_multiple(0, 0)
    True
    """
    if larger_num == 0:
        return True
    elif smaller_num == 0:
        return False
    return larger_num % smaller_num == 0


def contains_multiple(nums:list[int], multiple:int) -> bool:
    """
    Takes a list of numbers and an aditional number, if there is
    a multiple of the aditional number inside the list, return True
    otherwise return False
    >>> contains_multiple([1,2,3,4,5,6,7,8], 8)
    True
    >>> contains_multiple([1,2,3,4,5,6,7,8], 9)
    False
    >>> contains_multiple([1,2,3,4,5,6,7,8], 3)
    True
    >>> contains_multiple([32, 37, 21, 8, 19, 14, 7, 0, 22, 3, 13, 25, 38, 9, 5], 0)
    True
    >>> contains_multiple([35, 21, 25, 22, 0, 12, 14, 16, 4], 36)
    True
    >>> contains_multiple([36, 35, 14, 30, 9, 8, 7, 31, 16, 32, 33, 28, 27, 15, 5], 0)
    False
    """
    for num in nums:
        if is_multiple(multiple, num): return True
    return False


def get_long_enough(strings:list[str], threshold:int) -> list[str]:
    """
    Returns all the strings that in the list that have a length
    equal to or greater than the threshold
    >>> get_long_enough(['a', 'ab', 'abc', 'abcd', 'abcde'], 1)
    ['a', 'ab', 'abc', 'abcd', 'abcde']
    >>> get_long_enough(['a', 'ab', 'abc', 'abcd', 'abcde'], 2)
    ['ab', 'abc', 'abcd', 'abcde']
    >>> get_long_enough(['a', 'ab', 'abc', 'abcd', 'abcde'], 3)
    ['abc', 'abcd', 'abcde']
    >>> get_long_enough(['a', 'ab', 'abc', 'abcd', 'abcde'], 4)
    ['abcd', 'abcde']
    """
    new_strings:list[str] = []
    for string in strings:
        if len(string) >= threshold:
            new_strings.append(string)
    return new_strings


def all_multiples(nums:list[int], multiplier:int) -> bool:
    """
    Returns True if all numbers  are multiples of the given integer
    >>> all_multiples([1,2,3,4,5,6,7,8], 8)
    False
    >>> all_multiples([1,2,3,4,5,6,7,8], 9)
    False
    >>> all_multiples([1,2,3,4,5,6,7,8], 3)
    False
    >>> all_multiples([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    True
    >>> all_multiples([6, 10, 18, 2, 5, 16, 14, 19, 11, 9, 8, 13, 17, 7, 4, 15], 20)
    False
    >>> all_multiples([9, 153, 72, 18, 27, 99, 45, 81, 126, 90, 171, 135, 108], 9)
    True
    >>> all_multiples([4, -18, 18, -2, 14, -16, 9, -4, -15, 11, -5, -7, -3, -10, 17, 6, -11, 1], 0)
    False
    """
    for num in nums:
        if not is_multiple(multiplier, num):
            return False
    return True

def getting_shorter(strings:list[str]) -> bool:
    """
    Returns true if the strings in the list are in decending length
    >>> getting_shorter(['tiny', 'same', 'are', 'at'])
    False
    >>> getting_shorter(['biggest', 'bigger', 'ATE', 'at'])
    True
    """
    if len(strings) > 0: max_length:int = len(strings[0]) + 1
    else: return True
    for string in strings:
        str_len = len(string)
        if str_len >= max_length:
            return False
        elif str_len < max_length:
            max_length = str_len
    return True

