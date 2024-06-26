# Write a function named rotate that accepts a matrix mat as argument. It should return a matrix that is rotated by 90 degree in the clockwise direction. For example:
# [a b   c        =>   [d  a
#  d e   f]             e  b
#                       f  c]
# Input                  Expected Output
# Test Case1
# 2,3                        4,1
# 1,2,3                      5,2
# 4,5,6                      6,3
# Test Case2
# 3,2                        5,3,1
# 1,2                        6,4,2
# 3,4
# 5,6
# Test Case3
# 3,3                        7,4,1
# 1,2,3                      8,5,2
# 4,5,6                      9,6,3                     
# 7,8,9

def get_column(mat, col):
    col_list = [ ]
    m = len(mat)
    for row in range(m):
        col_list.append(mat[row][col])
    return col_list

def transpose(mat):
    m, n = len(mat), len(mat[0])
    mat_trans = [ ]
    for i in range(n):
        mat_trans.append(get_column(mat, i))
    return mat_trans

def rotate(mat):
    mat_trans = transpose(mat)
    rotated_mat = [ ]
    m, n = len(mat_trans), len(mat_trans[0])
    for i in range(m):
        row = [ ]
        for j in range(n):
            row = [mat_trans[i][j]] + row
        rotated_mat.append(row)
    return rotated_mat