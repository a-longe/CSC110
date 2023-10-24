import doctest
from math import log
from sys import set_int_max_str_digits
import random

global roll_count ; roll_count = 0

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

# increase max int->str size to accomodate perfect number calculator
set_int_max_str_digits(1_000_000)


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    
    die = random.randint(MIN_ROLL, MAX_ROLL)
    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))
    return die


def list_to_string(values:list[int]) -> str:
    string = ''
    for index, value in enumerate(values):
        string += str(value)
        if index != len(values) - 1:
            string += ','
    return string


def get_sequence(min_val:int, increment:int, max_val:int) -> str:
    """
    Similar to the range() function but instead of returning a itterable,
    return a string with commas separating the values
    >>> get_sequence(2, 5, 32)
    '2,7,12,17,22,27,32'
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    >>> get_sequence(1, 1, 7)
    '1,2,3,4,5,6,7'
    """
    # first create an itterable with the required values
    values = list(range(min_val, max_val + 1, increment))
    return list_to_string(values)


def digit_sum(num:int) -> int:
    """
    Returns the sum of the digits of the absolute value of the number
    given
    >>> digit_sum(-517)
    13
    >>> digit_sum(432)
    9
    """
    sum = 0
    abs_val = abs(num)
    while abs_val >= 1:
        sum += abs_val % 10
        abs_val //= 10
    return sum


def get_factors(num:int) -> list:
    """
    takes a number and returns all possible factors in a list, excluding
    the number itself
    >>> get_factors(6)
    [1, 2, 3]
    >>> get_factors(12)
    [1, 2, 3, 4, 6]
    """
    factor_list = []
    for possible_factor in range(1, num//2 + 1):
        if num % possible_factor == 0:
            # possible factor is a factor, add to factor string
            factor_list.append(possible_factor)
    return factor_list


def sum_factors(num:int) -> int:
    """
    Gets the sum of all possible factors of the given number
    excluding the number itself
    >>> sum_factors(6)
    6
    >>> sum_factors(12)
    16
    """
    sum = 0
    for factor in get_factors(num):
        sum += factor
    return sum


def is_perfect(num:int) -> bool:
    """
    Returns True if the number is a perfect number,
    which is true if the sum of it's factors is equal to 
    itself
    >>> is_perfect(6)
    True
    >>> is_perfect(4)
    False
    """
    return sum_factors(num) == num


def n_numbers(num_perfects:int) -> str:
    perfects = []
    testing = 1
    while len(perfects) < num_perfects:
        if sum_factors(testing) == testing:
            perfects.append(testing)
        testing += 1
    return list_to_string(perfects)

    
# PART 2 ------

PERFECT_ROLL_SCORE = 21
TRIO_ROLL_SCORE = 5

def calculate_score(dice:list[int], target:int) -> int:
    """
    Takes a list of the three dice rolls in your turn and returns the
    apporopriate score
    >>> calculate_score([5, 5, 5], 5)
    21
    >>> calculate_score([5, 5, 5], 6)
    5
    >>> calculate_score([4, 4, 4], 6)
    5
    >>> calculate_score([4, 4, 6], 6)
    1
    >>> calculate_score([4, 6, 6], 6)
    2
    """
    score = 0
    if dice[0] == target and dice[1] == target and dice[2] == target:
        score = PERFECT_ROLL_SCORE
    elif dice[0] == dice[1] and dice[1] == dice[2]:
        score = TRIO_ROLL_SCORE
    else:
        for roll in dice:
            if roll == target:
                score += 1
    if score == 1:
        print(f"scored: {score} point")
    else:
        print(f"scored: {score} points")
    return score


def roll_dice() -> list[int]:
    dice = [roll_one_die(), roll_one_die(), roll_one_die()]
    print(f"Three dice rolled: {dice[0]}, {dice[1]}, {dice[2]}")
    return dice
    

   

def take_turn(player:str, player_score:int, round:int) -> int:
    print(f"Player {player} is taking a turn in round {round}")
    roll = roll_dice()
    score = calculate_score(roll, round)
    player_score += score
    print(f"Total points: {player_score}\n")
    
    while not (score == 0 or player_score >= 21):
        roll = roll_dice()
        score = calculate_score(roll, round)
        player_score += score
        print(f"Total points: {player_score}\n")
        
    return player_score


def play_round(first_player:str, second_player:str, round:int) -> str:
    second_player_score = 0
    first_player_score = take_turn(first_player, 0, round)
    turn = 'second'
    while first_player_score < 21 and second_player_score < 21:
        if turn == 'first':
            first_player_score = take_turn(first_player, first_player_score, round)
            turn = 'second'
        elif turn == 'second':
            second_player_score = take_turn(second_player, second_player_score, round)
            turn = 'first'
    
    # determine winner
    if first_player_score >= second_player_score:
        # first wins
        winning_name = first_player

    else:
        # second wins
        winning_name = second_player

    # print win statement
    print(f"the winner of this round is: {winning_name}")
    print(f"{first_player} has {first_player_score} points and {second_player} has {second_player_score} points")
    return winning_name