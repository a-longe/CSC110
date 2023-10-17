import doctest

'''
Q1. Complete the function below according to the documentation.
This function is tested using doctest but differently than
we have done in the past - why?
'''


def minus_val(lo_nums: list[int], val: int) -> None:
    """ subtract val from every element in lo_nums.
    if the result of the subtraction is <0, replace element with 0
    >>> lst = []
    >>> minus_val(lst, 2)
    >>> lst
    []

    >>> lst = [3,4,5]
    >>> minus_val(lst, 4)
    >>> lst
    [0, 0, 1]

    >>> lst = [3,4,-5]
    >>> minus_val(lst, -6)
    >>> lst
    [9, 10, 1]
    """
    # WE are declaring the list seperatly from the function call and changing the]
    # list give, not returning a new function
    for index, num in enumerate(lo_nums):
        new_val = num - val
        if new_val < 0: new_val = 0
        lo_nums[index] = new_val

'''
Q2. uncomment and complete the following is_decreasing function
according to the documentation given
'''
def is_decreasing(lo_nums: list[int]) -> bool:
    """ determines whether the numbers in lo_nums are strictly decreasing by 1
    returns True if they are, False otherwise
    >>> is_decreasing([])
    True
    >>> is_decreasing([5,4,3,2])
    True
    >>> is_decreasing([5,4,3,0])
    False
    >>> is_decreasing([5,6,3,2])
    False
    >>> is_decreasing([5,6,7,8])
    False
    """
    for index in range(len(lo_nums) - 1):
        if lo_nums[index] != lo_nums[index + 1] + 1:
            return False
        
    return True




'''
Q3. Design a function that will take a list of integers and
determines whether the numbers in the list are all negative.
'''
def are_neg(nums:list[float]) -> bool:
    """
    Determines of a list numbers are all negative

    >>> are_neg([1,2,3])
    False
    >>> are_neg([-1,-2, 0])
    False
    >>> are_neg([-3, -6, -1])
    True
    """
    for num in nums:
        if num >= 0:
            return False
    return True

'''
Q4. Design a function that will take a list of integers and
determines whether the list contains a negative number.
'''


'''
Q5. Design a function that will take a list of integers and returns the
smallest number in the list. Your function should assume the list is not empty.
'''


'''
Q6. Design a function that takes a list of integers and
the function doubles every odd value in the given list.
'''
