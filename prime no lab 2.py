# For prime no.
import math
start=int(input("Enter a starting no:"))
end=int(input("Enter an ending no:"))
print(f"prime numbers between range {start} and {end} are:")
prime_no=[]
for n in range(start,end+1):
    if n>1:
        for a in range(2,int(math.sqrt(n))+1):
            if n%a==0:
                break
        else:
          print(n)
          prime_no.append(n)
          prime_sum =0
        
prime_sum=sum(prime_no)
print("sum of prime numbers in range are:",prime_sum)
          
          

          


    