def is_palindrome(n):
    strN = str(n)
    for i in range(0, len(strN)):
        if (strN[i] != strN[-(i + 1)]):
            return False

    return True

def largest_palindrome_product(start, ceiling):
    maxProduct = 0
    for i in range(ceiling - 1, start - 1, -1):
        for j in range(i, start - 1, -1):
            product = i * j
            if (is_palindrome(product)):
                maxProduct = max(maxProduct, product)
    
    return maxProduct

if __name__ == '__main__':
    start = 100
    ceiling = 1000
    print(largest_palindrome_product(start, ceiling))