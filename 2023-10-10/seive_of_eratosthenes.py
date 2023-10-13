import time
from functools import wraps
from math import log

num_expected_primes = {
    10: 4,
    100: 25,
    1_000: 168,
    10_000: 1_229,
    100_000: 9_592,
    1_000_000: 78_498,
    10_000_000: 664_579,
    100_000_000: 5_761_455,
    1_000_000_000: 50_847_534
}


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args[:len(args)-1]} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


# Theorem: pn = n (log n + log log n - 1 + (log log (n) - 2)/log n - ((log log (n))2 - 6 log log (n) + 11)/(2 log2 n)).
def nth_prime(n):
    log_n = log(n)
    log_log_n = log(log_n)
    return round(n * (log_n + log(log(n-1)) + (log_log_n - 2) / log_n - ((log_log_n) * 2 - 6 * log_log_n + 11) / (2 * log(n, 2))))


def get_multiples(num:int, to:int) -> list:
    num_multiples = to // num
    multiples = []
    for i in range(2, num_multiples + 1):
        multiples.append(num * i)
    return multiples

@timeit
def find_n_primes(num_primes) -> list:
    if num_primes < 1000:
        n = 1000
    else: n = num_primes
    array_len = nth_prime(n)
    return seive_of_eratosthenes(array_len, False)[:num_primes]

@timeit
def seive_of_eratosthenes(to_num:int, do_debug:bool) -> list:
    # first insstaciate array with len n with increasing numbers from 1
    is_prime:list = [True for i in range(to_num)]

    # create a list of possible factors for all numbers up to to_num
    largest_possible_factor = int(0.5 * to_num)+1
    possible_factors = [factor for factor in range(2, largest_possible_factor)]
    if do_debug: print("All Possible Factors:", possible_factors)

    # loop through each possible_factor and for each possible_factor loop through
    # each multiple of that number to set respective index to false in is_prime
    # list
    for possible_factor in possible_factors:
        # if possible_factor is already determined to not be prime,
        # Do not need to check all of it's multiples because they must have
        # already been determined to not be prime
        if not is_prime[possible_factor - 1]:
            # skip this itteration of possible factors, move onto next
            if do_debug: print("skipped", possible_factor)


        multiples = get_multiples(possible_factor, to_num)
        for multiple in multiples:
            multiple_index = multiple - 1
            if do_debug: print(possible_factor, multiple, "is not prime")
            is_prime[multiple_index] = False

    primes:list = []
    # now we have a list of booleans that repersent which numbers are is_prime
    # convert this to a list of numbers
    for index, bool in enumerate(is_prime):
        if bool:
            primes.append(index + 1)

    return primes[1:]

@timeit
def test_accuracy(search_to:int) -> None:
    num_primes = len(seive_of_eratosthenes(search_to, False))
    if not num_primes == num_expected_primes[search_to]:
        print(f"FAILED - {search_to}")
    else:
        print(f"PASSED - {num_primes}")
