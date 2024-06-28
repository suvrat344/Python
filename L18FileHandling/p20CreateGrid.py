# Write a function named number_grid that accepts two positive integers m and n as arguments. Within the function, create a file named numgrid.csv. Write the first mn positive integers to the file in the following way:
# Each line should be a sequence of n comma-separated integers.
# There should be a total of m lines in the file.
# For example, for the case of m=5,n=3, the file should be:
# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12
# 13,14,15
# Input                     Expected Output
# Test Case1
# 5                            1,2,3
# 3                            4,5,6
#                              7,8,9
#                             10,11,12
#                             13,14,15


# Test Case2
# 3                            1,2,3,4,5
# 5                            6,7,8,9,10
#                             11,12,13,14,15

def number_grid(m, n):
    f = open('numgrid.csv', 'w')
    x = 1
    line = ''
    while x <= m * n:
        line = line + str(x)
        if x % n == 0:
            if x != m * n:
                line = line + '\n'
            f.write(line)
            line = ''
        else:
            line = line + ','
        x = x + 1
    f.close()