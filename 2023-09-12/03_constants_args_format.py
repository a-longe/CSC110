
# def acres_to_sqr_meters():
#     acres = 5.7

#     sqr_meters = acres * 4046.85642
#     print('Area is: ', sqr_meters, 'm^2')


'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
How can we make this function easier for some reading it to quickly
comprehend what the function does?
'''

# we can remove any 'magic numbers' and replace them with constants and add comments
def acres_to_sqr_meters():
    """
    Converts 5.7 acres to square meters
    >>> acres_to_sqr_meters()
    ==> Area is: 23067.081594 m^2
    """
    acres = 5.7
    SQR_M_PER_ACRE = 4046.85642

    sqr_meters = acres * SQR_M_PER_ACRE
    print('Area is:', sqr_meters, 'm^2')

'''
Q1b. The acres_to_sqr_meters function is not very versatile -
it will only calculate the square meters for 5.7 acres!
Edit the function so that it will calculate the square meters
for ANY non-negative number of acres.
'''

# we can reordere the function by addinng acres as a argument to the function like this:
def better_acres_to_sqr_meters(acres: float):
    """
    This function will take the number of acres as an argument and convert it to m^2
    >>> better_acres_to_sqr_meters(5.7)
    ==> Area is: 23067.081594 m^2
    >>> better_acres_to_sqr_meters(0)
    ==> Area is: 0.0 m^2
    """
    sqr_meters = acres * 4046.85642
    print('Area is:', sqr_meters, 'm^2')

'''
Q2. Design a function that will take the name of the best team and
print out a cheer for that team.
'''

def cheer(team_name: str):
    """
    Take the name of a team as a argument and print out a cheer that includes that team's name
    >>> cheer("Riptide")
    ==> Riptide ON THREE! ONE TWO THREE Riptide!
    >>> cheer("JPod")
    ==> JPod ON THREE! ONE TOW THREE JPod!
    """
    print(f"{team_name} ON THREE! ONE TWO THREE {team_name}!")


'''
Q3. Design a function called print_bill that takes the
price of a clothing item. The function should print the bill
which should include the following items:
 the price, the PST amount, the GST amount, and the total bill including taxes
NOTE: PST is provincial sales tax at 7%
      GST is goods and services tax at 5%
'''

def print_bill(price: float):
    """
    Takes the price of an item and prints out a bill with the cost, PST, GST and total
    >>> print_bill(1)
    ==> Price: 1.00
        GST: 0.07
        PST: 0.05
        Total: 1.12
    >>> print_bill(10)
    ==> Price: 10.00
        GST: 0.70
        PST: 0.50
        Total: 11.20
    """
    GST_RATE = 0.07
    PST_RATE = 0.05
    DECIMAL_PLACES = 2
    gst = price * GST_RATE
    pst =  price * PST_RATE
    total = price + pst + gst
    print("-----BILL-----")
    print(f"Price: ${price:.2f}")
    print(f"GST:   ${gst:.2f}")
    print(f"PST:   ${pst:.2f}")
    print(f"Total: ${total:.2f}")


'''
Q4. Design a function that will take a person's name and age and will
print a personalized message for that person.
For example, if we call the function as: welcome('Amy', 21)
the function should print:  Welcome Amy! Amy's 21 years old.
'''

def birthday_card(name: str, age: int):
    """
    Take a name and age from the arguments and create a personalized birthday card
    >>> birthday_card("Alex", 17)
    ==> Happy Birthday Alex, I can believe that you're 17 years old!
    >>> birthday_card("Julian", 23)
    Happy Birthday Julian, I can believe that you're 23 years old!
    """
    print(f"Happy Birthday {name}! I can believe that you're {age} years old!")