import doctest

# input file column information:
NAME   = 0
RATING = 1
PRICE  = 2
TYPES  = 3

# represents a restaurant rating as (rating, name)
# where 0 <= rating <= 5
RestaurantRating = tuple[float, str]

''' Q1. complete the solution to the problem from earlier in the week '''

def recommend(filename: str, price: str, food_types: list[str]
              ) -> list[RestaurantRating]:
    """
    return a list of RestaurantRating of only restaurants in filename
    with given price category and that serve at least one food in food_types.
    The returned list should be in sorted order.
    
    >>> recommend('empty.txt', '$$$', ['Canadian', 'Breakfast and Brunch'])
    []
    >>> recommend('restaurant_data.txt', '$$$', ['Canadian', 'Breakfast and Brunch'])
    [(4.0, 'The Pacific Restaurant'), (4.5, 'Blue Fox Cafe'), (4.5, 'Clarke&Co')]
    """
    # read the file into 3 dictionaries 
    name_to_rating, price_to_names, type_to_names = populate_dicts(filename)

    # get restaurants with given price point or food type  
    # -> filter for price first
    names_with_price = price_to_names[price]

    # keep only restaurants that serve the types of food in food_types
    names_with_food_and_price = keep_with_foodtype(names_with_price, 
                                                   type_to_names,
                                                   food_types)
    
    # get (rating, name) list of accumulated restaurant names

    # sort (rating, name) list
    
    # return sorted (rating, name) list
    
 
def populate_dicts(filename: str) -> (dict[str, float],
                                      dict[str, list[str]],
                                      dict[str, list[str]]):
    """ populates and returns 3 dictionaries based on data in file
    - dict[restaurant name, rating]
    - dict[price, list[restaurant names]]
    - dict[food type, list[restaurant names]]
    
    Precondition: filename exists and contains lines of restaurant data as:
    name, rating, price point, food types separated by commas

    >>> populate_dicts('empty.txt')
    ({}, {'$': [], '$$': [], '$$$': [], '$$$$': [], '$$$$$': []}, {})

    >>> populate_dicts('restaurant_data.txt') # doctest: +NORMALIZE_WHITESPACE
    ({'Clarke&Co': 4.5, 
      'Red Fish Blue Fish': 4.5, 
      'Blue Fox Cafe': 4.5, 
      'Jam Cafe': 4.5, 
      'Il Terrazzo Ristorante': 4.5, 
      'Il Covo Trattoria': 4.0,
      'Nautical Nellies': 4.0, 
      "Cora's": 4.0, 
      'The Pacific Restaurant': 4.0,
      'Kuma Noodles Japan': 4.0, 
      'The Tartan Toque': 3.5},
     {'$': ['Kuma Noodles Japan'], 
      '$$': ['Red Fish Blue Fish', 'Jam Cafe', 'Il Covo Trattoria', 
             'Nautical Nellies', "Cora's", 'The Tartan Toque'],
      '$$$': ['Clarke&Co', 'Blue Fox Cafe', 'Il Terrazzo Ristorante', 
              'The Pacific Restaurant'], 
      '$$$$': [], 
      '$$$$$': []},
     {'Canadian': ['Clarke&Co', 'Blue Fox Cafe', 
                   'The Pacific Restaurant', 'The Tartan Toque'],
      'Fish and Chips': ['Red Fish Blue Fish'],
      'Seafood': ['Red Fish Blue Fish', 'Nautical Nellies'],
      'Breakfast and Brunch': ['Blue Fox Cafe', 'Jam Cafe', "Cora's"],
      'Italian': ['Il Terrazzo Ristorante', 'Il Covo Trattoria'],
      'Steakhouses': ['Nautical Nellies'], 
      'Ramen': ['Kuma Noodles Japan']})
    """
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': [], '$$$$$': []}
    food_to_names = {}

    file = open(filename, 'r')

    for line in file:
        line = line.strip()
        items = line.split(',')

        name = items[NAME]
        rating = float(items[RATING])
        price = items[PRICE]
        types = items[TYPES:]

        name_to_rating[name] = rating
        price_to_names[price].append(name)

        for foodtype in types:
            if foodtype in food_to_names:
                food_to_names[foodtype].append(name)
            else:
                food_to_names[foodtype] = [name]

    file.close()

    return (name_to_rating, price_to_names, food_to_names)


def keep_with_foodtype(names: list[str], type_to_names: dict[str, list[str]],
                       food_types: list[str]) -> list[str]:
    """ returns a list of only the restaurant names from names
    that serve at least one of the given food_types

    >>> names = ['Clarke&Co', 'Blue Fox Cafe', 'Il Terrazzo Ristorante', 'The Pacific Restaurant']

    >>> type_to_names = {\
    'Canadian': ['Clarke&Co', 'Blue Fox Cafe', 'The Pacific Restaurant', 'The Tartan Toque'],\
    'Fish and Chips': ['Red Fish Blue Fish'],\
    'Seafood': ['Red Fish Blue Fish', 'Nautical Nellies'],\
    'Breakfast and Brunch': ['Blue Fox Cafe', 'Jam Cafe', "Cora's"],\
    'Italian': ['Il Terrazzo Ristorante', 'Il Covo Trattoria'],\
    'Steakhouses': ['Nautical Nellies'],\
    'Ramen': ['Kuma Noodles Japan']}

    >>> food_types = ['Canadian', 'Breakfast and Brunch']

    >>> keep_with_foodtype([], {}, [])
    []
    >>> keep_with_foodtype([], type_to_names, food_types)
    []
    >>> keep_with_foodtype(names, {}, food_types)
    []
    >>> keep_with_foodtype(names, type_to_names, [])
    []
    >>> keep_with_foodtype([], {}, food_types)
    []
    >>> keep_with_foodtype(names, {}, [])
    []
    >>> keep_with_foodtype([], type_to_names, [])
    []
    >>> keep_with_foodtype(names, type_to_names, food_types)
    ['Clarke&Co', 'Blue Fox Cafe', 'The Pacific Restaurant']
    """
    # TODO: complete


'''
Q2. Design a function called get_uncommon that takes two sentences as strings. 
The function should return a sorted list of the uncommon words, where
an uncommon word is defined as:
   a word that appears exactly once in one of the sentences, 
   but not in the other sentence.
Words will be separated by space within the sentence and the sentences
will not contain punctuation.
'''


'''
Q3. Design a function called are_isomorphic that takes two strings and 
determines whether they are isomorphic.  
Two strings are isomorphic if every character of the first string
has mapping to every character of the second string and vice-versa.

Example 1: 'AABCCA', 'XXQZZX' are isomorphic because:
- every 'A' in s1 corresponds to an 'X' in s2 and the reverse is true
- every 'B' in s1 corresponds to a 'Q' in s2 and the reverse is true
- every 'C' in s1 corresponds to a 'Z' in s2 and the reverse is true
Example 2: 'AABCCAD', 'XXQZZXX' are not isomorphic because:
- every 'A' in s1 corresponds to an 'X' in s2 
but every 'X' in s2 does not correspond to an 'A' in s1
'''