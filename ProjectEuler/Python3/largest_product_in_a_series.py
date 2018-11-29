def largest_product(data, window):
    max_product = 0
    for i in range(len(data) - window):
        product = data[i]
        for j in range(i + 1, i + window):
            product *= data[j]
        max_product = max(max_product, product)
    
    return max_product

if __name__ == "__main__":
    data = list(map(lambda c : int(c), ''.join(open('data/problem8.txt').read().splitlines())))
    window = 13
    print(largest_product(data, window))