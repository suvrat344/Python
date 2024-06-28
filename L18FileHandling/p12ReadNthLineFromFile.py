# Write a function named read_line that accepts a text file named filename and a positive integer n as arguments. Within the function, read the file and return the nth line of the file. If the file has fewer than n lines, return the string 'None'.
# (1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.
# Input                                                        Expected Output
# Test Case1
# public_1.txt                                           2,Every human life is worth the same, and worth saving.
# 2
# Test Case
# public_2.txt
# 5                                                               None

def read_line(filename, n):
    flag = False
    with open(filename) as f:
        x = f.readlines()
        for i in range(len(x)):
            if(i==n-1):
                return x[i]
    if(flag==False):
        return None