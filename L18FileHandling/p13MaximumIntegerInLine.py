# Write a function named get_max_line that accepts a text file named filename as argument. Each line in this file contains an integer. The function should return the line number that houses the maximum integer in the file. If multiple lines have the same maximum number, return the smaller of the two. Line numbers start from one and not zero.
# (1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.
# Input                       Expected Output
# Test Case1
# public_1.txt                        3
# Test Case
# public_2.txt                       23

def get_max_line(filename):
    max = 0
    with open(filename,"r") as f:
        line = 0
        for i in f:
            line = line + 1
            if(int(i)>max):
                max = int(i)
                l = line
    return l