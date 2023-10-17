import doctest

'''
Q1.  Complete this function according to the documentation
'''
def find(lon: list[int], n: int) -> int:
    """ returns first index of n in lon, -1 if not found
    >>> find([], 2)
    -1
    >>> find([3, 6, 9, -1], 3)
    0
    >>> find([2, 3, 6, -12, 6], 6)
    2
    >>> find([3, 61, 9, -1], -1)
    3
    >>> find([3, 61, 9, -1], -18)
    -1
    """
    testing_index = 0
    len_lon = len(lon)
    
    # stop when index >= len(lon) or lon[index] == n

    while not (testing_index >= len_lon or lon[testing_index] == n):
        testing_index += 1
    
    if testing_index >= len_lon:
        return -1
    else:
        return testing_index


'''
Q1. Design a function that will take a list of integers and
changes the first element in the given list to its negated value.
ie. if the first value is 8, change it to -8,
if the first value is -2 change it to 2.
'''

def negate_first_item(nums:list[int]) -> list[int]:
    """
    Takes a list and returns a list with the same values except for
    the first item is negated or multiplied by -1
    >>> negate_first_item([-1, 2, 3])
    [1, 2, 3]
    >>> negate_first_item([4,7,-4,1])
    [-4, 7, -4, 1]
    >>> negate_first_item([63, 1, -6])
    [-63, 1, -6]
    """
    nums[0] *= -1 ; return nums

'''
Q2. Design a function that will take a list of integers and
adds one to every element in the given list.
'''

def add_one_to_list(nums:list[int]) -> list[int]:
    """
    Takes a list and returns a list with the same values but add
    oneto each element
    >>> add_one_to_list([63, 1, -6])
    [64, 2, -5]
    >>> add_one_to_list([4, 7, -4, 1])
    [5, 8, -3, 2]
    >>> add_one_to_list([0, 1, 2])
    [1, 2, 3]
    """
    add_one = lambda num : num + 1
    return list(map(add_one, nums))

'''
Q3a. Design a function that will take a list of integers and change
every value in that list to its absolute value
DO not use the built in abs function.

Q3b. Design a second version of this function that does use the built-in abs function
'''

def abs_list(nums:list[int]) -> list[int]:
    """
    Takes a list and returns the list with all the values being
    converted to their absolute value
    >>> abs_list([63, 1, -6])
    [63, 1, 6]
    >>> abs_list([4, 7, -4, 1])
    [4, 7, 4, 1]
    >>> abs_list([0, 1, 2])
    [0, 1, 2]
    """
    my_abs = lambda num : -num if num < 0 else num
    return list(map(my_abs, nums))

'''
Q4. Design a function that takes a list of integers and an
additional integer.  The function should determine whether the
additional number is contained in the list.
Do not use the builtin in operator.
'''

def is_in(nums:list[int], target:int) -> bool:
    """
    Returns a bool repersenting if a number is in a list
    >>> is_in([1,2,3], 0)
    False
    >>> is_in([1,2,3], 1)
    True
    >>> is_in([1,-2,3], 2)
    False
    >>> is_in([1,2,3], 4)
    False
    """
    for num in nums:
        if num == target:
            return True
    return False

'''
Q5. Design a function that takes a list of integers and an additional 
integer as second argument.
The function subtracts the integer from every value in the list.
If the subtraction results in a value below 0,
the element at that position should be set to 0.
'''

def sub_from_list(nums:list[int], sub:int) -> list:
    """
    Subtract sub from each element in the list and cap the 
    min value at 0
    >>> sub_from_list([1,2,3], 2)
    [0, 0, 1]
    >>> sub_from_list([-5, 10, 2], 3)
    [0, 7, 0]
    """
    subtract = lambda num : max((num - sub), 0)
    return list(map(subtract, nums))