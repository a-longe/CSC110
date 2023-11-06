HAPPY_PATH = 'happy.txt'
NOT_HAPPY_PATH = 'not_happy.txt'

''' Q1. Write code to do the following:
A- open the file happy.txt for reading
B- read and print the whole file using the read function
C- update the code to read and print just the first line of the file
D- add a while loop to read and print every line single spaced
E- update the code to print every word on its own line single spaced
F- write the code to print every word on its own line single spaced using a for loop
G- update F so that the first line of the file is skipped
'''


def q1():
    with open(HAPPY_PATH, 'r') as file_handler:
        file_handler.readline() # read line one so that the next line skips it and it does not print
        for line in file_handler: # python see file_handler as a itterable of all the lines of the file
            words = line.split()
            for word in words:
                print(word)



''' Q2. Write code to do the following:
- open the file happy.txt for appending
- add the words: 'authored by Pharell Williams' to the end of the file on its own line
'''


def q2():
    print('Q2:')

    with open(HAPPY_PATH, 'a') as file_handler:
        file_handler.write('\nauthored by Pharell Williams')

    with open(HAPPY_PATH, 'r') as f:
        print(f.read())



''' Q3. Write code to do the following:
- open the file not_happy.txt for writing
- add the words: 'You should be happier' to this file
Before you run this code, look at the contents of not_happy.txt
- close the file, run the program and then reopen the file
'''


def q3():
    print('Q3:')
    # read the lines
    # add 'You should be happier'
    # reread the lines

    with open(NOT_HAPPY_PATH, 'r') as file_handler:
        print(file_handler.read())

    with open(NOT_HAPPY_PATH, 'a') as file_handler:
        file_handler.write('\nYou should be happier')

    with open(NOT_HAPPY_PATH, 'r') as file_handler:
        print(file_handler.read())
