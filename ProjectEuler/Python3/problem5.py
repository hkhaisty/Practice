def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def smallest_multiple(limit):
    divisors = list(range(limit, 0, -1))
    smallest_multiple = 2
    while (divisors):
        if smallest_multiple % divisors[-1] == 0:
            divisors.pop()
        else:
            smallest_multiple = lcm(smallest_multiple, divisors[-1])

    return smallest_multiple

if __name__ == '__main__':
    limit = 20
    print(smallest_multiple(limit))