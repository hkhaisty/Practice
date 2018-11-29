import prime_generator as pg

def nth_prime(n):
    return pg.generate_nth_prime(n)

if __name__ == '__main__':
    n = 10001
    print(nth_prime(n))
