import doctest
from song import Song


def starting_function() -> None:

    print('starting_function executing...')
    my_song = Song('Lost', 'Frank Ocean', 145)

    '''Q1. What will output if I uncomment/run the following?
    '''
    # print(my_song.__title)
    # can't access atributes of a class that start with __* outside of a class

    '''Q2. What will output if I uncomment/run the following?
    '''
    my_song.__title = 'Hello'
    print('my_song.__title: ', my_song.__title)
    #^ does not access .__title, it creates a new var
    print('my_song.get_title()', my_song.get_title())

    '''Q3. If I comment out the implementation of __str__ in the Song class,
    how will the output of the following line change?
    '''
    print(my_song)

    '''Q4. If I comment out the __str__, __repr__ and __eq__ methods
    in the Song class, how will the output of the following lines change?
    Think first about what the output will be before you comment out the methods.
    '''
    # song_adele = Song('Hello', 'Adele', 244)
    # song_extra = song_adele
    # song_adele_long = Song('Hello', 'Adele', 421)
    # song_lionel = Song('Hello', 'Lionel Richie', 206)

    # print('song_adele', song_adele)
    # print('song_extra', song_extra)
    # print('song_adele_long', song_adele_long)
    # print('song_lionel', song_lionel)

    # print(song_adele == song_adele)
    # print(song_extra == song_adele)
    # print(song_adele == song_adele_long)
    # print(song_lionel == song_adele)

    
    ''' Q5. How will the output of the four print statements above change
    if we uncomment the __eq__ method in the Song class?
    '''

    ''' Q6. Implement a new instance method in your Song class.
    This method should be called is_written_by and takes as an argument
    an artist name and determines whether the Song's artist is the given artist.
    '''


'''
Q7. Design a function that takes list of Songs and an artist name.
The function should return a list of Songs that are written by the given artist.
'''


def get_songs_by(lo_songs:list[Song], artist:str) -> list[Song]:
    """
    takes a list of songs and will filter the list of songs given by if the 
    given artist is in the song
    >>> get_songs_by([Song('Hello', 'Adele', 244), Song('Hello', 'Adele', 421), Song('Hello', 'Lionel Richie', 206)], 'Adele')
    [Song('Hello', 'Adele', 244), Song('Hello', 'Adele', 421)]
    """
    is_written_by = lambda song : song.get_artist().title() == artist.title()
    return list(filter(is_written_by, lo_songs))

'''
Q8. Design a function that takes a list of Songs and returns the longest Song.
If there are multiple Songs with the longest length, return the first one.
Your function can assume there is at least one Song in the list.
'''

def get_longest_song(lo_songs:list[Song]) -> Song:
    """
    takes a list of songs and will return the longest song, if there are
    two with the same, longest length, return the first
    >>> get_longest_song([Song('Hello', 'Adele', 244), Song('Hello', 'Adele', 421), Song('Hello', 'Lionel Richie', 206)])
    Song('Hello', 'Adele', 421)
    """
    longest = lo_songs[0]
    for song in lo_songs:
        if song.get_length() > longest.get_length():
            longest = song
    return longest
    

'''
Q9. Design a function that takes a list of Songs and a list of all
the longest Songs (there may be more than one).
Your function CANNOT assume there is at least one Song in the list.
Think of how to use the previous function as a helper!
'''

def get_all_longest(lo_songs:list[Song]):
    '''
    >>> get_all_longest([Song('Hello', 'Adele', 244), Song('Hello', 'Adele', 421), Song('Hello', 'Lionel Richie', 421)])
    [Song('Hello', 'Adele', 421), Song('Hello', 'Lionel Richie', 421)]
    '''
    if len(lo_songs) > 0: 
        longest_songs = [lo_songs[0]]
        longest = longest_songs[0].get_length()
    else: longest_songs = []
    for song in lo_songs[1:]:
        if song.get_length() > longest:
            longest_songs = [song]
            longest = song.get_length()
        elif song.get_length() == longest:
            longest_songs.append(song)
    return longest_songs



if __name__ == '__main__':
    #  the code in here will run if you run this program directly
    #  the code in here will NOT run if someone imports this module
    starting_function()
