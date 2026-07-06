#permutation and combination lab 4
import math
n=int(input("Enter any no. n:"))
r=int(input("Enter other no. r:"))
def combination(n,r):
    C=(math.factorial(n))//(math.factorial(r)*math.factorial(n-r))
    return(C)
print("Combination is:",combination(n,r))
def permutation(n,r):
    P=(math.factorial(n))//(math.factorial(n-r))
    return(P)
print("Permutation is:",permutation(n,r))



