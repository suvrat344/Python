# Implement the following functions.
# (1) Write a function named get_column that accepts a matrix named mat and a non-negative integer named col as arguments. 
# It should return the column that is at index col in the matrix mat as a list. Zero-based indexing is used here.
# (2) Write a function named get_row that accepts a matrix named mat and a non-negative integer named row as arguments. It 
# should return the row that is at index row in the matrix mat as a list. Zero-based indexing is used here.
# Input                                                  Expected Output
# Test Case1
# get_column([[1, 2], [3, 4]], 0)                           [1, 3]
# Test Case2
# get_row([[1, 2], [3, 4]], 1)                              [3, 4]

def get_column(mat, col):
    col_list = [ ]
    m = len(mat)
    for row in range(m):
        col_list.append(mat[row][col])
    return col_list

def get_row(mat, row):
    row_list = [ ]
    n = len(mat[0])
    for col in range(n):
        row_list.append(mat[row][col])
    return row_list

print(get_column([[1, 2], [3, 4]], 0))