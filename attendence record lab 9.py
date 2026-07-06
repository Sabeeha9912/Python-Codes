# attendence record
classes=20
min_classes=15
attandance={}
st_no=int(input("Enter no of students."))
for n in range(st_no):
    name=input("Enter student name:")
    attended=int(input("Enter no. of attended classes:"))
    attandance[name]=attended
for name,attended in attandance.items():
    percentage=((attended*100)/classes)
    if percentage>=75:
        print("Eligible")
    else:
        print("Not eligible")

