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

Show = tuple[str, str, str, list[str], list[str], str, 
            Date, str, str, str, list[str], str]
ID = 0
TYPE = 1
TITLE = 2
DIRECTORS = 3
CAST = 4
COUNTRY = 5
DATE_ADDED = 6
YEAR_ADDED = 7
RATING = 8
DURATION = 9
CATAGORIES = 10
DISCRIPTION = 11

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
                return False

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
    year = START_YEAR + int(year)
    month = month_to_num[month]
    day = int(day)
    return (year, month, day)


def parse_data(filename:str) -> list[Show]: 
    """
    Takes a file of show data and will parse that data into a list, allowing for
    only one read of the file
    >>> parse_data('0lines_data.csv')
    []

    >>> parse_data('11lines_data.csv')
    [('81217749', 'Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], 'India:United States', (2019, 11, 15), '2018', 'TV-PG', '74 min', ['Documentaries', 'International Movies'], 'A trio of filmmakers treks across India to explore the correlation between vanishing rivers and massive energy projects and renewable energy sources.'), ('70303496', 'Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], 'India', (2018, 9, 6), '2014', 'TV-14', '146 min', ['Comedies', 'Dramas', 'International Movies'], 'Aamir Khan teams with director Rajkumar Hirani to play a social crusader in a political satire on the state of corruption in India.'), ('70142798', 'Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], 'Thailand', (2018, 9, 5), '2009', 'TV-MA', '125 min', ['Horror Movies', 'International Movies'], 'From disfiguring punishments to festering souls. Thai horror masters present five supernatural tales of karma in this sequel to the 4bia anthology.'), ('80999063', 'Movie', 'Super Monsters Save Halloween', [''], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '', (2018, 10, 5), '2018', 'TV-Y', '25 min', ['Children & Family Movies'], "The Super Monsters use their powers to get their neighbors in the Halloween spirit:then help a nervous friend see there's nothing to be afraid of."), ('80190843', 'TV Show', 'First and Last', [''], [''], '', (2018, 9, 7), '2018', 'TV-MA', '1 Season', ['Docuseries'], "Take an intimate look at the emotionally charged first and last days of new and soon-to-be released inmates at Georgia's Gwinnett County Jail."), ('80119349', 'Movie', 'Out of Thin Air', ['Dylan Howitt'], [''], '', (2017, 9, 29), '2017', 'TV-14', '85 min', ['Documentaries', 'International Movies'], 'Picking up 40 years after six were convicted for two strange murders in Iceland:this chilling documentary proves confessions can’t always be trusted.'), ('70062814', 'Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], 'Thailand', (2018, 9, 5), '2004', 'TV-MA', '96 min', ['Horror Movies', 'International Movies'], 'After killing a young girl in a hit-and-run accident:a couple is haunted by more than just the memory of their deadly choice.'), ('80182115', 'Movie', 'Long Shot', ['Jacob LaMendola'], [''], 'United States', (2017, 9, 29), '2017', 'TV-14', '40 min', ['Documentaries'], "When Juan Catalan is arrested for a murder he didn't commit:he builds his case for innocence around raw footage from a popular TV show. A documentary."), ('80187722', 'TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], '', (2018, 10, 12), '2018', 'TV-MA', '1 Season', ['Docuseries'], 'Actor and fight enthusiast Frank Grillo travels the world:immersing himself in different fight cultures to understand their traditions and motivations.'), ('70213237', 'TV Show', "Monty Python's Almost the Truth", [''], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], 'United Kingdom', (2018, 10, 2), '2009', 'NR', '1 Season', ['British TV Shows', 'Docuseries'], 'The legacy of comedy group Monty Python:whose irreverent brand of humor has tickled the ribs of millions:is explored in this documentary.'), ('70121522', 'Movie', '3 Idiots', ['Rajkumar Hirani'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], 'India', (2019, 8, 1), '2009', 'PG-13', '164 min', ['Comedies', 'Dramas', 'International Movies'], "While attending one of India's premier colleges:three miserable engineering students and best friends struggle to beat the school's draconian system.")]
    """
    lo_shows = []
    with open(filename, 'r') as file_handler:
        file_handler.readline()
        for line in file_handler:
            line = line.strip()
            data = line.split(',')
            id = data[ID]
            title = data[TITLE]
            show_type = data[TYPE]
            catagories = data[CATAGORIES].split(':')
            directors = data[DIRECTORS].split(':')
            country = data[COUNTRY]
            cast = data[CAST].split(':')
            unique_actors = []
            for actor in cast:
                if not actor in unique_actors:
                    unique_actors.append(actor)
            cast = unique_actors
            date_added = create_date(data[DATE_ADDED])
            release_year = data[YEAR_ADDED]
            rating = data[RATING]
            duration = data[DURATION]
            desciption = data[DISCRIPTION]
            lo_shows.append((id, show_type, title, directors, cast, country, 
                            date_added, release_year, rating, duration,
                            catagories, desciption))
    return lo_shows


