import prime_generator

def summation_of_primes(ceiling):
    primes = prime_generator.generate_primes(ceiling)
    return sum(primes)

if __name__ == "__main__":
    ceiling = 2000000
    print(summation_of_primes(ceiling))