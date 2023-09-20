import doctest

def print_longer(string1: str, string2: str):
    """
    Takes two strings and prints the longer of the two, if they are the same
    length print the first one
    >>> print_longer('a', 'aa')
    aa
    >>> print_longer('aaa', 'aa')
    aaa
    >>> print_longer('a', 'a')
    a
    >>> print_longer('', 'a')
    a
    """
    string1_length = len(string1)
    string2_length = len(string2)

    if string2_length > string1_length:
        print(string2)
    else:
        print(string1)


def print_real_roots(a:float, b:float, c:float):
    """
    Using the quadratic equasion, determine the root of a trinomial with coefficents
    a, b and c
    >>> print_real_roots(0, 3, 6)
    ERROR
    >>> print_real_roots(1, 1, 5)
    NO REAL ROOTS
    >>> print_real_roots (1, 6, 9)
    -3.000,-3.000
    >>> print_real_roots(1, 4, 4)
    -2.000,-2.000
    >>> print_real_roots(2, -8, 8)
    2.000,2.000
    >>> print_real_roots(1, 0, 0)
    0.000,0.000
    >>> print_real_roots(1, 1, 0)
    0.000,-1.000
    >>> print_real_roots(1, 0, 1)
    NO REAL ROOTS
    """
    DESCRIMINANT = (b ** 2) - (4 * a * c)

    if a == 0:
        print("ERROR")
    elif DESCRIMINANT < 0:
        print("NO REAL ROOTS")
    else:
        # There are real roots so compute quadratic formula and print x to 3dp
        # to accout for the +- we need two variable to hold the roots

        first_root = ((b * -1) + (DESCRIMINANT ** 0.5)) / (2 * a)
        second_root = ((b * -1) - (DESCRIMINANT ** 0.5)) / (2 * a)
        print(f"{first_root:.3f},{second_root:.3f}")


CHANGE_DATE_JAN = 20
CHANGE_DATE_FEB = 19
CHANGE_DATE_MAR = 21
CHANGE_DATE_APR = 20
CHANGE_DATE_MAY = 21
CHANGE_DATE_JUN = 21
CHANGE_DATE_JUL = 23
CHANGE_DATE_AUG = 23
CHANGE_DATE_SEP = 23
CHANGE_DATE_OCT = 23
CHANGE_DATE_NOV = 22
CHANGE_DATE_DEC = 22

def print_zodiac_sign(month:str, day:int):
    """
    Precondition: input must be valid date
    Takes the month as a string and a day as an integer and prints out what
    zodiac sign that date coresponds to
    >>> print_zodiac_sign("January", CHANGE_DATE_JAN)
    Aquarius
    >>> print_zodiac_sign("February", CHANGE_DATE_FEB - 1)
    Aquarius
    >>> print_zodiac_sign("February", CHANGE_DATE_FEB)
    Pisces
    >>> print_zodiac_sign("March", CHANGE_DATE_MAR - 1)
    Pisces
    >>> print_zodiac_sign("March", CHANGE_DATE_MAR)
    Aries
    >>> print_zodiac_sign("April", CHANGE_DATE_APR - 1)
    Aries
    >>> print_zodiac_sign("April", CHANGE_DATE_APR)
    Taurus
    >>> print_zodiac_sign("May", CHANGE_DATE_MAY - 1)
    Taurus
    >>> print_zodiac_sign("May", CHANGE_DATE_MAY)
    Gemini
    >>> print_zodiac_sign("June", CHANGE_DATE_JUN - 1)
    Gemini
    >>> print_zodiac_sign("June", CHANGE_DATE_JUN)
    Cancer
    >>> print_zodiac_sign("July", CHANGE_DATE_JUL - 1)
    Cancer
    >>> print_zodiac_sign("July", CHANGE_DATE_JUL)
    Leo
    >>> print_zodiac_sign("August", CHANGE_DATE_AUG - 1)
    Leo
    >>> print_zodiac_sign("August", CHANGE_DATE_AUG)
    Virgo
    >>> print_zodiac_sign("September", CHANGE_DATE_SEP - 1)
    Virgo
    >>> print_zodiac_sign("September", CHANGE_DATE_SEP)
    Libra
    >>> print_zodiac_sign("October", CHANGE_DATE_OCT - 1)
    Libra
    >>> print_zodiac_sign("October", CHANGE_DATE_OCT)
    Scorpio
    >>> print_zodiac_sign("November", CHANGE_DATE_NOV - 1)
    Scorpio
    >>> print_zodiac_sign("November", CHANGE_DATE_NOV)
    Sagittarius
    >>> print_zodiac_sign("December", CHANGE_DATE_DEC - 1)
    Sagittarius
    >>> print_zodiac_sign("December", CHANGE_DATE_DEC)
    Capricorn
    >>> print_zodiac_sign("January", CHANGE_DATE_JAN - 1)
    Capricorn
    """

    sign = ""

    match month:
        case "January":
            # Capricorn or Aquarius
            if day < CHANGE_DATE_JAN:
                sign = "Capricorn"
            else:
                sign = "Aquarius"

        case "February":
            # Aquarius or Pisces
            if day < CHANGE_DATE_FEB:
                sign = "Aquarius"
            else:
                sign = "Pisces"

        case "March":
            # Pisces or Aries
            if day < CHANGE_DATE_MAR:
                sign = "Pisces"
            else:
                sign = "Aries"

        case "April":
            # Aries or Taurus
            if day < CHANGE_DATE_APR:
                sign = "Aries"
            else:
                sign = "Taurus"

        case "May":
            # Taurus or Gemini
            if day < CHANGE_DATE_MAY:
                sign = "Taurus"
            else:
                sign = "Gemini"

        case "June":
            # Gemini or Cancer
            if day < CHANGE_DATE_JUN:
                sign = "Gemini"
            else:
                sign = "Cancer"

        case "July":
            # Cancer or Leo
            if day < CHANGE_DATE_JUL:
                sign = "Cancer"
            else:
                sign = "Leo"

        case "August":
            # Leo or Virgo
            if day < CHANGE_DATE_AUG:
                sign = "Leo"
            else:
                sign = "Virgo"

        case "September":
            # Virgo or Libra
            if day < CHANGE_DATE_SEP:
                sign = "Virgo"
            else:
                sign = "Libra"

        case "October":
            # Libra or Scorpio
            if day < CHANGE_DATE_OCT:
                sign = "Libra"
            else:
                sign = "Scorpio"

        case "November":
            # Scorpio or Sagittarius
            if day < CHANGE_DATE_NOV:
                sign = "Scorpio"
            else:
                sign = "Sagittarius"

        case "December":
            # Sagittarius or Capricorn
            if day < CHANGE_DATE_DEC:
                sign = "Sagittarius"
            else:
                sign = "Capricorn"

    print(sign)