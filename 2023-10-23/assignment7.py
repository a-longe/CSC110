import doctest

Date = tuple[int, int, int]
# year, month, day
YEAR = 0
MONTH = 1
DAY = 2

Show = tuple[str, str, list[str], list[str], Date]
# type of show, title, list of directors, list of actors, date added
TYPE = 0
TITLE = 1
DIRECTORS = 2
ACTORS = 3
DATE = 4

def raise_to_power(to_be_raised:list[int], exponants:list[int]) -> None:
    """
    Takes the first list and raises it to the exponants in the second, 
    if the first list is longer, raise the remaining number to the power
    of one, if the second list is longer, ignore the numbers in it that 
    dont correspond to a number
    >>> x = [1, 2, 3]
    >>> raise_to_power(x, [2,4,0])
    >>> x
    [1, 16, 1]

    >>> x = [1, 2, 3]
    >>> raise_to_power(x, [2, 4])
    >>> x
    [1, 16, 3]

    >>> x = [1,2,3]
    >>> raise_to_power(x, [2, 4, 0, 2])
    >>> x
    [1, 16, 1]
    """
    for index, base in enumerate(to_be_raised):
        # determine exponant
        try:
            exponant = exponants[index]
        except IndexError:
            exponant = 1

        to_be_raised[index] = base ** exponant
        

def month_to_num(month:str) -> int: 
    """
    Takes a month as the first three letters of the month's name
    with the first letter being capitalized
    """
    month_to_num = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    return month_to_num[month]

def create_date(date:str) -> Date:
    """
    takes a input string in the format 'DD-MMM-YY' ex. '25-May-06' for
    May 25th 2006 and it will return a Date type
    >>> create_date('25-May-06')
    (2006, 5, 25)
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    """
    day, month, year = date.split('-')
    year = 2000 + int(year)
    month = month_to_num(month)
    day = int(day)
    return (year, month, day)


def create_show(show_type:str, title:str, director_string:str, actors_string:str, date_string:str) -> Show:
    """
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))

    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))   
    """
    if len(director_string) == 0:
        directors = []
    else: directors = director_string.split(':')
    if len(actors_string) == 0:
        actors = []
    else: actors = actors_string.split(':')
    date_added = create_date(date_string)
    return (show_type, title, directors, actors, date_added)


def get_titles(shows:list[Show]) -> list[str]:
    """
    Takes a list of shows and returns a list of the titles
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    """
    titles = []
    for show in shows:
        titles.append(show[TITLE]) 
    return titles


def is_actor_in_show(show:Show, actor_to_find:str) -> bool:
    """
    Takes a show and an actor and returns a boolean
    based on if the actor is in the show
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    """
    return actor_to_find.title() in show[ACTORS]
    

def is_before(date1:Date, date2:Date) -> bool:
    """
    Returns True if date1 is before date2
    >>> is_before((2021, 5, 2), (2020, 2, 1))
    False
    >>> is_before((2020, 3, 2), (2020, 3, 5))
    True
    """
    if date1[YEAR] < date2[YEAR]:
        return True
    elif date1[YEAR] > date2[YEAR]:
        return False
    else:
        # years must be equal
        if date1[MONTH] < date2[MONTH]:
            return True
        elif date1[MONTH] > date2[MONTH]:
            return False
        else:
            # months must be equal
            if date1[DAY] < date2[DAY]:
                return True
            elif date1[DAY] > date2[DAY]:
                return False
            else:
                # dates are the same
                return True
        


def count_shows_before_date(shows:list[Show], date_threshold:Date) -> int:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]

    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0

    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    """
    count = 0
    for show in shows:
        if is_before(show[DATE], date_threshold):
            count += 1
    return count


def get_shows_with_actor(shows:list[Show], actor_to_find:str) -> list[Show]:
    """
    gets the shows in the given show list with the given actor and returns it 
    as a list

    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    """
    shows_with_actor = []
    for show in shows:
        if actor_to_find.title() in show[ACTORS]:
            shows_with_actor.append(show)
    return shows_with_actor