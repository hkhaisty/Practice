#https://en.wikipedia.org/wiki/Pythagorean_triple
def special_pythagorean_triplet(target):
    for n in range(1, target):
        for m in range(n + 1, target):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == target:
                return a * b * c
    
    return -1


if __name__ == "__main__":
    target = 1000
    print(special_pythagorean_triplet(target))