def create_id_date(lo_shows:list[Show]) -> dict[str: Date]:
    """
    >>> create_id_date([])
    {}

    # doctest: +NORMALIZE_WHITESPACE
    >>> create_id_date([('81217749', 'Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], 'India:United States', (2019, 11, 15), '2018', 'TV-PG', '74 min', ['Documentaries', 'International Movies'], 'A trio of filmmakers treks across India to explore the correlation between vanishing rivers and massive energy projects and renewable energy sources.'), ('70303496', 'Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], 'India', (2018, 9, 6), '2014', 'TV-14', '146 min', ['Comedies', 'Dramas', 'International Movies'], 'Aamir Khan teams with director Rajkumar Hirani to play a social crusader in a political satire on the state of corruption in India.'), ('70142798', 'Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], 'Thailand', (2018, 9, 5), '2009', 'TV-MA', '125 min', ['Horror Movies', 'International Movies'], 'From disfiguring punishments to festering souls. Thai horror masters present five supernatural tales of karma in this sequel to the 4bia anthology.'), ('80999063', 'Movie', 'Super Monsters Save Halloween', [''], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '', (2018, 10, 5), '2018', 'TV-Y', '25 min', ['Children & Family Movies'], "The Super Monsters use their powers to get their neighbors in the Halloween spirit:then help a nervous friend see there's nothing to be afraid of."), ('80190843', 'TV Show', 'First and Last', [''], [''], '', (2018, 9, 7), '2018', 'TV-MA', '1 Season', ['Docuseries'], "Take an intimate look at the emotionally charged first and last days of new and soon-to-be released inmates at Georgia's Gwinnett County Jail."), ('80119349', 'Movie', 'Out of Thin Air', ['Dylan Howitt'], [''], '', (2017, 9, 29), '2017', 'TV-14', '85 min', ['Documentaries', 'International Movies'], 'Picking up 40 years after six were convicted for two strange murders in Iceland:this chilling documentary proves confessions can’t always be trusted.'), ('70062814', 'Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], 'Thailand', (2018, 9, 5), '2004', 'TV-MA', '96 min', ['Horror Movies', 'International Movies'], 'After killing a young girl in a hit-and-run accident:a couple is haunted by more than just the memory of their deadly choice.'), ('80182115', 'Movie', 'Long Shot', ['Jacob LaMendola'], [''], 'United States', (2017, 9, 29), '2017', 'TV-14', '40 min', ['Documentaries'], "When Juan Catalan is arrested for a murder he didn't commit:he builds his case for innocence around raw footage from a popular TV show. A documentary."), ('80187722', 'TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], '', (2018, 10, 12), '2018', 'TV-MA', '1 Season', ['Docuseries'], 'Actor and fight enthusiast Frank Grillo travels the world:immersing himself in different fight cultures to understand their traditions and motivations.'), ('70213237', 'TV Show', "Monty Python's Almost the Truth", [''], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], 'United Kingdom', (2018, 10, 2), '2009', 'NR', '1 Season', ['British TV Shows', 'Docuseries'], 'The legacy of comedy group Monty Python:whose irreverent brand of humor has tickled the ribs of millions:is explored in this documentary.'), ('70121522', 'Movie', '3 Idiots', ['Rajkumar Hirani'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], 'India', (2019, 8, 1), '2009', 'PG-13', '164 min', ['Comedies', 'Dramas', 'International Movies'], "While attending one of India's premier colleges:three miserable engineering students and best friends struggle to beat the school's draconian system.")])
    {'81217749': (2019, 11, 15), '70303496': (2018, 9, 6), '70142798': (2018, 9, 5), '80999063': (2018, 10, 5), '80190843': (2018, 9, 7), '80119349': (2017, 9, 29), '70062814': (2018, 9, 5), '80182115': (2017, 9, 29), '80187722': (2018, 10, 12), '70213237': (2018, 10, 2), '70121522': (2019, 8, 1)}
    """
    id_to_date = {}
    for show in lo_shows:
        id_to_date[show[ID]] = show[DATE_ADDED]
    return id_to_date

