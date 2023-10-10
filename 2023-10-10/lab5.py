CHILD_MAX_AGE = 17
ADULT_MAX_AGE = 64
MAX_ITTERATIONS = 100

def get_age_catagory(age:int) -> str:
    age_catagory = ""
    if age <= CHILD_MAX_AGE:
        # is child
        age_catagory = "child"
    elif age <= ADULT_MAX_AGE:
        # is adult
        age_catagory = "adult"
    else:
        # is senior
        age_catagory = "senior"
    return age_catagory

def print_name_age_v1() -> None:
    """
    Asks for your age and name, assumes you are nice and have given a valid age
    or will throw an error
    """
    name:str = input("Please enter your name: ")
    age:int = int(input("Please enter a positive whole number as your age: "))
    age_catagory:str = get_age_catagory(age)

    print(f"hello {name} {age_catagory}")


def print_name_age_v2() -> None:
    """
    Asks for your age and name, will handle if given invalid age
    """
    name:str = input("Please enter your name: ")
    age = input("Please enter a positive whole number as your age: ")
    if age.isdigit() and int(age) >= 0:
        age_catagory:str = get_age_catagory(int(age))
        print(f"hello {name} {age_catagory}")
    else:
        print(f"{name} you are lying about your age")


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


def print_name_age_v3() -> None:
    """
    Prompts user for name, then continuously asks user for valid integer
    as age then prints hello, followed by their name and what age catagory
    they fall into
    """
    name:str = input("Please enter your name: ")
    age:int = get_num(0, "Please enter your age: ")
    age_catagory:str = get_age_catagory(age)
    print(f"hello {name} {age_catagory}")
