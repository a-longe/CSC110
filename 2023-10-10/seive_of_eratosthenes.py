import math

def seive_of_eratosthenes(num_primes:int) -> list:
    # first insstaciate array with len n with increasing numbers from 1
    # prime number theorum states that between 1 and n there will be n/ln(n) primes
    array_size = round(num_primes/math.log(num_primes, 10)) * 2
    possible_factors = [x for x in range(1, array_size)]
    print(possible_factors)
