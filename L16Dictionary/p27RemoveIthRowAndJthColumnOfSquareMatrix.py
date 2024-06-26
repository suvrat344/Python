# Given a square matrix M and two indices (i,j),Mij is the matrix obtained by removing the ith row and the jth column of M.
# Write a function named minor_matrix that accepts three arguments:
# M: a square matrix
# i: a non-negative integer
# j: a non-negative integer
# The function should return the matrix Mij after removing the ith row and the jth column of M. Note that we use zero-based indexing throughout. That is, if the matrix M is of dimensions n×n, then we have 0≤i,j≤n−1.
# (1) You can assume that the number of rows in M will be at least 3 in each test case.
# Input                             Expected Output
# Test Case1
# 3                                    4,6
# 1,2,3                                7,9
# 4,5,6
# 7,8,9
# 0
# 1
# Test Case2
# 3                                    2,3
# 1,2,3                                5,6
# 4,5,6
# 7,8,9
# 2
# 0

def minor_matrix(M, i, j):
    n = len(M)
    M_ij = [ ]
    for row in range(n):
        if row == i:
            continue
        L = [ ]
        for col in range(n):
            if col == j:
                continue
            L.append(M[row][col])
        M_ij.append(L)
    return M_ij