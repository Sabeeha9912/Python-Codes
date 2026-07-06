# 2nd smallest element in list
a=[1,1,3,4,5,6]
new_list=[]
for item in a:
    if item not in new_list:
        new_list.append(item)
print(new_list)
new_list.sort()
print("2nd smallest no. is:",new_list[1])
