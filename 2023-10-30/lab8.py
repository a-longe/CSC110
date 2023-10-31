import doctest

DATA_FILE_PATH = "lab8-name-age.txt"
CSV_FILE_PATH = "output.csv"

Person = tuple[str, float]
NAME = 0
AGE = 1

def file_to_person_list(file_name:str) -> list[Person]:
    """
    takes a file of file with peoples information
    with each person being seperated onto seperate lines
    with their name and age being seperated by spaces
    >>> file_to_person_list(DATA_FILE_PATH)
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
    """
    people = []
    with open(file_name, 'r') as file_handler:
        for person in file_handler:
            name, age = person.rstrip('\n').split(' ')
            people.append((name, int(age)))
    return people


def get_average_age(people:list[Person]) -> int:
    """
    Precondition: len(people) > 0
    Takes a list of Persons and calculates the average age and returns it
    as a whole number rounded down
    >>> get_average_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)])
    31
    """
    sum = 0
    for person in people:
        sum += person[AGE]
    return sum // len(people)


def get_above_age(people:list[Person], threshold_age:int) -> list[Person]:
    """
    Returns a list based on the given list but only containing the people who's
    age is ABOVE the threshold age
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 21)
    [('Tian', 27), ('Jose', 53), ('Rajan', 65)]
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 100)
    []
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 4)
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
    """
    old_people = []
    for person in people:
        if person[AGE] > threshold_age:
            old_people.append(person)
    return old_people


def to_file(people:list[Person], file_name:str) -> None:
    """
    Takes a list of people and a file name and writes to that file as a .cvs
    with each line being a person and the name and age being separated by a 
    comma
    """
    # create a new list with strings and commas seperating the age and name
    lines_to_write = []
    for person in people:
        line = f"{person[NAME]},{person[AGE]}\n"
        lines_to_write.append(line) 

    with open(file_name, 'w') as file_handler:
        file_handler.writelines(lines_to_write)


def write_names_above_avg_age(input_file_name:str, output_file_name:str
                              ) -> None:
    """
    Takes a input and an output file name and will find the average and in the
    input file and will only write the people who are above the average age
    """
    input_people = file_to_person_list(input_file_name)
    # check to make sure the file had any people in it
    if len(input_people) == 0: return None
    avg_age = get_average_age(input_people)
    input_people_above_avg = get_above_age(input_people, avg_age)
    to_file(input_people_above_avg, output_file_name)
    
