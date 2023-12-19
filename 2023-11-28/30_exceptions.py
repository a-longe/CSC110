def start_function():
    print('start_function')
    #  Q0. What is the output of the following code:
    print('Q0:')
    print('main before bar(4)')
    bar(4)
    print('main after bar(4)')
    """
    Q0:
    main before bar(4)
    a
    b
    main after bar(4)
    """

    #  Q1. What is the output of the following code:
    # print('Q1:')
    # print('main before bar(abc)')
    # bar('abc')
    # print('main after bar(abc)')
    """
    Q1:
    main before bar('abc')
    a
    ERROR
    """

    #  Q2. What is the output of the following code:
    print('Q2:')
    print('main before foo(4)')
    foo(4)
    print('main after foo(4)')
    """
    Q2:
    main before foo(4)
    a
    b
    c
    e
    main after foo(4)
    """

    #  Q3. What is the output of the following code:
    print('Q3:')
    print("main before foo(abc)")
    foo('abc')
    print("main after foo('abc')")
    """
    Q3:
    main before foo('abc')
    a
    b
    d
    e
    main after foo('abc')
    """

    #  Q4. What is the output of the following code:
    print('Q4:')
    print("main before baz('10')")
    baz('10')
    print("main after baz('10')")
    """
    Q4:
    main before baz('10')
    a
    b
    c
    d
    e
    g
    main after baz('10')
    """

    #  Q5. What is the output of the following code:
    # print('Q5:')
    # print("main before baz('abc')")
    # baz('abc')
    # print("main after baz('abc')")
    """
    Q5:
    main before baz('abc')
    a
    b
    ERROR
    """


    #  Q6. What is the output of the following code:
    # print('Q6:')
    # print("main before baz('-1')")
    # baz('-1')
    # print("main after baz('-1')")
    """
    Q6:
    main before baz('-1')
    a
    b
    c
    d
    ERROR
    """

    #  Q7. update get_number to use exception handling to deal with invalid input
    print('Q7:')
    result = get_number()
    print(result)
    """
    Q7:
    <INPUT: int>
    """


    #  Q8. Update read_file to use exception handling to prevent the program from crashing
    print('Q8:')
    read_file('happy.txt')
    read_file('notthere.txt')


# documentation omitted intentionally in the following functions
def bar(arg):
    print('a')
    arg += 1
    print('b')


def foo(arg):
    print('a')
    try:
        print('b')
        arg += 1
        print('c')
    except TypeError:
        print('d')

    print('e')


def baz(arg):
    print('a')
    try:
        print('b')
        arg = int(arg)
        print('c')
        arg += 1
        print('d')
        x = 100 / arg
        print('e')
    except TypeError:
        print('f')
    print('g')


def get_number() -> int:
    """ returns a integer entered by the user if valid,
    Precondition: user must enter a valid integer
    """
    n = ''
    while type(n) != int:
        try:
            s_input = input('Enter an integer: ')
            n = int(s_input)
        except ValueError:
            print('Invalid Input: Must be an integer')
    return n


def read_file(filename: str) -> None:
    """ opens filename, reads it into a single string and prints it
    Precondition: filename must exist
    """
    try:
        with open(filename, 'r') as file_handler:
            print(file_handler.read())
    except FileNotFoundError:
        print('File Not Found')


if __name__ == '__main__':
    #  the code in here will run if you run this program directly
    #  the code in here will NOT run if someone imports this module
    print('running directly')
    start_function()