def create_id_cast(lo_shows:list[Show]) -> dict[str: list[str]]:
    """
    >>> create_id_cast([])
    {}

    # doctest: +NORMALIZE_WHITESPACE
    >>> create_id_cast([('81217749', 'Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], 'India:United States', (2019, 11, 15), '2018', 'TV-PG', '74 min', ['Documentaries', 'International Movies'], 'A trio of filmmakers treks across India to explore the correlation between vanishing rivers and massive energy projects and renewable energy sources.'), ('70303496', 'Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], 'India', (2018, 9, 6), '2014', 'TV-14', '146 min', ['Comedies', 'Dramas', 'International Movies'], 'Aamir Khan teams with director Rajkumar Hirani to play a social crusader in a political satire on the state of corruption in India.'), ('70142798', 'Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], 'Thailand', (2018, 9, 5), '2009', 'TV-MA', '125 min', ['Horror Movies', 'International Movies'], 'From disfiguring punishments to festering souls. Thai horror masters present five supernatural tales of karma in this sequel to the 4bia anthology.'), ('80999063', 'Movie', 'Super Monsters Save Halloween', [''], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '', (2018, 10, 5), '2018', 'TV-Y', '25 min', ['Children & Family Movies'], "The Super Monsters use their powers to get their neighbors in the Halloween spirit:then help a nervous friend see there's nothing to be afraid of."), ('80190843', 'TV Show', 'First and Last', [''], [''], '', (2018, 9, 7), '2018', 'TV-MA', '1 Season', ['Docuseries'], "Take an intimate look at the emotionally charged first and last days of new and soon-to-be released inmates at Georgia's Gwinnett County Jail."), ('80119349', 'Movie', 'Out of Thin Air', ['Dylan Howitt'], [''], '', (2017, 9, 29), '2017', 'TV-14', '85 min', ['Documentaries', 'International Movies'], 'Picking up 40 years after six were convicted for two strange murders in Iceland:this chilling documentary proves confessions can’t always be trusted.'), ('70062814', 'Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], 'Thailand', (2018, 9, 5), '2004', 'TV-MA', '96 min', ['Horror Movies', 'International Movies'], 'After killing a young girl in a hit-and-run accident:a couple is haunted by more than just the memory of their deadly choice.'), ('80182115', 'Movie', 'Long Shot', ['Jacob LaMendola'], [''], 'United States', (2017, 9, 29), '2017', 'TV-14', '40 min', ['Documentaries'], "When Juan Catalan is arrested for a murder he didn't commit:he builds his case for innocence around raw footage from a popular TV show. A documentary."), ('80187722', 'TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], '', (2018, 10, 12), '2018', 'TV-MA', '1 Season', ['Docuseries'], 'Actor and fight enthusiast Frank Grillo travels the world:immersing himself in different fight cultures to understand their traditions and motivations.'), ('70213237', 'TV Show', "Monty Python's Almost the Truth", [''], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], 'United Kingdom', (2018, 10, 2), '2009', 'NR', '1 Season', ['British TV Shows', 'Docuseries'], 'The legacy of comedy group Monty Python:whose irreverent brand of humor has tickled the ribs of millions:is explored in this documentary.'), ('70121522', 'Movie', '3 Idiots', ['Rajkumar Hirani'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], 'India', (2019, 8, 1), '2009', 'PG-13', '164 min', ['Comedies', 'Dramas', 'International Movies'], "While attending one of India's premier colleges:three miserable engineering students and best friends struggle to beat the school's draconian system.")])
    {'81217749': ['Naseeruddin Shah'], '70303496': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], '70142798': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], '80999063': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '70062814': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], '80187722': ['Frank Grillo'], '70213237': ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], '70121522': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}
    """
    id_to_cast = {}
    for show in lo_shows:
        if show[CAST][0] == '':
            continue
        id_to_cast[show[ID]] = show[CAST]
    return id_to_cast

