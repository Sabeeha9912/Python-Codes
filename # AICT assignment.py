# AICT assignment
import math
N=input("Enter student's name:")
R=int(input("Enter student's Roll no.:"))
P=len(N)
print("Length of N IS:",P)
vowels="AEIOUaeiou"
V=0
for character in N:
    if character in vowels:
        V=V+1
print("No. of vowels are:",V)
#        1:
temp=V if V%2!=0 else V+1
odd_no=[]
if P%2!=0 and R%2!=0:
    for odd in range(20):
        print(temp)
        odd_no.append(temp)
        temp+=2
print("Sum of odd_no is:",sum(odd_no))
print("Product of odd no. is:",math.prod(odd_no))
#    2
temp2=V if V%2==0 else V+1
even_no=[]
if P%2==0 and R%2==0:
    for even in range(20):
        print(temp2)
        even_no.append(temp2)
        temp2+=2
print("Sum of even_no is:",sum(even_no))
print("Product of even_no is:",math.prod(even_no))
#    3
prime_no=[]
num=V 
count=0
if (P%2==0 and R%2!=0 ) or (P%2!=0 and R%2==0):
    while count<20:
        if num>1:
            for prime in range(2,int(math.sqrt(num)) +1):
                if num%prime==0:
                    break
            else:
                print(num)
                prime_no.append(num)
                count+=1
        num+=1
print("Prime_sum is:",sum(prime_no)) 
print("prime product is:",math.prod(prime_no))  

    




        
