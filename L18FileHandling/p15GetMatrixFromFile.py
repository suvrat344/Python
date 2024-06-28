# filename points to a file that contains a n×n matrix. The ith line of the file represents the (i−1)th row of the matrix as a sequence of comma separated integers, where 1≤i≤n. We have used zero-based indexing here. This file doesn't have a header and has exactly n lines. A sample file is given for your reference:
# 1,2,3
# 4,5,6
# 7,8,9
# Your task is to return the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Write a function named get_matrix that accepts the filename as argument. It should return the matrix as a list of lists. 
# Each cell of the matrix should be an integer and not a string.
# (1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.
# Input                                                        Expected Output
# Test Case1                              
# public_1.csv                                [[17, 16, 97, -56], [80, 0, 87, -11], [10, 29, -72, 36], [-69, -80, 88, 16]]
# Test Case2
# public_2.csv                                [[-48, 88, 81], [-93, -64, 58], [-32, -98, 77]]

def get_matrix(filename):
    l = []
    f  = open(filename,"r")
    x = f.readlines()
    for i in x:
        l1 = i.strip().split(",")
        l.append([])
        for j in l1:
            l[-1].append(int(j))
    return l