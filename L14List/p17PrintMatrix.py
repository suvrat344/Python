# Accept a square matrix as input and store it in a variable named matrix. The first line of input will be, n, the number of rows in the matrix. Each of the next n lines will have a sequence of n space-separated integers.
# Input                                  Expected Output
# Test Case1
# 2
# 1 2                                      [[1, 2], [3, 4]]
# 3 4
# Test Case2
# 3
# 1 2 3
# 4 5 6                                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 7 8 9

n = int(input("Enter number of row in matrix : "))

matrix = [ ]
for i in range(n):
    L = [ ]
    for num in input(f"Enter {n} space separated integer : ").split(' '):
        L.append(int(num))
    matrix.append(L)
print(matrix)