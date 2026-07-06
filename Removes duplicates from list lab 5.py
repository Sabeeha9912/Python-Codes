# Removes duplicates from list
lists=input("Enter some no.separated by commas:")
a= [int(x.strip()) for x in lists.split(",")]
new_list= []
for item in a:
    if item not in new_list:
        new_list.append(item)
print("new list after removing repeating values is:",new_list)
