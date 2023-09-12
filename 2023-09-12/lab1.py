""" Alex Longe - LAB 1 """

def print_my_info():
    """
    Take your name, favorite number and age and print out some info with that
    >>> print_my_info("Alex", 17, 17)
    ==> My name is Alex
        My favourite number is 17
        I am 17 years old
        Here is some math: 17/17 is 1
    """
    name = "Alex"
    fav_num = 14
    age = 17
    result = fav_num/age
    print(f"My name is {name}")
    print(f"My favourite number is {fav_num}")
    print(f"I am {age} years old")
    print(f"Here is some math: {fav_num}/{age} is {result}")

def print_sum():
    num1 = 23.2
    num2 = 82.4
    print(num1 + num2)