import doctest

# departure city, arival city, duration
Flight = tuple[str, str, float]
DEPATURE = 0
ARIVAL = 1
DURATION = 2


def swap(list:list, position1:int, position2:int) -> None:
    """
    Preconditions: position1 and position2 must be valid indecies for the list
    Takes a list and swaps the elements in the two given positions
    >>> x = [1,2,3,4]
    >>> swap(x, 0, 3)
    >>> x
    [4, 2, 3, 1]

    >>> x = [1,2,3]
    >>> swap(x, 0, 1)
    >>> x
    [2, 1, 3]
    """
    value1 = list[position1]
    value2 = list[position2]
    list[position1], list[position2] = value1, value2


VALUE = 0
INDEX= 1
def index_of_smallest(values:list) -> int:
    """
    finds the index of the smallest value in the list
    as determined by pythons > < and = opporators
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'A'])
    4
    """
    if len(values) > 0: smallest = (values[0], 0)
    else: return -1
    for index, value in enumerate(values):
        if value < smallest[VALUE]:
            smallest = (value, index)
    return smallest[INDEX]


def total_duration(flights:list[Flight]) -> int:
    """
    Finds the total duration in a list of flights
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    """
    sum = 0
    for flight in flights:
        sum += flight[DURATION]
    return sum


def get_destinations_from(flights:list[Flight], departure_city:str) -> list[str]:
    """
    returns a list with all unique destinations from the flights provided
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)], "Victoria")
    ['Vancouver', 'Calgary']
    """
    unique_destinations = []
    for flight in flights:
        if flight[DEPATURE] == departure_city and flight[ARIVAL] not in unique_destinations:
            unique_destinations.append(flight[ARIVAL])
    return unique_destinations