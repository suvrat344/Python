# A sequence of n terms (a1,a2,…,an) is called an Arithmetic progression (AP) if the difference between any two 
# consecutive terms stays constant. That is : a2-a1=a3−a2=⋯=an−an−1=d
# Some useful terms:
# a1 is the first term of the AP.
# d is called the common difference of the AP.
# n is the total number of terms in the AP.
# Write a function named write_AP that accepts the following arguments:
# a_1: first term of the AP, integer.
# d: common difference of the AP, integer.
# n: number of terms in the AP, positive integer.
# Within the function, create a file named out.txt and write the first n terms of the AP to it, one term on each line, starting from the first term.
# Input                           Expected Output
# Test Case1
# 1                                    1
# 3                                    4
# 5                                    7
#                                      10
#                                      13
# Test Case2
# 2                                     2
# -10                                  -8
# 3                                    -18

def write_AP(a_1, d, n):
    f = open('out.txt', 'w')
    x = a_1
    for i in range(n):
        line = f'{x}'
        if i != n - 1:
            line = line + '\n'
        f.write(line)
        x = x + d
    f.close()