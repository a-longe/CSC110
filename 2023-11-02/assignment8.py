import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

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
    month = month_to_num[month]
    day = int(day)
    return (year, month, day)


def read_file(filename: str) -> list[NetflixShow]:
    """ Reads file at filename into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []

    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    """
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    shows = []
    with open(filename, 'r') as file_handler:
        file_handler.readline()
        for line in file_handler:
            data = line.split(',')
            cast = data[INPUT_CAST].split(':')
            if cast[0] == '': cast = []
            directors = data[INPUT_DIRECTORS].split(':')
            if directors[0] == '': directors = []
            show = (data[INPUT_TYPE], data[INPUT_TITLE], directors, cast,\
                    create_date(data[INPUT_DATE]))
            shows.append(show)
    return shows


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
        # years must be equalR
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
                return False


def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    """ Returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []

    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']

    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    """
    oldest_titles = []
    if not show_data:
        oldest_date = show_data[0][DATE]
        oldest_titles = [show_data[0][TITLE]]
    for show in show_data:
        if show[DATE] == oldest_date and show[TITLE] not in oldest_titles:
            oldest_titles.append(show[TITLE])
        elif is_before(show[DATE], oldest_date):
            oldest_titles = [show[TITLE]]
            oldest_date = show[DATE]
    return oldest_titles


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    """ Returns a sorted list of actors that are in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts) # doctest: +NORMALIZE_WHITESPACE
    ['Emma Stone', 'Hugh Bonneville', 'Lily Travers', 'Michael Cera', \
    'Om Puri', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Jonah Hill', 'Om Puri']
    """
    # loop over shows and create a dictionary with all the actors and the number
    # of times they appear in a movie as the values
    actor_appearences = {}
    for show in shows:
        for actor in show[CAST]:
            if actor in actor_appearences.keys():
                actor_appearences[actor] += 1
            else:
                actor_appearences[actor] = 1
            actor_appearences[actor] -= show[CAST].count(actor) - 1 

    most_appearences = []
    num_max_appearences = 0
    for actor in actor_appearences:
        if actor_appearences[actor] > num_max_appearences:
            most_appearences = [actor]
            num_max_appearences = actor_appearences[actor]
        elif actor_appearences[actor] == num_max_appearences:
            most_appearences.append(actor)

    # sort according to ><
    sorted_names = []
    if len(most_appearences) > 0: sorted_names.append(most_appearences[0])
    for actor in most_appearences[1:]:
        is_placed = False
        for index, sorted_name in enumerate(sorted_names):
            if actor < sorted_name:
                sorted_names.insert(index, actor)
                is_placed = True
                break
        if not is_placed: sorted_names.append(actor)
    return sorted_names


def is_term_in_show(show:NetflixShow, search_term:str) -> bool:
    """
    Returns true if the term appears in any part of the NetflixShow data
    >>> movie = ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12))
    >>> is_term_in_show(movie, 'House')
    True
    >>> is_term_in_show(movie, 'houSE')
    True
    >>> is_term_in_show(movie, 'Hayman')
    True
    >>> is_term_in_show(movie, 'HeYMAN')
    False
    >>> is_term_in_show(movie, 'Heyman')
    False
    """
    for element in show:
        if type(element) == list or type(element) == tuple:
            for term in element:
                if search_term.lower() in str(term).lower():
                    return True
        elif search_term.lower() in str(element).lower():
            return True
    return False


def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str],
                                do_return_none_with_no_term=False) -> list[NetflixShow]:
    """ returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    If terms is empty, all elements in show_data will be included in the returned list.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
     ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
      'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
      'Anupam Kher', 'Madhavan'],  \
     (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, []) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
       'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
       'Anupam Kher', 'Madhavan'],  \
      (2018, 8, 2)),\
     ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
      (2017, 12, 12)),\
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]
    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'],
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'],
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
        'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
        'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
       (2017, 12, 12)), \
      ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], \
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12)), \
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]
    """
    shows_with_term = []
    if not do_return_none_with_no_term and terms == []: return show_data
    for show in show_data:
        for term in terms:
            if is_term_in_show(show, term):
                shows_with_term.append(show)
                break
    return shows_with_term


