#!/usr/bin/env python3

from doctest import testmod

def sum_even_values(nums: list[int]) -> int:
    """
    Returns the sum of all even numbers in a list
    >>> sum_even_values([])
    0
    >>> sum_even_values([1,2,3,4,5,6])
    12
    >>> sum_even_values([-1, 5, -6, 3, 7, -2, 10])
    2
    """
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
    return even_sum


def count_above(nums:list[int], threashold:int) -> int:
    """
    Threshold is not inclusive, returns the number of values in a list 
    above the given threshold
    >>> count_above([], 0)
    0
    >>> count_above([1,2,3,4,5], 2)
    3
    >>> count_above([-1, 5, -6, 3, 7, -2, 10], -2)
    5
    """
    count = 0
    for num in nums:
        if num > threashold:
            count += 1
    return count


def add1(nums:list[int]) -> list[int]:
    """
    returns a the list of numbers given with one added to each element
    >>> add1([])
    []
    >>> add1([1, 2, 3, 4, 5, 6])
    [2, 3, 4, 5, 6, 7]
    >>> add1([-1, 5, -6, 3, 7, -2, 10])
    [0, 6, -5, 4, 8, -1, 11]
    """
    new_nums = []
    for num in nums:
        new_nums.append(num + 1)
    return new_nums


def are_all_even(nums:list[int]) -> bool:
    """
    returns true only when all nums in the list are even
    >>> are_all_even([])
    True
    >>> are_all_even([1, 2, 3, 4, 5, 6])
    False
    >>> are_all_even([-1, 5, -6, 3, 7, -2, 10])
    False
    >>> are_all_even([2,4,6,8])
    True
    >>> are_all_even([-4, -6, -18, -8, -42])
    True
    """
    for num in nums:
        if num % 2 != 0:
            return False
    return True