def create_catagory_id(lo_shows:list[Show]) -> dict[str: list[str]]:
    """
    >>> create_catagory_id([])
    {}

    # doctest: +NORMALIZE_WHITESPACE
    >>> create_catagory_id([('81217749', 'Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], 'India:United States', (2019, 11, 15), '2018', 'TV-PG', '74 min', ['Documentaries', 'International Movies'], 'A trio of filmmakers treks across India to explore the correlation between vanishing rivers and massive energy projects and renewable energy sources.'), ('70303496', 'Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], 'India', (2018, 9, 6), '2014', 'TV-14', '146 min', ['Comedies', 'Dramas', 'International Movies'], 'Aamir Khan teams with director Rajkumar Hirani to play a social crusader in a political satire on the state of corruption in India.'), ('70142798', 'Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], 'Thailand', (2018, 9, 5), '2009', 'TV-MA', '125 min', ['Horror Movies', 'International Movies'], 'From disfiguring punishments to festering souls. Thai horror masters present five supernatural tales of karma in this sequel to the 4bia anthology.'), ('80999063', 'Movie', 'Super Monsters Save Halloween', [''], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '', (2018, 10, 5), '2018', 'TV-Y', '25 min', ['Children & Family Movies'], "The Super Monsters use their powers to get their neighbors in the Halloween spirit:then help a nervous friend see there's nothing to be afraid of."), ('80190843', 'TV Show', 'First and Last', [''], [''], '', (2018, 9, 7), '2018', 'TV-MA', '1 Season', ['Docuseries'], "Take an intimate look at the emotionally charged first and last days of new and soon-to-be released inmates at Georgia's Gwinnett County Jail."), ('80119349', 'Movie', 'Out of Thin Air', ['Dylan Howitt'], [''], '', (2017, 9, 29), '2017', 'TV-14', '85 min', ['Documentaries', 'International Movies'], 'Picking up 40 years after six were convicted for two strange murders in Iceland:this chilling documentary proves confessions can’t always be trusted.'), ('70062814', 'Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], 'Thailand', (2018, 9, 5), '2004', 'TV-MA', '96 min', ['Horror Movies', 'International Movies'], 'After killing a young girl in a hit-and-run accident:a couple is haunted by more than just the memory of their deadly choice.'), ('80182115', 'Movie', 'Long Shot', ['Jacob LaMendola'], [''], 'United States', (2017, 9, 29), '2017', 'TV-14', '40 min', ['Documentaries'], "When Juan Catalan is arrested for a murder he didn't commit:he builds his case for innocence around raw footage from a popular TV show. A documentary."), ('80187722', 'TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], '', (2018, 10, 12), '2018', 'TV-MA', '1 Season', ['Docuseries'], 'Actor and fight enthusiast Frank Grillo travels the world:immersing himself in different fight cultures to understand their traditions and motivations.'), ('70213237', 'TV Show', "Monty Python's Almost the Truth", [''], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], 'United Kingdom', (2018, 10, 2), '2009', 'NR', '1 Season', ['British TV Shows', 'Docuseries'], 'The legacy of comedy group Monty Python:whose irreverent brand of humor has tickled the ribs of millions:is explored in this documentary.'), ('70121522', 'Movie', '3 Idiots', ['Rajkumar Hirani'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], 'India', (2019, 8, 1), '2009', 'PG-13', '164 min', ['Comedies', 'Dramas', 'International Movies'], "While attending one of India's premier colleges:three miserable engineering students and best friends struggle to beat the school's draconian system.")])
    {'Documentaries': ['81217749', '80119349', '80182115'], 'International Movies': ['81217749', '70303496', '70142798', '80119349', '70062814', '70121522'], 'Comedies': ['70303496', '70121522'], 'Dramas': ['70303496', '70121522'], 'Horror Movies': ['70142798', '70062814'], 'Children & Family Movies': ['80999063'], 'Docuseries': ['80190843', '80187722', '70213237'], 'British TV Shows': ['70213237']}
    """
    catagory_to_ids = {}
    for show in lo_shows:
        for catagory in show[CATAGORIES]:
            if catagory in catagory_to_ids.keys():
                catagory_to_ids[catagory].append(show[ID])
            else:
                catagory_to_ids[catagory] = [show[ID]]
    return catagory_to_ids

