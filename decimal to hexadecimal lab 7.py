# Convert decimal to hexadecimal
def dec_to_hex(n):
    try:
        return hex(n)[2:]  # convert to hex and remove '0x'
    except TypeError:
        print("TypeError: UDF cannot accept a string or invalid type")
try:                                  # Main program
    user_input = int(input("Enter any decimal number: "))
    print("Hexadecimal value is:", dec_to_hex(user_input))
finally:
    print("UDF call successfully.")
