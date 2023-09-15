import math


ASSCI_SKULL = """ _________
/         \\
| ''   '' |
\    A    /
 \ \"\"\"\"\" /
 |_______|"""

ASSCI_CROSSBONES = """\'\"\'    \'\"\'
 \\     /
   \\ /
     /\\
   /    \\
 \'\"\'    \'\"\'"""


LOGO_PREFFIX_SUFFIX = "/~~~~~~~~\\"

def print_ascci_skull():
    """
    Prints an ascci repersentation of a spiral:
    >>> print_ascci_skull()
     _________
    /         \\
    | ''   '' |
    \    A    /
     \ \"\"\"\"\" /
     |_______|
    """
    print(ASSCI_SKULL)


def print_ascci_crossbones():
    """
    Prints an assci repersentation of crossbones:
    >>> print_ascci_crossbones()
    \'\"\'    \'\"\'
     \\     /
       \\ /
         /\\
       /    \\
     \'\"\'    \'\"\'
    """
    print(ASSCI_CROSSBONES)

def print_logo():
    """
    Use print_assci_skull() and print_assci_crossbones() to generate a logo making sure to wrap the logo in the prefix/suffix string
    """
    print(LOGO_PREFFIX_SUFFIX)
    print_ascci_skull()
    print(LOGO_PREFFIX_SUFFIX)
    print_ascci_crossbones()
    print(LOGO_PREFFIX_SUFFIX)
    print_ascci_skull()
    print(LOGO_PREFFIX_SUFFIX)
    print_ascci_crossbones()
    print(LOGO_PREFFIX_SUFFIX)

def calculate_surface_area(height:float, diameter:float):
    """
    Take the hight of a cylinder and its diameter to calculate it's surface area, we can do this by first calcuating the 
    circumference of a circle with the same diameter and multiplying that circumference by the hight and adding the area 
    of two circles with the same diameter
    >>> calculate_surface_area(1.2, 3.5)
    cylinder area: 32.4
    >>> calculate_surface_area(0, 0)
    cylinder area: 0.0
    """
    radius = diameter / 2

    # first find circle with same diameter's circumference:
    # C = 2*pi*r
    circumference = 2 * math.pi * radius

    # add the area of the "wrap around" section of the cylinder
    area = circumference * height

    # find the area of one of the "caps" of the cylindar
    # A = pi * r^2
    
    cap_area = math.pi * (radius ** 2)

    # add the area of two caps to the total area and print
    area += 2 * cap_area

    print(f"cylinder area: {area:.1f}")

