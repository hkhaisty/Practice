def is_even(n):
    return n % 2 == 0

def fibonacciEvenSum(limit):
    fibonacci = [1, 2]
    nextFib = 0
    index = 1
    evenSum = 2
    while nextFib <= limit:
        nextFib = fibonacci[index] + fibonacci[index - 1]
        fibonacci.append(nextFib)
        index += 1
        
        if (is_even(nextFib)):
            evenSum += nextFib
    
    return evenSum

if __name__ == '__main__':
    limit = 4000000
    print(fibonacciEvenSum(limit))