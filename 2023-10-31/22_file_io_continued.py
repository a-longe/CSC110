import doctest

DATA_FILE_PATH = 'yvrTemperatures08.txt'

# repersents tempature reading for a day
TemperatureReading = tuple[float, float, float, float]
MIDNIGHT = 0
SIXAM = 1
NOON = 2
SIXPM = 3


''' Q1. In this problem, assume we have a file called yvrTemperatures08.txt
containing the temperature readings at Vancouver International Airport at
midnight, 6am, noon and 6pm on given days of the year 2008.
The meteorologists at the airport attempt to record data every day but
technical problems mean that data for some days of the year could go missing.
We know the file is formatted as follows:
- data for each day is on a line of its own
- the first entry is an integer from 1 to 366 (2008 was a leap year)
representing the day of the year
- the next four entries are floating point numbers representing the temperature at
midnight, 6am, noon and 6pm, in that order
- there is at least one line of data in the file

STEP 1: work through an example

Given the sample data file below:
1. Calculate the average temperature at
midnight, at 6am, at noon and 6pm across the days

2. :For each time (midnight, at 6am, at noon and 6pm), count the number of
readings that are above the calculated average for that time of day

1    3.4  2.3  3.5  5.4
74   1.2  1.2  2.3  2.2
298  -2.1 -0.1 1.0  0.5
366  1.3  1.3  2.4  2.1



STEP 2: Given your process for completing the above calculations,
design a program that, given the weather data in the file, prints
the average temperatures for the 4 times of day and the number of readings
across all days that are above the calculated average for each of the 4 times.

Think about what functions you will need to write.
Reading from a file is time consuming,
so make sure your design will only read from the file once!

What does the data you need to store look like?
Which function will you write first?
Which functions will need to call other functions?

Extension:  Write your results to an output file.
'''

def file_to_temperatures(file_name:str) -> list[TemperatureReading]:
    """
    reads data from a file with the format of each line being a day in the year,
    the first data point being the day of the year as an integer (January 1st
    would be 1) then, separated by whitespace there are 4 floats repersenting 
    the tempature at midnight, 6am, noon and 6pm
    >>> file_to_tempatures(DATA_FILE_PATH)
    [(3.4, 2.3, 3.5, 5.4), (1.2, 1.2, 2.3, 2.2), (-2.1, -0.1, 1.0, 0.5), (1.3, 1.3, 2.4, 2.1)]
    """
    readings = []
    with open(file_name, 'r') as file_handler:
        for day in file_handler:
            tempature_reading = tuple(day.split()[1:])
            tempature_reading = (int(string) for string in tempature_reading)
            readings.:append(tempature_reading)
    return readings


def get_avg_temp_at_times(readings:list[TemperatureReading]) -> list[float]:
    """
    Takes a list of tempature readings and will output a list of averages at the 
    different times midnight, 6am, noon, 6pm
    >>> get_avg_temp_at_times(file_to_tempatures(DATA_FILE_PATH))
    [0.95, 1.18, 2.30, 2.55]
    """
    sums = [0.0 * 4]
    for reading in readings:
        for time_index, temp in enumerate(reading):
            sums[time_index] = temp

    for index, sum in enumerate(sums):
        sums[index] = sum/len(sums)

    return sums

def analyze_tempatures(file_name:str) -> None:
    """
    Prints report on tempature data in the given file
    >>> analyze_tempatures(DATA_FILE_PATH)
    AVERAGES: 0.95, 1.18, 2.30, 2.55
    COUNTS: 3, 3, 2, 1
    """
    # read data and store to list
    temp_readings: list[TemperatureReading] = file_to_temperatures(file_name)

    # find average tempature

    # find how many readings are above the average every day

    # prints information
