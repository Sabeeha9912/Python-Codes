#lab 4
user_input = input("Enter a string: ")
to_upper = lambda x: x.upper()     
upper_str = to_upper(user_input)
print(f"\nUppercase string: {upper_str}")
def invert(text):
    reversed_text = text[::-1]        
    print(f"Reversed string: {reversed_text}")
invert(upper_str)

