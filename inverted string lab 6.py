# inverted string (recursion)
def invert_string(s):
    if len(s) == 0:        # base case
        return s
    return invert_string(s[1:]) + s[0]
text = input("Enter a string: ")
print("Inverted string:", invert_string(text))
