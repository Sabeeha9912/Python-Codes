# lambda function lab 4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
larger = (lambda x, y: x if x >= y else y)(a, b)
print(f"\nLarger number (from lambda): {larger}")
def print_table(n, start, end):
    for i in range(start, end + 1):
        print(f"{n} x {i} = {n * i}")
s = int(input("Enter table start: "))
e = int(input("Enter table end: "))
print_table(larger, s, e)

