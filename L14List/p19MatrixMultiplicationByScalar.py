# Accept a square matrix A and an integer s as input and print the matrix s⋅A as output. Multiplying a matrix by an integer s is equivalent to multiplying each element of the matrix by s. For example:
# 2⋅[1   2   =   [2         4
#   3   4]       6         8]
# The first line of input is a positive integer, n, that denotes the dimension of the matrix A. Each of the next n lines contains a sequence of space-separated integers. The last line of the input contains the integer s.
# Print the matrix s⋅A as output. Each row of the matrix must be printed as a sequence of space separated integers, one row on each line. There should not be any space after the last number on each line. If the expected output looks exactly like the actual output and still you are getting a wrong answer, it is because of the space at the end.
# Input                  Expected Output
# Test Case1
# 2                        2 4
# 1 2                      6 8
# 3 4                        
# 2
# Test Case2
# 2                        50  100
# 10 20                    150 200                
# 30 40                         
# 5

n = int(input("Enter number of row : "))
matrix = [ ]
for i in range(n):
    row = [ ]
    for x in input(f"Enter {n} space separated integer : ").split(' '):
        row.append(int(x))
    matrix.append(row)
s = int(input("Enter multiplicative factor : "))

for row in range(n):
    for col in range(n):
        matrix[row][col] *= s

for row in range(n):
    for col in range(n):
        if col != n - 1:
            print(matrix[row][col], end = ' ')
        else:
            print(matrix[row][col])