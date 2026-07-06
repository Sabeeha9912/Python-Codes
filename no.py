# mysum = 0
# for i in range(7, 10):
#     mysum += i
# print(mysum)
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    print("sum is:",mysum) 
    if mysum == 7:
        break
    mysum += 1
print(mysum)

