# combination and permutation
from math import factorial
def permutation(n, r):
    return factorial(n) // factorial(n - r)
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("nPr:", permutation(n, r))
print("nCr:", combination(n, r))