def create_id_title(lo_shows:list[Show]) -> dict[str: str]:
    """
    >>> create_id_title([])
    {}

    # doctest: +NORMALIZE_WHITESPACE
    >>> create_id_title([('81217749', 'Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], 'India:United States', (2019, 11, 15), '2018', 'TV-PG', '74 min', ['Documentaries', 'International Movies'], 'A trio of filmmakers treks across India to explore the correlation between vanishing rivers and massive energy projects and renewable energy sources.'), ('70303496', 'Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], 'India', (2018, 9, 6), '2014', 'TV-14', '146 min', ['Comedies', 'Dramas', 'International Movies'], 'Aamir Khan teams with director Rajkumar Hirani to play a social crusader in a political satire on the state of corruption in India.'), ('70142798', 'Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], 'Thailand', (2018, 9, 5), '2009', 'TV-MA', '125 min', ['Horror Movies', 'International Movies'], 'From disfiguring punishments to festering souls. Thai horror masters present five supernatural tales of karma in this sequel to the 4bia anthology.'), ('80999063', 'Movie', 'Super Monsters Save Halloween', [''], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], '', (2018, 10, 5), '2018', 'TV-Y', '25 min', ['Children & Family Movies'], "The Super Monsters use their powers to get their neighbors in the Halloween spirit:then help a nervous friend see there's nothing to be afraid of."), ('80190843', 'TV Show', 'First and Last', [''], [''], '', (2018, 9, 7), '2018', 'TV-MA', '1 Season', ['Docuseries'], "Take an intimate look at the emotionally charged first and last days of new and soon-to-be released inmates at Georgia's Gwinnett County Jail."), ('80119349', 'Movie', 'Out of Thin Air', ['Dylan Howitt'], [''], '', (2017, 9, 29), '2017', 'TV-14', '85 min', ['Documentaries', 'International Movies'], 'Picking up 40 years after six were convicted for two strange murders in Iceland:this chilling documentary proves confessions can’t always be trusted.'), ('70062814', 'Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], 'Thailand', (2018, 9, 5), '2004', 'TV-MA', '96 min', ['Horror Movies', 'International Movies'], 'After killing a young girl in a hit-and-run accident:a couple is haunted by more than just the memory of their deadly choice.'), ('80182115', 'Movie', 'Long Shot', ['Jacob LaMendola'], [''], 'United States', (2017, 9, 29), '2017', 'TV-14', '40 min', ['Documentaries'], "When Juan Catalan is arrested for a murder he didn't commit:he builds his case for innocence around raw footage from a popular TV show. A documentary."), ('80187722', 'TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], '', (2018, 10, 12), '2018', 'TV-MA', '1 Season', ['Docuseries'], 'Actor and fight enthusiast Frank Grillo travels the world:immersing himself in different fight cultures to understand their traditions and motivations.'), ('70213237', 'TV Show', "Monty Python's Almost the Truth", [''], ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], 'United Kingdom', (2018, 10, 2), '2009', 'NR', '1 Season', ['British TV Shows', 'Docuseries'], 'The legacy of comedy group Monty Python:whose irreverent brand of humor has tickled the ribs of millions:is explored in this documentary.'), ('70121522', 'Movie', '3 Idiots', ['Rajkumar Hirani'], ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey'], 'India', (2019, 8, 1), '2009', 'PG-13', '164 min', ['Comedies', 'Dramas', 'International Movies'], "While attending one of India's premier colleges:three miserable engineering students and best friends struggle to beat the school's draconian system.")])
    {'81217749': 'SunGanges', '70303496': 'PK', '70142798': 'Phobia 2', '80999063': 'Super Monsters Save Halloween', '80190843': 'First and Last', '80119349': 'Out of Thin Air', '70062814': 'Shutter', '80182115': 'Long Shot', '80187722': 'FIGHTWORLD', '70213237': "Monty Python's Almost the Truth", '70121522': '3 Idiots'}
    """
    id_to_title = {}
    for show in lo_shows:
        id_to_title[show[ID]] = show[TITLE]
    return id_to_title

