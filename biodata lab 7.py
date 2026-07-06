#biodata
def valid_bio(name,adrs,cnct_no,age,gender):
    if any (char.isdigit() for char in name):
        raise ValueError("Name cannot be in digits.")
    if len(adrs)<3:
        raise ValueError("Adress length cannot be less than 3.")
    if not cnct_no.isdigit():
        raise ValueError("Contact no. cannot have any alphabet.")
    if age<0 or age>150:
        raise ValueError("Age cannot be less than 0 and greater than 150.")
    if gender.lower() not in ["male" , "female"]:
        raise  ValueError("Gender can only b male and female.")
    print("Bio data is valid.")
try:
    name=input("Enter your name:")
    adrs=input("Enter your adress:")
    cnct_no=input("Enter your contact number:")
    age=int(input("Enter your age:"))
    gender=input("Enter your gender:")
    print(name,adrs,cnct_no,age,gender)
    valid_bio(name,adrs,cnct_no,age,gender)
except ValueError as ve:
    print("Value error",ve)
























