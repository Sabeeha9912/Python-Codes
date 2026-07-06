#Conversion from celcius to faren.. lab 4
def find_cel(f):
   # f=0
    c=((f-32)*5)/9
    return(c)
print("Temperature in celsius is:",find_cel(97.8))
def find_faren(C):
     F=((C*9)/5)+32
     return(F) 
print("Temperature in farenheit  is:",find_faren(36.6))