def query(show_data: list[NetflixShow]) -> list[str]:
    """
    Returns a sorted list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> query([])
    []

    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]

    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]

    >>> query([('Movie', 'The Matrix Reloaded',\
  ['Mwayi Nielsen', 'Mayamiko Scriven', 'Wayan Scriven', 'Jing Berardi'], [],\
  (2007, 6, 16)),\
 ('Movie', 'Avatar', ['Chidiebere Martinek', 'Wayan Gereben', 'Kanta Nielsen'],\
  [], (2016, 4, 26)),\
 ('Movie', 'Game of Thrones',\
  ['Chidiebere Kennedy', 'Jose Kennedy', 'Jing Bryan', 'Xia Bryan'], [],\
  (2000, 3, 23)),\
 ('Movie', 'The Witcher',\
  ['Neo Koenig', 'Charis Berardi', 'Kanta Scriven', 'Jianping Garfield',\
   'Nur MacAoidh', 'Mayamiko Scriven', 'Wayan Scriven'],\
  [], (2000, 2, 24)),\
 ('TV Show', 'The Mandalorian',\
  ['Uchenna Nielsen', 'Neo Lee', 'Dada Smith', 'Michele Gereben',\
   'Mayamiko Kennedy', 'Wambli Nielsen', 'Mwayi Lee'],\
  [], (2001, 10, 21)),\
 ('Movie', 'Breaking Bad', ['Connie Lee', 'Michele Kennedy', 'Dada Garfield'],\
  [], (2016, 2, 7)),\
 ('Movie', 'Fight Club',\
  ['Bob MacAoidh', 'Kanta MacAoidh', 'Dada Gereben', 'Wayan Smith'], [],\
  (2018, 2, 26)),\
 ('Movie', 'Titanic',\
  ['Jose Stroman', 'Nur Alserda', 'Jie Martinek', 'Wambli Bryan',\
   'Mayamiko Smith', 'Dada Garfield', 'Jie Alserda', 'Kanta Alserda'],\
  [], (2018, 6, 3)),\
 ('Movie', 'Harry Potter and the Chamber of Secrets',\
  ['Chidiebere Berardi', 'Chidiebere Scriven'], [], (2011, 5, 14)),\
 ('TV Show', 'Jurassic Park',\
  ['Dada Lee', 'Charis Gereben', 'Nur Berardi', 'Uchenna Martinek',\
   'Wayan MacAoidh', 'Jose Kennedy', 'Mayamiko Scriven', 'Mwayi Smith'],\
  [], (2012, 2, 14)),\
 ('TV Show', 'Guardians of the Galaxy', ['Charis Gereben', 'Mayamiko Lee'], [],\
  (2022, 10, 16)),\
 ('TV Show', 'The Crown',\
  ['Xia Berardi', 'Wambli Budai', 'Michele Lee', 'Mayamiko MacAoidh',\
   'Bob Gereben', 'Charis Smith', 'Neo Martinek', 'Jianping Blum'],\
  [], (2018, 9, 21))])
    []
    """
    # get most popular actors
    popular_actors = get_actors_in_most_shows(show_data)
    
    # get movies with these actors
    shows_with_popular_actors = get_shows_with_search_terms(show_data, popular_actors, do_return_none_with_no_term=True)
    
    unsorted_titles = []
    for show in shows_with_popular_actors:
        unsorted_titles.append(show[TITLE])
    
    # sort
    sorted_titles = []
    try: sorted_titles.append(unsorted_titles[0])
    except IndexError: return []
    for show_title in unsorted_titles[1:]:
        has_inserted = False
        for index, sorted_title in enumerate(sorted_titles):
            if show_title < sorted_title:
                sorted_titles.insert(index, show_title)
                has_inserted = True
                break
        if not has_inserted: sorted_titles.append(show_title)

    return sorted_titles
