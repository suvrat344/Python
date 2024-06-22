# Accept two square matrices A and B of dimensions n×n as input and compute their sum A+B.The first line will contain the integer n. This is followed by 2n lines. Each of the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. Each of the last n lines is a sequence of comma-separated integers that denotes one row of the matrix B.
# Your output should again be a sequence of n lines, where each line is a sequence of comma-separated integer that denotes a row of the matrix A+B.
# Input                      Expected Output
# Test Case1
# 2
# 1,2                          6,8
# 3,4                         10,12
# 5,6
# 7,8                            
# Test Case2
# 3
# 1,0,1                      1,0,2
# 0,1,0                      0,2,0
# 1,0,1                      2,0,1
# 0,0,1
# 0,1,0
# 1,0,0                           
                           
n = int(input("Enter number of row : "))

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
        C[i][j] = A[i][j] + B[i][j]
        if j != n - 1:
            print(C[i][j], end = ',')
        else:
            print(C[i][j])