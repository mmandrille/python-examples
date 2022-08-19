'''
    In mathematics, the Fibonacci numbers, commonly denoted Fn , 
    form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones.
    The sequence commonly starts from 0 and 1, although some authors omit the initial terms and start the sequence from 1 and 1 or from 1 and 2. 
    Starting from 0 and 1, the next few values in the sequence are:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

'''
# Imports
# importing libraries
import time
import math

# Definitions
def fibo_one(n): 
       a,b = 0,1 
       for i in range(1,n): 
           a, b = b, a + b # Nice swap
       return b

def fibo_recur(n):
   if n <= 1:
       return n
   else:
       return(fibo_recur(n-1) + fibo_recur(n-2))


cache = {0: 0, 1: 1} # Because we are going back its much faster
def fibo_recur_memo(n):
     if n in cache:  # Base case
         return cache[n]
     # Compute and cache the Fibonacci number
     cache[n] = fibo_recur_memo(n - 1) + fibo_recur_memo(n - 2)  # Recursive case
     return cache[n]    

def fibonacci_iterator(n):
    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


class FibonacciClass:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n): # After Instance we can use it as function
        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # We use recursive calling
            self.cache.append(fib_number) # We feed cache for next calling
        return self.cache[n]

if __name__ == '__main__':
    idx = 35
    fibclass = FibonacciClass()
    # Executions
    print(f"The Straight Fibonacci result for {idx} number in sequence is: {fibo_one(idx)}")
    print(f"The Cache Fibonacci result for {idx} number in sequence is: {fibo_recur_memo(idx)}")
    print(f"The Class Fibonacci result for {idx} number in sequence is: {fibclass(idx)}")
    print(f"The Fibonacci Iterator result for {idx} number in sequence is: {fibonacci_iterator(idx)}")
    print(f"The Basic Recursive Fibonacci result for {idx} number in sequence is: {fibo_recur(idx)}")
    
    
    
    