class Song:
    ''' repersents a song with a title, artist and length in sec'''
    def __init__(self, title:str, artist:str, sec_len:int) -> None:
        """
        >>> my_song = Song('Hipster Girls', 'Lil B', 156)
        """
        self.title = title
        self.artist = artist
        self.sec_len = sec_len

    