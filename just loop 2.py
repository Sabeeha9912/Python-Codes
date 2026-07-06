# Nested loop (2)
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()  #for new line.

for i in range(0,5,1):
     for j in range(1,i+1):
        print("*",end="")
     print()  #both have same output bcz at 0 starting value it will print nothing