import doctest

RestaurauntData = tuple[str, float, str, list[str]]
# input file column information:
NAME = 0
RATING = 1
PRICE_POINT = 2
TYPES = 3

# represents a restaurant rating as (rating, name)
# where 0 <= rating <= 5
RestaurantRating = tuple[float, str]

def get_restraunt_data(filename:str) -> list[RestaurauntData]:
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
    restaurants:list[RestaurauntData] = []
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            line = line.strip()
            name, rating_str, price, foods_str = line.split(',', 3)
            food_types = foods_str.split(',')
            rating = float(rating_str)
            restaurant = (name, rating, price, food_types)
            restaurants.append(restaurant)
    return restaurants


def create_price_restauraunt(restaurants:list[RestaurauntData]
                                  ) -> dict[str:list[str]]:
    price_restauraunt = {'$': [], '$$': [], '$$$': [], '$$$$': [], '$$$$$': []}
    for restaurant in restaurants:
        price_restauraunt[restaurant[PRICE_POINT]].append(restaurant[NAME])
    return price_restauraunt

def create_restauraunt_rating(restaurants:list[RestaurauntData]
                                  ) -> dict[str:float]:
    restaurant_rating = {}
    for resteraunt in restaurants:
        restaurant_rating[resteraunt[NAME]] = resteraunt[RATING]
    return restaurant_rating

def create_types_restauraunt(restaurants:list[RestaurauntData]
                                  ) -> dict[str:list[str]]:
    types_restaurant = {}
    for restauraunt in restaurants:
        for food_type in restauraunt[TYPES]:
            if food_type in types_restaurant.keys():
                types_restaurant[food_type].append(restauraunt[NAME])
            else:
                types_restaurant[food_type] = [restauraunt[NAME]]
    return types_restaurant

def recommend(filename: str, price: str, food_types: list[str]
              ) -> list[RestaurantRating]:
    """
    return a list of RestaurantRating of only restaurants in filename 
    with given price category and that serve at least one food in food_types.
    The returned list should be in sorted order by rating then restaurant name.
    
    >>> recommend('empty.txt', '$$$', ['Canadian', 'Breakfast and Brunch'])
    []
    >>> recommend('restaurant_data.txt', '$$$', \
                  ['Canadian', 'Breakfast and Brunch'] \
                 )  # doctest: +NORMALIZE_WHITESPACE
    [(4.0, 'The Pacific Restaurant'), 
     (4.5, 'Blue Fox Cafe'),
     (4.5, 'Clarke&Co')]
    """
    name_to_rating, price_to_names, food_to_names = populate_dicts(filename)
    restauraunts_in_price_range = price_to_names[price]
    restauraunts_with_food_type = []
    for food_type in food_types:
        if food_type in food_to_names.keys():
            restauraunts_with_food_type += food_to_names[food_type]

    # find restauraunts which are in both lists
    unsorted_answer = []
    for restauraunt in restauraunts_in_price_range:
        if restauraunt in restauraunts_with_food_type:
            unsorted_answer.append((name_to_rating[restauraunt], restauraunt))
    
    unsorted_answer.sort()
    return unsorted_answer
    
    
    
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
    restauraunt_data = get_restraunt_data(filename)
    name_rting = create_restauraunt_rating(restauraunt_data)
    price_restauraunts = create_price_restauraunt(restauraunt_data)
    food_type_restauraunts = create_types_restauraunt(restauraunt_data)

    return name_rting, price_restauraunts, food_type_restauraunts
