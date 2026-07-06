#students in UET
a=input("Enter E_CAt base applied student's names separated by commas:")
E_Cat={x.strip().lower() for x in a.split(",")}
b=input("Enter non E_Cat base applied student's name separated by commas:")
NonE_Cat={x.strip().lower() for x in b.split(",")}
both=E_Cat.intersection (NonE_Cat )
print("Students applied in both E_Cat and non E_Cat are:",both)
total=E_Cat.union(NonE_Cat)
print("Total students applied in UET are:",len(total))