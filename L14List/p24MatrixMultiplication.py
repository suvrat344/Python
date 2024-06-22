# Accept two square matrices A and B of dimensions n×n as input and compute their product AB.
# The first line of the input will contain the integer n. This is followed by 2n lines. Out of these, each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. Each of the last n lines is a sequence of comma-separated integers that denotes one row of the matrix B.
# Your output should again be a sequence of n lines, where each line is a sequence of comma-separated integers that denotes a row of the matrix AB.
# Input                        Expected Output
# Test Case1
# 2                               19,22
# 1,2                             43,50
# 3,4
# 5,6
# 7,8                                
# Test Case2
# 3                               2,3,4
# 1,0,0                           5,9,1
# 0,1,0                           10,12,13
# 0,0,1
# 2,3,4
# 5,9,1
# 10,12,13                                

n = int(input("Enter number of rows : "))

A = [ ]
for i in range(n):
    row = [ ]
    for x in input(f"Enter {n} comma separated integer : ").split(','):
        row.append(int(x))
    A.append(row)
    
B = [ ]
for i in range(n):
    row = [ ]
    for x in input(f"Enter {n} comma separated integer : ").split(','):
        row.append(int(x))
    B.append(row)

C = [ ]
for i in range(n):
    row = [ ]
    for j in range(n):
        row.append(0)
    C.append(row)

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
        if j != n - 1:
            print(C[i][j], end = ',')
        else:
            print(C[i][j])