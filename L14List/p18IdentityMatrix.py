# An identity matrix is a square matrix which has ones on the main diagonal and zeros everywhere else. For example, the identity matrix of size 3×3 is:
# [1   0    0
#  0   1    0
#  0   0    1]

# Accept a positive integer n as input and print the identity matrix of size n×n. Your output should have n lines, where each line is a sequence of n comma-separated integers that corresponds to one row of the matrix.
# Input                  Expected Output
# Test Case1
# 2                         1,0
#                           0,1
# Test Case2
# 3                         1,0,0
#                           0,1,0
#                           0,0,1

n = int(input("Enter number of row : "))
I = [ ]
for i in range(n):
    row = [ ]
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    I.append(row)
    
for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(I[i][j], end = ',')
        else:
            print(I[i][j])