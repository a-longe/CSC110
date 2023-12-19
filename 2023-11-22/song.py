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

    def __str__(self) -> str:
        return f"Title: {self.__title}, Artist: {self.__artist}, Length: {self.__length}"
    
    def __repr__(self) -> str:
        return f"Song('{self.__title}', '{self.__artist}', {self.__length})"
    
    def __eq__(self, __value: object) -> bool:
        if self.__title == __value.__title:
            if self.__artist == __value.__artist:
                if self.__length == __value.__length:
                    return True
        return False
    
    def add_time(self, time_to_add:int) -> None:
        self.__length += time_to_add

    def get_title(self) -> None:
        return self.__title
    
    def get_artist(self) -> None:
        return self.__artist
    
    def get_length(self) -> None:
        return self.__length
