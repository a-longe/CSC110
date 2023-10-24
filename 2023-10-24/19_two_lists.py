import doctest


# represent a person's information as (name, age)
# where name!='' and age>=0
Person = tuple[str, int]
NAME = 0
AGE = 1

'''
Here is where we left off last lecture...
I have added documentation and tests.
We will start by completing the insert function.
'''


def print_people(lo_people: list[Person]) -> None:
    """ prints information for each Person in lo_people
    >>> print_people([])
    >>> print_people([('Adam', 22), ('Jose', 45), ('Lizzo', 32)])
    Adam: 22
    Jose: 45
    Lizzo: 32
    """
    for p in lo_people:
        print(p[NAME], ': ', p[AGE], sep='')


def is_before(p1: Person, p2: Person) -> bool:
    """ determines whether p1 is before p2 in age, or if age is equal
    if name of p1 is before name of p2. returns True if it is, False otherwise.
    >>> is_before(('Adam', 30), ('Lizzo', 32))
    True
    >>> is_before(('Zac', 30), ('Lizzo', 32))
    True
    >>> is_before(('Adam', 32), ('Lizzo', 32))
    True
    >>> is_before(('Zac', 32), ('Lizzo', 32))
    False
    >>> is_before(('Betty', 40), ('Lizzo', 32))
    False
    >>> is_before(('Zac', 40), ('Lizzo', 32))
    False
    >>> is_before(('Lizzo', 40), ('Lizzo', 40))
    False
    """
    return p1[AGE] < p2[AGE] or (p1[AGE] == p2[AGE] and p1[NAME] < p2[NAME])


def insert_person(lo_people: list[Person], to_insert: Person) -> list[Person]:
    """ creates and returns a list with to_insert inserted into lo_people 
    in order of increasing age. If ages are equal, order by name alphabetically.
    Precondition: lo_people is in increasing age order, then alphabetical by name
    >>> people = [('Adam', 22), ('Jose', 25), ('Lizzo', 32)]

    >>> insert_person([], ('Tian', 19))
    [('Tian', 19)]

    >>> insert_person(people, ('Jill', 19))
    [('Jill', 19), ('Adam', 22), ('Jose', 25), ('Lizzo', 32)]

    >>> insert_person(people, ('Jill', 25))
    [('Adam', 22), ('Jill', 25), ('Jose', 25), ('Lizzo', 32)]

    >>> insert_person(people, ('Jill', 33))
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]
    """
    new_people = lo_people[:]
    has_inserted = False
    for index, person in enumerate(lo_people):
        if is_before(to_insert, person):
            new_people.insert(index, to_insert)
            has_inserted = True
            break
    if not has_inserted:
        new_people.append(to_insert)
    return new_people
        



'''
Q1. Design a function that takes a list of Person tuples in no order.
The function should create and return a new list in increasing age order.
'''


def sort_people(lo_people: list[Person]) -> list[Person]:
    """ creates a new list with Persons in lo_people in increasing age order,
    and alphabetical by name if ages are equal

    >>> sort_people([])
    []

    >>> sort_people([('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)])
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]

    >>> sort_people([('Adam', 22), ('Jose', 12), ('Lizzo', 32), ('Jill', 32)])
    [('Jose', 12), ('Adam', 22), ('Jill', 32), ('Lizzo', 32)]

    >>> sort_people([('Adam', 22), ('Jose', 18), ('Betty', 18), ('Jill', 12)])
    [('Jill', 12), ('Betty', 18), ('Jose', 18), ('Adam', 22)]
    """
    ordered_people = []
    for person in lo_people:
        ordered_people = insert_person(ordered_people, person)
    return ordered_people
    


'''
Q2. Design a function that takes a list of person tuples in no particular order.
The function should print the information for each person in order increasing age.
'''


def print_sorted_list(lo_people: list[Person]) -> None:
    """ prints lo_people in sorted order of age then by name
    >>> print_sorted_list([])
    >>> print_sorted_list([('Adam', 22), ('Jose', 12), ('Lizzo', 32), ('Jill', 32)])
    Jose: 12
    Adam: 22
    Jill: 32
    Lizzo: 32
    """
    sorted_people = sort_people(lo_people)
    for person in sorted_people:
        print(f"{person[NAME]}: {person[AGE]}")


'''
Q3. Design a function that will take two lists of integers and
creates and returns a list of tuples that are pairs across the lists.
ie. if the lists are [2, 3, 4] and [5, 6, 7]
the function should return [(2, 5), (3, 6), (4, 7)]

The function should assume the lists are the same length
'''

def create_pairs(list1:list[int], list2:list[int]) -> list[tuple[int]]:
    """
    Precondition: len(list1) == len(list2)
    Takes two lists and returns a list of tuples containing pairs of numbers with the same index
    >>> create_pairs([2, 3, 4], [5, 6, 7])
    [(2, 5), (3, 6), (4, 7)]
    >>> create_pairs([],[])
    []
    >>> create_pairs([1,2,3], [1, 4, 9])
    [(1, 1), (2, 4), (3, 9)]
    """
    pairs = []
    for element1, element2 in zip(list1, list2):
        pairs.append((element1, element2))
    return pairs



'''
Q4. Design a function that will take two lists of integers
and an additional integer argument.  The function should
create and return a list of tuples that are pairs across the lists.
If a list is shorter than the other, the tuple gets filled with the
additional argument.
ie. if the function is called with [2, 3, 4], [5, 6] and 1000
the function should return [(2, 5), (3, 6), (4, 1000)]
'''

def better_create_pairs(list1:list[int], list2:list[int], filler:int) -> list[tuple[int]]:
    """
    Takes two lists and returns pairs of integers which share indecies
    if one list is shorter than the other, use the filler argument
    to use as a default value to replace the missing integers
    >>> better_create_pairs([2, 3, 4], [5, 6], 1000)
    [(2, 5), (3, 6), (4, 1000)]
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
            element1 = filler

        try:
            element2 = list2[index]
        except IndexError:
            element2 = filler

        pairs.append((element1, element2))
    return pairs