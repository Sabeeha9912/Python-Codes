#polindrome
a=int(input("Enter a no:"))
b=0
temp=a
while temp>0:
    r=temp%10
    b=(b*10)+r
    temp=temp//10
    if b==a:
        print("you entered a polidrome")
    else:
        print("entered no is not a polidrome")
 