def is_even(n):
    return n % 2 == 0

def fibonacciEvenSum(ceiling):
    fibonacci = [1, 2]
    nextFib = 0
    index = 1
    evenSum = 2
    while nextFib <= ceiling:
        nextFib = fibonacci[index] + fibonacci[index - 1]
        fibonacci.append(nextFib)
        index += 1
        
        if (is_even(nextFib)):
            evenSum += nextFib
    
    return evenSum

if __name__ == '__main__':
    ceiling = 4000000
    print(fibonacciEvenSum(ceiling))