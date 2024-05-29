import math

def sieve(n):
    """ Generate a list of prime numbers up to n """
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(math.sqrt(n)) + 1):
        if sieve[start]:
            for i in range(start*start, n + 1, start):
                sieve[i] = False
    
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def nth_prime(n):
    """ Return the nth prime number (0-based index) """
    if n == 0:
        return 2
    
    # A rough estimate of the upper bound for the nth prime number
    upper_bound = n * math.log(n) + n * math.log(math.log(n))
    upper_bound = int(upper_bound) if upper_bound > 0 else 2
    
    primes = sieve(upper_bound)
    
    while len(primes) <= n:
        upper_bound *= 2
        primes = sieve(upper_bound)
    
    return primes[n]