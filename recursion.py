# simple recursion examples

def fact1(n):
    ''' Computes the factorial of a positive integer'''
    if n < 2: return 1
    return n * fact1(n-1)

# storing previous smaller results in this dict
# bigger results are computed but not used afterwards
saved = {}
def fact2(n):
    ''' Factorial using (some) memoization '''
    if n < 2: return 1
    if n not in saved:
        saved[n] = n * fact2(n-1)
    return saved[n]


def fibo1(n):
    ''' Computes whole Fibonacci secuence up to a positive integer, no recursion'''
    L = [1,1]
    if n<= 2: return L
    for i in range(n-2):
        L.append(L[-1] + L[-2])
    return L

def fibo2(n):
    ''' Nth fibonacci element using recursion'''
    return n if n < 2 else fibo2(n - 1) + fibo2(n -2)


print fact1(6)
print fact2(6)
print fact2(8)
from math import factorial
print factorial(6)


print fibo1(10)
print fibo2(10)
