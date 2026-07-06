#reverse
a=eval(input("Enter a list:"))
b=a.copy()
b.reverse()
if b==a:
    print("You entered a palindrome.")
else:
    print("you did not entered a palindrome.")

