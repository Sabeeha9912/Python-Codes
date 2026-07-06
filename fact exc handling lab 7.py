# fact exc handling
import math
try:
    a=input("Enter any positive no.:")
    assert a.isdigit
    a=int(a)
    assert a>=0
    print(f"Factorial of {a} is:", math.factorial(a))
except AssertionError as ae:
    print("Error",ae)
except Exception as e:
    print("invalid input",e)
