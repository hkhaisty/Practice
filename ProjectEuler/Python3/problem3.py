import prime_generator as pg

def largest_factor(n):
    primes = pg.generate_primes(int(n ** (1 / 2)))
    for i in range(1, len(primes)):
        if n % primes[-i] == 0:
            return primes[-i]

    return None

if __name__ == '__main__':
    n = 600851475143 
    print(largest_factor(n))
