# Calculate inverse and errors
try:
    print("Enter 2x2 matrix.")
    a11=float(input("Enter a11:"))
    a12=float(input("Enter a12:"))
    a21=float(input("Enter a21:"))
    a22=float(input("Enter a22:"))
    det=a11*a22-a12*a21
    print(f"Determinant is {det} so:")  # determinant
    inv=[                               #inverse
        [a22/det,   -a12/det],
        [-a21/det,   a11/det],
    ]
    print("Inverse of matrix is:")
    for row in inv:
        print(row)
except ValueError:
    print("Value error.")
except AssertionError as ae:
    print("Error",ae)
except Exception as e:
    print("Unexpected error.",e)
