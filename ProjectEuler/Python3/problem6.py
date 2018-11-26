def sum_of_squares(ceiling):
    return sum([n**2 for n in range(1, ceiling + 1)])

def square_of_sum(ceiling):
    return sum(list(range(1, ceiling + 1)))**2

def sum_square_difference(ceiling):
    return abs(sum_of_squares(ceiling) - square_of_sum(ceiling))

if __name__ == '__main__':
    ceiling = 100
    print(sum_square_difference(ceiling))