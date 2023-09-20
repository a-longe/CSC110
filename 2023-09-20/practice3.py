YEAR_ON_EARTH = 365
YEAR_ON_MARS = 687

def print_planet_age(days_old:int):
    earth_years = days_old // YEAR_ON_EARTH
    mars_years = days_old // YEAR_ON_MARS
    if earth_years > 1: earth_suffix = "years" 
    else: earth_suffix = "year"
    if mars_years > 1: mars_suffix = "years"
    else: mars_suffix = "year" 
    print(f"Earth age: {earth_years} {earth_suffix}")
    print(f"Mars age: {mars_years} {mars_suffix}")