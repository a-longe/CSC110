import doctest

'''
Q1. Design a function that takes a list of tuples and prints
the first element of every tuple.
'''

def print_first(tuples:list[tuple]) -> None:
    """
    Takes a list of tuples and prints out the first element in eeach tuple
    >>> print_first([(0, 1, 2), (), (3,)])
    0
    3
    """
    for tuple in tuples:
        if len(tuple) > 0:
            print(tuple[0])

'''
Q2. Design a function that takes a list of tuples where each tuple contains
the name and age of a person.  The function should print the information on
for each person represented in the list.
'''

# repersents a persons info as (name, age)
# name != empty string, age >= 0
Person = tuple[str, int]
NAME = 0
AGE = 1

def print_info(data:list[Person]) -> None:
    """
    Takes a list of tuples and prints out the information stored in the tuple
    the data should look like this (name:str, age:int)
    >>> print_info([("Alex Longe", 17), ("Jim", 32), ("Bob", 76)])
    Name: Alex Longe Age: 17
    Name: Jim Age: 32
    Name: Bob Age: 76
    """
    for person in data:
        name = person[NAME]
        age = person[AGE]
        print(f"Name: {name} Age: {age}")

'''
Q3. Design a function that takes a list of tuples and an additional tuple as
arguments. Each tuple contains the name and age of a person.
The function should return a list of only those tuples in the list who are
younger than the age of the person represented in the additional argument.
If they are the same age, tie should be broken by
lexicographical order of names (Python's string ordering).
'''
def is_older(person1:Person, person2:Person) -> bool:
    """
    >>> is_older(('Celina', 22), ('Adele', 22))
    True
    >>> is_older(("A", 17), ("B", 13))
    True
    >>> is_older(("C", 17), ("A", 18))
    False
    """
    if person1[AGE] > person2[AGE]:
        return True
    elif person1[AGE] == person2[AGE]:
        if person1[NAME] > person2[NAME]:
            return True
    return False


def print_younger(people:list[Person], threashold_person:Person) -> list[Person]:
    """
    print only the data of people younger than the given person
    >>> print_younger([('Alex Longe', 17), ('Jim', 32), ('Bob', 76)], ('Jill', 31))
    [('Alex Longe', 17)]
    >>> print_younger([('Alex Longe', 17), ('Jim', 32), ('Bob', 76)], ('Jared', 99))
    [('Alex Longe', 17), ('Jim', 32), ('Bob', 76)]
    >>> print_younger([('Alex Longe', 17), ('Jim', 32), ('Bob', 76)], ('Baby', 1))
    []
    >>> print_younger([('Alex Longe', 17), ('Celina', 22), ('Jim', 32), ('Bob', 76)], ('Adele', 22))
    [('Alex Longe', 17)]
    """
    # get max age
    max_age = threashold_person[AGE]
    youger_people = []
    for person in enumerate(people):
        if is_older(threashold_person, person):
            youger_people.append(person)
    return youger_people

'''
Q4. Design a function that takes a list of person tuples in increasing age
order (if age is equal, by name lexicographically)
and an addtional argument that is also a person tuple.
The function should create and return a new list with all the persons in the
orginal list + the additional argument.
The new list should be increasing age order too.
If there are 2 people of the same age, order by name lexicographically.
'''

def add_person(ordered_people:list[Person], person_to_add:Person) -> list[Person]:
    """
    loops through the list of sorted people until the new peron is in the right index
    then appends them
    >>> add_person([('Alex Longe', 17), ('Jim', 32), ('Bob', 76)], ('Jill', 31))
    [('Alex Longe', 17), ('Jill', 31), ('Jim', 32), ('Bob', 76)]]
    >>> add_person([('Alex Longe', 17), ('Celina', 22), ('Jim', 32), ('Bob', 76)], ('Adele', 22))
    [('Alex Longe', 17), ('Adele', 22), ('Celina', 22), ('Jim', 32), ('Bob', 76)]
    """
    new_ordered_people:list[Person] = []
    for index, person in enumerate(ordered_people):
        if is_older(person, person_to_add):
            new_ordered_people.append(person_to_add)
            new_ordered_people.append(ordered_people[index:])
            break
        new_ordered_people.append(person)
    return new_ordered_people