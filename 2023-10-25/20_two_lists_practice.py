import doctest


'''
Q0. Complete the function below from last lecture.
'''

def zip_longer(list1: list[int], list2: list[int], fill_val: int
               ) -> list[tuple[int, int]]:
    """ creates and returns a list of tuples for pairs across list1 and list2,
    fills missing values with fill_val
    >>> zip_longer([], [], 2)
    []
    >>> zip_longer([2, 3, 4], [], 1000)
    [(2, 1000), (3, 1000), (4, 1000)]
    >>> zip_longer([], [5, 6, 7], 1)
    [(1, 5), (1, 6), (1, 7)]
    >>> zip_longer([8, 9, 10], [5, 6, 7], 1)
    [(8, 5), (9, 6), (10, 7)]
    >>> zip_longer([8, 9, 10], [5, 6], 2)
    [(8, 5), (9, 6), (10, 2)]
    >>> zip_longer([8, 9], [5, 6, 7], 2)
    [(8, 5), (9, 6), (2, 7)]
    """
    pairs = []
    
    # find larger list
    if len(list1) >= len(list2):
        list_size = len(list1)
    else:
        list_size = len(list2)

    for index in range(list_size):
        element1:int
        element2:int

        try:
            element1 = list1[index]
        except IndexError:
            element1 = fill_val

        try:
            element2 = list2[index]
        except IndexError:
            element2 = fill_val

        pairs.append((element1, element2))
    return pairs

'''
Q1. Design a function that will take two lists of integers
that are in increasing order. The function should
create and return a list of all the values from list1 and list2
in sorted order
ie. if the function is called with [2, 10], [5, 6, 11]
the function should return [2, 5, 6, 10, 11]
'''
VALUE = 0
INDEX= 1
def index_of_smallest(values:list) -> tuple[int]:
    """
    finds the index of the smallest value in the list
    as determined by pythons > < and = opporators
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'A'])
    4
    """
    if len(values) > 0: smallest = (values[0], 0)
    else: return -1
    for index, value in enumerate(values):
        if value < smallest[VALUE]:
            smallest = (value, index)
    return smallest[INDEX]

def merge_ordered_lists(list1:list[int], list2:list[int]) -> list[int]:
    """
    Adds two lists together and keeps the correct ordering
    >>> merge_ordered_lists([2, 10], [5, 6, 11])
    [2, 5, 6, 10, 11]
    """
    result = []
    result_len = len(list1) + len(list2)
    merged_unordered = list1 + list2

    for index in range(result_len):
        smallest_index = index_of_smallest(merged_unordered)
        result.append(merged_unordered[smallest_index])
        merged_unordered.pop(smallest_index)
    return result
    

'''
Q2. Design a function that will sort a given list of integers.
The function should use a selection sort algorithm:
for each position in the given list,
-finds the position of the smallest value between 
the current position and the end of the list
-swaps the values at the current position and
the position of the smallest value
NOTE: this function will mutate the list
TIP: use the functions you wrote in lab as helper functions
'''

def swap(list:list, position1:int, position2:int) -> None:
    """
    Preconditions: position1 and position2 must be valid indecies for the list
    Takes a list and swaps the elements in the two given positions
    >>> x = [1,2,3,4]
    >>> swap(x, 0, 3)
    >>> x
    [4, 2, 3, 1]

    >>> x = [1,2,3]
    >>> swap(x, 0, 1)
    >>> x
    [2, 1, 3]
    """
    value1 = list[position1]
    value2 = list[position2]
    list[position1], list[position2] = value2, value1

def selection_sort(nums:list[int]) -> None:
    """
    Sorts a list based on pythons >< operators
    >>> selection_sort([1, 2, 3, 0])
    [0, 1, 2, 3]
    >>> selection_sort([5, 4, 2, 3, 1])
    [1, 2, 3, 4, 5]
    """
    for index in range(len(nums)):
        smallest_index = index_of_smallest(nums[index:]) + index
        swap(nums, index, smallest_index)
    return nums



'''
Q3. Design a function that takes 2 lists of integers and determines whether the
first list is strictly contained in the second list.
You should not need a nested loop to solve this problem.
For example,
[1, 4, 3] is contained in [1, 1, 4, 3]
[1, 4, 3] is not contained in [1, 1, 4, 4, 3]
'''

def is_list_in_list(nums:list[int], contained_in:list[int]) -> bool:
    """
    Returns if one list of integers is directly contained in the second list
    >>> is_list_in_list([1, 4, 3], [1, 1, 4 ,3])
    True
    >>> is_list_in_list([1, 4, 3], [1, 1, 4, 4, 3])
    False
    """
    # loops over each element in the second list and checks that element and the next elements
    # equal to the length of the first list
    nums_len = len(nums)
    contained_in_len = len(contained_in)
    for index in range(contained_in_len - nums_len + 1):
        list_splice = contained_in[index:index + nums_len]
        if list_splice == nums:
            return True
    return False
