import doctest
from song import Song

def starting_function() -> None:

    print('starting_function executing...')

    # Q0. create a Song class in a separate song.py file

    # Q1. create a Song object with your choice of data in this file
    my_song1 = Song('Hipster Girls', 'Lil B', 156)

    # Q2. print out the title of your song object using the . operator
    print(my_song1.title)

    # Q3. update the length of your song and then print it out using the . operator
    my_song1.sec_len = 232
    print(my_song1.sec_len)

    # Q4. create a second Song object with your choice of data in this file and print the title
    my_song2 = Song('Crazy Train', 'Ozzie Ozborne', 257)
    print(my_song2.title)

    ''' Q5.

    A. create a new variable and set it equal to the first song you created.
    Print the title and artist of the song using the new variable name name.
    Print the title and artist of the song using the previous variable name.
    What do you notice?

    '''
    copy_song = my_song1
    print('\nset copy song to my song 1')
    print('Copy:', copy_song.title, copy_song.artist)
    print('Original1:', my_song1.title, my_song1.artist)
    print('Original2:', my_song2.title, my_song2.artist)
    '''
    They have the same values


    B. Change the title of the song to 'NEW TITLE' using the new variable name.
    Print the title and artist of the song using the new variable name.
    Print the title and artist of the song using the original variable name.
    What do you notice?

    '''
    copy_song.title = 'NEW TITLE'
    print('\nchanged copy song to NEW_TITLE')
    print('Copy:', copy_song.title, copy_song.artist)
    print('Original1:', my_song1.title, my_song1.artist)
    print('Original2:', my_song2.title, my_song2.artist)
    '''
    The name of the first variable changesd as well...i hate python...

    C. Change the title of the song to 'ANOTHER TITLE' using the original variable name.
    Print the title and artist of the song using the new variable name.
    Print the title and artist of the song using the original variable name.
    What do you notice?

    '''
    my_song1.title = 'ANOTHER TITLE'
    print('\nchanged original variable title to ANOTHER TITLE')
    print('Copy:', copy_song.title, copy_song.artist)
    print('Original1:', my_song1.title, my_song1.artist)
    print('Original2:', my_song2.title, my_song2.artist)
    '''


    D. Set your new variable equal to the second song you created.
    Print the title and artist of the song using the new variable name.
    Print the title and artist of the songs you created using the original variable names.
    What do you notice?

    '''
    copy_song = my_song2
    print('\nset copy song to my song 2')
    print('Copy:', copy_song.title, copy_song.artist)
    print('Original1:', my_song1.title, my_song1.artist)
    print('Original2:', my_song2.title, my_song2.artist)
    '''


    E. Change the title of the song to 'LAST TITLE' using the new variable name.
    Print the title and artist of the song using the new variable name.
    Print the title and artist of the songs you created using the original variable names.
    What do you notice?
    '''
    copy_song.title = 'LAST TITLE'
    print('\nset copy_songs title to LAST TITLE')
    print('Copy:', copy_song.title, copy_song.artist)
    print('Original1:', my_song1.title, my_song1.artist)
    print('Original2:', my_song2.title, my_song2.artist)


''' Q6. Design a function that takes a list of Song instances (objects)
and returns the total length of all of them
'''


if __name__ == '__main__':
    # the code in here will run if you run this program directly
    # the code in here will NOT run if someone imports this module
    print('__name__ == __main is True')
    starting_function()
