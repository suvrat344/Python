# Write a function named dim_equal that accepts two matrices A and B as arguments. It should return True if the the dimensions of both matrices are the same, and False otherwise.
# Input                             Expected Output
# Test Case1
# [[1, 2], [3, 4]]                       True
# [[5, 6], [7, 8]]
# Test Case2
# [[1, 2], [3, 4], [5, 6]]               False
# [[7, 8], [9, 10]]

def dim_equal(A, B):
    row1,row2 = len(A),len(B)
    col1,col2 = 0,0
    
    for i in range(len(A)):
        col1 = len(A[i])
        break
    for i in range(len(A)):
        col2 = len(B[i])
        break
    
    if(row1 == row2 and col1 == col2):
        return True
    else:
        return False
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(dim_equal(A,B))