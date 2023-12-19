import doctest

class Song:
    """ Song class with title, artist, length in seconds
    """
    def __init__(self, title: str, artist: str, length: int) -> None:
        """ initialize an instance of Song with given title, artist and length
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        """
        self.__title = title
        self.__artist = artist
        self.__length = length
    
    def get_title(self) -> str:
        """ return the title associated with Song self
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        >>> my_song.get_title()
        'Martin & Gina'
        """
        return self.__title

    def get_artist(self) -> str:
        """ return the artist associated with Song self
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        >>> my_song.get_artist()
        'Polo G'
        """
        return self.__artist
    
    def get_length(self) -> int:
        """ return the length associated with Song self
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        >>> my_song.get_length()
        160
        """
        return self.__length
    
    def set_title(self, title: str) -> None:
        """ set the title of Song self to the given title
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        >>> my_song.set_title('Lights')
        """
        self.__title = title
        
    def set_length(self, length: int) -> None:
        """ set the length of Song self to the given length
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        >>> my_song.set_length(200)
        """
        self.__length = length
    
    def __str__(self) -> str:
        """ returns a human readable string with attributes from Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> str(s)
        'Jump by van Halen, 234 seconds long'
        """
        res_string = f'{self.__title} by {self.__artist}, ' \
                     + f'{self.__length} seconds long'
        return res_string
        
        
    def __repr__(self) -> str:
        """ returns a string that matches the creation of that Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> repr(s)
        "Song('Jump', 'van Halen', 234)"
        """
        res_string = f"Song({repr(self.__title)}, {repr(self.__artist)}, " \
                     + f"{repr(self.__length)})"
        return res_string
    
    def __eq__(self, other: 'Song') -> bool:
        """" returns True if same title and artist for self and other,
        False otherwise
        >>> s1 = Song('Jump', 'van Halen', 234)
        >>> s2 = Song('Jump', 'van Halen', 255)
        >>> s3 = Song('Jump', 'Pointer Sisters', 234)
        >>> s1==s1
        True
        >>> s1==s2
        True
        >>> s1==s3
        False
        """
        return (self.__title == other.__title
                and self.__artist == other.__artist)
     
    def add_time(self, additional_time: int) -> None:
        """ adds additional_time in seconds to Song self
        >>> s1 = Song('Jump', 'van Halen', 234)
        >>> s1.add_time(20)
        >>> s1
        Song('Jump', 'van Halen', 254)
        """
        self.__length += additional_time
        
