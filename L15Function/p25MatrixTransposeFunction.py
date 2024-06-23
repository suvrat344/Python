# The transpose of a matrix swaps its rows and columns:
# [ a  b   c    ==>     [a  d
#   d  e   f]            b  e
#                        c  f]
# Write a function named transpose that accepts a matrix mat as input and returns its transpose.
# Input                      Expected Output
# Test Case1
# 1,2,3                           1,4
# 4,5,6                           2,5
#                                 3,6

# Test Case2
# 1,2                            1,3,5
# 3,4                            2,4,6
# 5,6                              

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

mat = [[1,2,3],[4,5,6]]
print(transpose(mat))