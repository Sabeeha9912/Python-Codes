#Taking 3 rows from user
matrix = []
print("Enter 3 rows for 3x3 matrix (each row must contain 3 numbers):")
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)
print("\nOriginal 3x3 Matrix:")  # to display matrix
for row in matrix:
   print(row)
transpose = [] # for transpose
for i in range(3):
    t_row = []
    for j in range(3):
        t_row.append(matrix[j][i])
    transpose.append(t_row)
print("\nTranspose of Matrix:")
for row in transpose:
    print(row)
