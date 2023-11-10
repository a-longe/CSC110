import doctest

ResterauntData = tuple[str, float, str, list[str]]
NAME = 0
RATING = 1
PRICE_POINT = 2
TYPE = 3

''' Q1. Create and return an inverted version of a
dictionary of type dict[str, int] passed as an argument.
Each unique value in the input dictionary becomes a key in the output dictionary.
'''
def invert_dict(dictionary:dict[str, int]) -> dict[int, list[str]]:
    """
    Inverts a dictionary so that the keys become the values and the values
    become the keys

    >>> invert_dict({'a': 1, 'b':2, 'c':3})
    {1: ['a'], 2: ['b'], 3: ['c']}
    >>> invert_dict({'a': 1, 'b':1, 'c':1})
    {1: ['a', 'b', 'c']}
    >>> invert_dict({})
    {}
    >>> invert_dict({'abc':6})
    {6: ['abc']}
    """
    inverted_dictionary = {}
    for key, value in dictionary.items():
        if value not in inverted_dictionary.keys():
            inverted_dictionary[value] = [key]
        else:
            inverted_dictionary[value].append(key)
    return inverted_dictionary

'''
Q2. Imagine you have a file filled with rows of restaurant data, 
where each row has the following information, separated by commas :
- the restaurant name
- the rating of that restaurant
- a number of dollar signs representing the price point of that restaurant
- the types of food served by that restaurant (at least one)
(see sample text file provided: restaurant_data.txt)

Problem Description
You want to write a recommender function (with necessary helper functions) 
that will allow someone to specify: 
the name of the input file holding the restaurant data, 
the price they want to pay 
and a set of food types they are interested in.

The program should find all the restaurants that are at 
that price point and that serve at least one of the food types 
the person is interested in.
The program should give them a list of the restaurant names with their ratings, 
in order of increasing rating.

Not sure where to start...
1. Work through an example
- What inputs (arguments) should the function take?
- What should the function output (return)?

2. Where should you store the data as it is read in from the file?
- what items within a line of data would it be useful to filter on? 
  By filter we mean, which items within a line of the data should be 
  considered to decide if the restaurant on that line of data should be 
  included in the report to the user.
- What dictionaries will you want your program to create to help 
  with filtering the data.
  Think about what you want to filter on, and what you want to produce.
  -> What you filter on is the key and what you produce is the value.
  
3. What steps will your program need to perform to solve this problem? 
'''

def get_restraunt_data(filename:str) -> list[ResterauntData]:
    """
    Takes a filename and will return a list of resteraunt data

    >>> get_restraunt_data('restaurant_data.txt')
    [('Clarke&Co', 4.5, '$$$', ['Canadian']), \
('Red Fish Blue Fish', 4.5, '$$', ['Fish and Chips', 'Seafood']), \
('Blue Fox Cafe', 4.5, '$$$', ['Breakfast and Brunch', 'Canadian']), \
('Jam Cafe', 4.5, '$$', ['Breakfast and Brunch']), \
('Il Terrazzo Ristorante', 4.5, '$$$', ['Italian']), \
('Il Covo Trattoria', 4.0, '$$', ['Italian']), \
('Nautical Nellies', 4.0, '$$', ['Seafood', 'Steakhouses']), \
("Cora's", 4.0, '$$', ['Breakfast and Brunch']), \
('The Pacific Restaurant', 4.0, '$$$', ['Canadian']), \
('Kuma Noodles Japan', 4.0, '$', ['Ramen']), \
('The Tartan Toque', 3.5, '$$', ['Canadian'])]
    """
    restaurants:list[ResterauntData] = []
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            name, rating_str, price, foods_str = line.split(',', 3)
            food_types = foods_str.split(',')
            rating = float(rating_str)
            restaurant = (name, rating, price, food_types)
            restaurants.append(restaurant)
    return restaurants


def create_price_restauraunt_dict(restaurants:list[ResterauntData]
                                  ) -> dict[str:list[str]]:
    

def create_restauraunt_rating(restaurants:list[ResterauntData]
                                  ) -> dict[str:float]:
    

def create_types_restauraunt(restaurants:list[ResterauntData]
                                  ) -> dict[str:list[str]]:
    
