def sieve_of_erastosthenes(n):
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n):
        if (i * i >= n):
            break
        
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = False
    
    return isPrime

def generate_primes(n, method=sieve_of_erastosthenes):
    if method == sieve_of_erastosthenes:
        primes = method(n)
        return [i for i in range(len(primes)) if primes[i]]
