import doctest

# we designed this function in a past lecture:


def get_num(min_val:int, prompt:str) -> int:
    """
    Takes a minimum value and a prompt and continuously askes the user
    for a inpit that is a valid integer and is greater than or equal to that
    given minimum
    """
    age = input(prompt)
    while not (age.isdigit() and int(age) >= min_val):
        age = input(prompt)
    return int(age)


'''
Q1. Design a function called print_list that takes a list of numbers and
prints all the numbers in the list separated by a comma and space and
enclosed in square brackets.

Use a loop to do this, don't just use print(list_of_numbers)
'''

def print_list(list_of_numbers:list) -> None:
    """
    Prints a list by iterating through a list and printing each element followed
    by a comma, all wrapped in square brackets
    >>> print_list([1,2,3])
    [1,2,3]
    >>> print_list([1])
    [1]
    >>> print_list([])
    """
    for index, num in enumerate(list_of_numbers):
        is_last_num = index == len(list_of_numbers) - 1
        if index == 0:
            print(f'[', end="")
        if is_last_num:
            print(num, end=']\n')
        else:
            print(num, end=',')


'''
Q2. Design a function that will repeatedly prompt the user to enter
positive whole numbers and 0 to stop.
The function should create and return a list that holds all of the positive
integers entered by the user.
The function should ignore invalid input (ie. floats, words, negative values)
'''

def get_list_nums() -> list[int]:
    numbers = []
    num = get_num(0, "Please enter a positive whole number: ")
    while num != 0:
        numbers.append(num)
        num = get_num(0, "Please enter a positive whole number: ")
    return numbers


'''
Q3. Design a function that takes a list of numbers and returns the sum
of the numbers in the list.
Do not use the builtin sum function.
'''

def get_sum_nums() -> int:
    numbers = get_list_nums()
    sum = 0
    for num in numbers:
        sum += num
    return sum

'''
Q4. Design a function that takes a list of integers and returns a new list
with the numbers from the given list with all odd numbers removed.

Example: if called as: keep_even([3, 61, 4, 3, 2, 5])
it should return the list [4, 2]
'''

def remove_odd_nums(list_of_numbers:list[int]) -> list:
    is_even = lambda num : num % 2 == 0
    return list(filter(is_even, list_of_numbers))


'''
Q5. Design a function that takes a list of integers and
an additional integer value.
The function should return the index of the first occurrence of
the additional integer within the list.
If the value is not found in the list, the function should
return -1.
Do not use the builtin list index function
'''

def find(list_of_numbers:list, target:int) -> int:
    for index, num in enumerate(list_of_numbers):
        if num == target:
            return index
    return -1
