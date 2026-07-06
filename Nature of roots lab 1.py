# Nature of roots of quardratic equation
import math
a=int(input("Enter a no. a:"))
b=int(input("Enter a no. b:"))
c=int(input("Enter a no. c:"))
disc=b**2-4*a*c
if disc == 0:
    print("Roots are real,equal and rational.")
elif disc>0:
    print("Roots are real,distinct and irrational.")
else:
    print("Roots are imaginary.")
#calculate roots:
if disc>= 0:
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2=(-b - math.sqrt(disc))/(2*a)
    print("Root x1 is:" , root1)
    print("Root x2 is:", root2)