def read_file(filename: str) -> (dict[str, Date], dict[str, list[str]],
                                dict[str, list[str]], dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    # doctest: +NORMALIZE_WHITESPACE
    >>> read_file('11lines_data.csv')
    ({'81217749': (2019, 11, 15), \
'70303496': (2018, 9, 6), \
'70142798': (2018, 9, 5), \
'80999063': (2018, 10, 5), \
'80190843': (2018, 9, 7), \
'80119349': (2017, 9, 29), \
'70062814': (2018, 9, 5), \
'80182115': (2017, 9, 29), \
'80187722': (2018, 10, 12), \
'70213237': (2018, 10, 2), \
'70121522': (2019, 8, 1)}, \
{'81217749': ['Naseeruddin Shah'], \
'70303496': ['Aamir Khan', \
'Anuskha Sharma', \
'Sanjay Dutt', \
'Saurabh Shukla', \
'Parikshat Sahni', \
'Sushant Singh Rajput', \
'Boman Irani', \
'Rukhsar'], \
'70142798': ['Jirayu La-ongmanee', \
'Charlie Trairat', \
'Worrawech Danuwong', \
'Marsha Wattanapanich', \
'Nicole Theriault', \
'Chumphorn Thepphithak', \
'Gacha Plienwithi', \
'Suteerush Channukool', \
'Peeratchai Roompol', \
'Nattapong Chartpong'], \
'80999063': ['Elyse Maloway', \
'Vincent Tong', \
'Erin Matthews', \
'Andrea Libman', \
'Alessandro Juliani', \
'Nicole Anthony', \
'Diana Kaarina', \
'Ian James Corlett', \
'Britt McKillip', \
'Kathleen Barr'], \
'70062814': ['Ananda Everingham', \
'Natthaweeranuch Thongmee', \
'Achita Sikamana', \
'Unnop Chanpaibool', \
'Titikarn Tongprasearth', \
'Sivagorn Muttamara', \
'Chachchaya Chalemphol', \
'Kachormsak Naruepatr'], \
'80187722': ['Frank Grillo'], \
'70213237': ['Graham Chapman', \
'Eric Idle', \
'John Cleese', \
'Michael Palin', \
'Terry Gilliam', \
'Terry Jones'], \
'70121522': ['Aamir Khan', \
'Kareena Kapoor', \
'Madhavan', \
'Sharman Joshi', \
'Omi Vaidya', \
'Boman Irani', \
'Mona Singh', \
'Javed Jaffrey']}, \
{'Documentaries': ['81217749', '80119349', '80182115'], \
'International Movies': ['81217749', \
'70303496', \
'70142798', \
'80119349', \
'70062814', \
'70121522'], \
'Comedies': ['70303496', '70121522'], \
'Dramas': ['70303496', '70121522'], \
'Horror Movies': ['70142798', '70062814'], \
'Children & Family Movies': ['80999063'], \
'Docuseries': ['80190843', '80187722', '70213237'], \
'British TV Shows': ['70213237']}, \
{'81217749': 'SunGanges', \
'70303496': 'PK', \
'70142798': 'Phobia 2', \
'80999063': 'Super Monsters Save Halloween', \
'80190843': 'First and Last', \
'80119349': 'Out of Thin Air', \
'70062814': 'Shutter', \
'80182115': 'Long Shot', \
'80187722': 'FIGHTWORLD', \
'70213237': "Monty Python's Almost the Truth", \
'70121522': '3 Idiots'})
    """
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    lo_shows = parse_data(filename)
    return (create_id_date(lo_shows), create_id_cast(lo_shows),
        create_catagory_id(lo_shows), create_id_title(lo_shows))


    


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]

    >>> query('fail1.csv', 'Comedies', (2019, 7, 28,), [])
    [('PK', '70303496')]

    >>> query('fail2.csv', 'International Movies', (2019, 7, 28), [])
    [('Out of Thin Air', '80119349'), ('PK', '70303496'), ('Phobia 2', '70142798'), ('Shutter', '70062814')]

    >>> query('fail3.csv', 'International Movies',\
(2019, 8, 9),\
['Peeratchai Roompol', 'RukhsarJirayu La-ongmanee', 'Ian James Corlett',\
 'Anuskha Sharma', 'Nattapong Chartpong', 'Erin Matthews', 'Sivagorn Muttamara',\
 'Graham Chapman', 'John Cleese', 'Kachormsak Naruepatr', 'Britt McKillip',\
 'Andrea Libman', 'Terry Jones', 'Vincent Tong', 'Saurabh Shukla',\
 'Titikarn Tongprasearth', 'Javed Jaffrey', 'Natthaweeranuch Thongmee',\
 'Elyse Maloway', 'Omi Vaidya', 'Aamir Khan', 'Naseeruddin Shah',\
 'Charlie Trairat', 'Chumphorn Thepphithak', 'Kareena Kapoor',\
 'Worrawech Danuwong', 'Boman Irani', 'Gacha Plienwithi',\
 'Sushant Singh Rajput', 'Marsha Wattanapanich', 'Diana Kaarina', 'Madhavan',\
 'Kathleen Barr', 'Frank Grillo', 'Nicole Theriault', 'Michael Palin',\
 'Parikshat Sahni', 'Alessandro Juliani', 'Mona Singh', 'Sanjay Dutt',\
 'Eric Idle', 'Terry Gilliam', 'Unnop Chanpaibool', 'Ananda Everingham',\
 'Nicole Anthony', 'Suteerush Channukool', 'Chachchaya Chalemphol',\
 'Achita Sikamana', 'Sharman Joshi'])
    [('Avatar', '946294'), ('Avengers Infinity War', '936789'), ('Guardians of the Galaxy', '913579'), ('Harry Potter and the Chamber of Secrets', '640621'), ('Harry Potter and the Prisoner of Azkaban', '610119'), ('Jurassic Park', '755325'), ('Star Wars: A New Hope', '625273'), ('Stranger Things', '875314'), ('The Lord of the Rings The Return of the King', '677033'), ('The Lord of the Rings The Two Towers', '990868'), ('The Shawshank Redemption', '777497'), ('The Witcher', '775729'), ('Westworld', '837526')]
    
    >>> query('large_data.csv', 'International Movies', (2016, 2, 10), [])
    [('Even the Rain', '70154110'), ('Fifty', '80082739'), ('How to Change the World', '80036832'), ('Ip Man', '70118799'), ('Ip Man 2', '70137753'), ('Just Another Love Story', '70084180'), ('Miss Julie', '80017275'), ('Stop at Nothing: The Lance Armstrong Story', '80007215'), ('Suburra', '80075009'), ('The Perfect Dictatorship', '80032640'), ('The Physician', '80014996'), ('The Square', '70268449'), ('This Was Tomorrow', '80092409'), ('Trailer Park Boys: Drunk:High and Unemployed: Live in Austin', '80081410'), ('Tyke Elephant Outlaw', '80066806'), ('Virunga', '80009431'), ("Winter on Fire: Ukraine's Fight for Freedom", '80031666')]
    """
    filtered_shows = []
    id_to_date, id_to_cast, catagory_to_ids, id_to_title = read_file(filename)
    if category in catagory_to_ids.keys():
        shows_in_catagory = catagory_to_ids[category]
    else:
        shows_in_catagory = []
    shows_with_actor_and_before_date = []
    for show_id in shows_in_catagory:
        if not actors:
            if is_before(id_to_date[show_id], date):
                shows_with_actor_and_before_date.append(show_id)
                continue
        elif show_id not in id_to_cast.keys():
            continue
        else:
            for actor in id_to_cast[show_id]:
                if is_before(id_to_date[show_id], date):
                    if actor in actors:
                        shows_with_actor_and_before_date.append(show_id)
                        break
    lo_id_titles = []
    for show_id in shows_with_actor_and_before_date:
        title, id = id_to_title[show_id], show_id
        if (title, id) not in lo_id_titles:
            lo_id_titles.append((id_to_title[show_id], show_id))
    return sorted(lo_id_titles)