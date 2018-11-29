def is_multiple_of_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0

def sum_of_multiples(ceiling):
    multipleSum = 0
    for n in range(ceiling):
        if is_multiple_of_3_or_5(n):
            multipleSum += n

    return multipleSum

if __name__ == '__main__':
    ceiling = 1000
    print(sum_of_multiples(ceiling))
