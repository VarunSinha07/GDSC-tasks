n = int(input("Enter the order of the square matrix: "))
matrix = []

print("Enter the entries row wise one by one:")
 
# For user input
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(n):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

# Sort non-boundary elements
non_boundary = []
for i in range(1, n-1):
    for j in range(1, n-1):
        non_boundary.append(matrix[i][j])
non_boundary.sort()

index = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        matrix[i][j] = non_boundary[index]
        index += 1

# Calculate sum of diagonal elements
diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]  # Sum of main diagonal
    diagonal_sum += matrix[i][n-i-1]  # Sum of secondary diagonal

print("Sorted matrix:")
for row in matrix:
   print(*row)  # Print row elements separated by spaces

print("Sum of diagonal elements:", diagonal_sum)
