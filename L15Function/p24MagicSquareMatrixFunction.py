# A n×n square matrix of positive integers is called a magic square if the following sums are equal:
# (1) row-sum: sum of numbers in every row; there are n such values, one for each row
# (2) column-sum: sum of numbers in every column; there are n such values, one for each column
# (3) diagonal-sum: sum of numbers in both the diagonals; there are two values
# There are n+n+2=2n+2 values involved. All these values must be the same for the matrix to be a magic-square.
# Write a function named is_magic that accepts a square matrix as argument and returns YES if it is a magic-square and NO 
# if it isn't one.
# Input                             Expected Output
# Test Case1
# 2
# 1 2                                    NO
# 2 1
# Test Case2
# 3
# 4 9 2
# 3 5 7                                  YES
# 8 1 6

def is_magic(mat):
    m = len(mat)
    d1sum, d2sum = 0, 0
    for i in range(m):
        d1sum += mat[i][i]
        d2sum += mat[i][m - i - 1]
    if not(d1sum == d2sum):
        return 'NO'
    for i in range(m):
        rsum, csum = 0, 0
        for j in range(m):
            rsum += mat[i][j]
            csum += mat[j][i]
        if not(rsum == csum == d1sum):
            return 'NO'
    return 'YES'

mat = [[1,2],[2,1]]
print(is_magic(mat))