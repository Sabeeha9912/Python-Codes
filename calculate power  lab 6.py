# calculate power
def power(base, exp):
    if exp == 0:          # base case
        return 1
    return base * power(base, exp - 1)
base = int(input("Enter the number: "))   # Taking input from the user
exp = int(input("Enter the power: "))
result = power(base, exp)
print("Result:", result)
