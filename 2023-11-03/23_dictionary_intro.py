import doctest

EMAIL_DATA = 'emailInfo.csv'
HAPPY_FILE = 'happy.txt'
SMALL_FILE = 'small.txt'
VOTES_FILE = 'votes.txt'
EMPTY_FILE = 'empty.txt'

'''
Q1. Design a function that will take a filename of a file with rows of
names and email addresses separated by commas and creates and
returns a dictionary of email contacts.

What will happen if the given file has 2 lines with the same name
but different email addresses?
'''

def parse_email_file(filename:str) -> dict[str:str]:
    """
    takes a file containing names and their assosiated email and will return a
    dictionary with their name as the key and their email as the value
    >>> parse_email_file(EMAIL_DATA)
    {'abc': 'abc@foo.ca', 'cde': 'cde@foo.ca', 'fgh': 'fgh@foo.ca', \
'ijk': 'ijk@foo.ca'}
    """
    information:dict[str:str] = {}
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            name, email = line.split(',')
            information[name] = email
    return information


''' Q2. Design a function that takes a filename of a file with rows of votes
containing a voter id followed by vote (yes, no or abstain) and returns
a dictionary containing the counts of votes for yes, no, abstain.
'''

def parse_votes(filename:str) -> dict[str: int]:
    """
    takes a filename of a file which contains rows of voter ids and their vote
    and returns a dictionary with the counts of each vote
    >>> parse_votes(VOTES_FILE)
    {'yes': 4, 'no': 2, 'abstain': 0}
    >>> parse_votes(EMPTY_FILE)
    {'yes': 0, 'no': 0, 'abstain': 0}
    """
    votes = {'yes': 0, 'no': 0, 'abstain': 0}
    has_voted = []
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            voter_id, vote = line.split()
            if voter_id not in has_voted: votes[vote] += 1
            has_voted.append(voter_id)
    return votes


'''
Q3. Design a function that takes a text file and creates and returns a
dictionary of all the words in the file (no duplicates) followed by
the number of times that word occured.
'''

def file_word_count(filename:str) -> dict[str:int]:
    """
    loops over every word in a file and keeps a count of the number of times
    that word is used, return it in a dictionary witht he word as the key and
    the number of times as the value
    >>> file_word_count(SMALL_FILE)
    {'one': 1, 'two': 3, 'three': 2, 'repeat': 1, 'bye': 1}
    """
    word_dict = {}
    with open(filename) as file_handler:
        for line in file_handler:
            line = line.strip()
            for word in line.split():
                # if word is already in dict add one to it's key
                if word in word_dict.keys():
                    word_dict[word] += 1
                # otherwise, add the key and value to the dictionary
                else:
                    word_dict[word] = 1
    return word_dict


''' Q4. Design a function that takes a dictionary of names:email addresses
and prompts the user to input a name and prints the email address if
found otherwise prints "name not found.  Would you like to add this contact?"
If the user enters yes, proceeds to collect the name and email address
and create a new name:email address entry in the dictionary.
Test this function from the shell.
'''
def access_emails(name_email_dict:dict[str:str]) -> None:
    """
    Takes a dictionary of names:emails and will prompt the user to input a name
    and if there is an email assosiated with that name print out the email.
    If there is no name in the dictionary matching the requested name, propt the
    user to enter and email to be added to the dictionary with the name
    """
    name = input('Please enter a name: ')
    if name in name_email_dict.keys():
        print(name_email_dict[name])
    else:
        email = input(f'Sorry {name}, we cant find your email, please enter: ')
        name_email_dict[name] = email
