# fibnocci 
def febnocci(n):
    if n<=1:
        return n
    else:
        return febnocci(n-1)+febnocci(n-2)
print("1st 20 febnocci no. are:")
for i in range (20):
    print(febnocci(i),end="")