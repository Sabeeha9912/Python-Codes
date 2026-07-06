def calculate_gpa():
    total_grade_points = 0
    total_credit_hours = 0
    subjects = int(input("Enter the number of subjects: "))
    for i in range(1, subjects + 1):
        print(f"\nSubject {i}:")
        grade_point = float(input("Enter the Grade Point: "))
        credit_hour = float(input("Enter the Credit Hours: "))
        total_grade_points += grade_point * credit_hour
        total_credit_hours += credit_hour
    gpa = total_grade_points / total_credit_hours
    #gpa=(grade_point*credit_hour)/credit_hour  . It can also be done at place of lines after input in loop.
    return gpa
gpa = calculate_gpa()
print(f"\nYour Semester GPA is: {gpa}")
 