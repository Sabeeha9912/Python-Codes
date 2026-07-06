decimal= int(input("Enter any decimal no: "))
binary=''
# using loop
while decimal>0:
    remainder = decimal%2
    binary = str(remainder) + binary
    decimal=decimal//2
print("Binary:", binary)
