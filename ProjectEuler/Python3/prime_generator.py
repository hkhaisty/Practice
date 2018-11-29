def sieve_of_erastosthenes(ceiling):
    isPrime = [True for _ in range(ceiling)]
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, ceiling):
        if (i * i >= ceiling):
            break
        
        if isPrime[i]:
            for j in range(i * i, ceiling, i):
                isPrime[j] = False
    
    return isPrime

def generate_primes(ceiling, method=sieve_of_erastosthenes):
    if method == sieve_of_erastosthenes:
        primes = method(ceiling)
        return [i for i in range(len(primes)) if primes[i]]

def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        
        i += 1

    return True

def generate_nth_prime(n):
    prime_count = 1
    curr = 1
    while prime_count < n:
        curr += 2
        if is_prime(curr):
            prime_count += 1

    return curr