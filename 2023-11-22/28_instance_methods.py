import doctest
from song import Song


def starting_function() -> None:

    print('starting_function executing...')

    my_song = Song('Lost', 'Frank Ocean', 145)
    print(my_song.get_title())
    print(my_song.get_artist())
    print(my_song.get_length())

    '''Q1. make the attributes in your Song class private.
    Does your code from above still work? If not, fix it.
    '''

    '''Q2. print your Song object '''

    print(my_song)

    '''Q3. in your Song class implement the __str__ method according
    to documenation commented out below. Does your output change?

    def __str__(self) -> str:
        """ returns a human readable string with attributes from Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> str(s)
        'Jump by van Halen, 234 seconds long'
        """
    '''

    '''Q4. create another 2 song objects with your choice of data '''

    my_song2 = Song('Crazy Train', 'Ozzie Ozborne', 210)
    my_song3 = Song("California Dreamin'", 'The Mamas and The Papas', 183)

    '''Q5. create a list of your 3 songs and print the list '''

    lo_songs = [my_song, my_song2, my_song3]
    print(lo_songs)

    '''Q6. in your Song class implement the __repr__ method
    according to documenation commented out below. Does your output change?

    def __repr__(self) -> str:
        """ returns a string that matches the creation of that Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> repr(s)
        "Song('Jump', 'van Halen', 234)"
        """
    '''

    '''Q7. create another song object with the same title and artist
    as one of your other Song objects.
    Compare these two song using the == operator.
    '''

    copy_of_song_2 = Song('Crazy Train', 'Ozzie Ozborne', 210)
    print(copy_of_song_2 == my_song2)

    '''Q8. in your Song class implement the __eq__ method according
    to documenation commented out below. Does your output change?

    def __eq__(self, other: 'Song') -> bool:
        """ returns True if same song, False otherwise
        >>> s1 = Song('Jump', 'van Halen', 234)
        >>> s2 = Song('Jump', 'van Halen', 255)
        >>> s3 = Song('Jump', 'Pointer Sisters', 234)
        >>> s1==s1
        True
        >>> sin1==s2
        True
        >>> s1==s3
        False
        """
    '''

    '''
    Q9. Implement a new instance method in your Song class.
    This method should be called add_time and should take as an argument the
    amount of time to add to the Song.  When the method is complete, it should
    have added the given time to the Song.
    Add some example calls to this method in your main function.

    
    What happens if you call this method on a Song instance
    that you added to your list?
    '''
    print(lo_songs)
    print(lo_songs[1])
    print(lo_songs[1].get_length())
    lo_songs[1].add_time(41)
    print(lo_songs)


if __name__ == '__main__':
    # the code in here will run if you run this program directly
    # the code in here will NOT run if someone imports this module
    starting_function()
