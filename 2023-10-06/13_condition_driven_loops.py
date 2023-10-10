'''
Q1. Design a function called get_number that asks a
user to enter a whole number int >= 0 returns
the number as an integer.
TIP: remember the int function
'''

def get_number() -> int:
    """
    Ask for a whole number >= 0 and return the given number as a integer
    """
    num:str = input("Enter a whole number >= 0:")
    try:
        return int(num)
    except ValueError:
        return float(num)

'''
Q2. update the get_number so that if the user enters
an invalid int (non-integer or number<0)
it repeatedly prompts the user.
When a valid entry is finally made, the function
returns the number as an integer
TIP: remember the isdigit function
'''

def new_get_number() -> int:
    """
    Continues to ask the user for a whole number until the one given is a
    int and is >= 0
    """
    num = get_number()
    is_float, is_negative = type(num) == float, num < 0
    while is_float or is_negative:
        print("Invalid Number")
        num = get_number()
        is_float, is_negative = type(num) == float, num < 0
    return num


'''
Q3. Design a function that will compute and return the sum of a series
of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''

def get_sum() -> int:
    """
    The user will enter a series of positive whole numbers and the function will
     return the sum of all these numbers
    """
    num = new_get_number()
    sum = num
    while num != 0:
        num = new_get_number()
        sum += num
    return sum

'''
Q4. Design a function that will determine and return the largest of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''

def get_largest() -> int:
    num = new_get_number()
    largest = num
    while num != 0:
        num = new_get_number()
        if num > largest:
            largest = num
    return largest

'''
Q5. Design a function that will calculate and return the average of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
If the first number entered by the user is 0, the message
"Error: no data" is printed and the function returns -1.
'''
def get_average() -> float:
    num = new_get_number()
    sum = num
    count = 1
    while num != 0:
        num = new_get_number()
        sum += num
        count += 1
    return sum / count
