# Consider a positive integer x that is a power of 2. The logarithm of x to the base 2 is the number of times 2 has to be multiplied with itself so get x, and is denoted by log2(x). For example, log2(4)=2. Note that log2(1)=0.
# Write a recursive function named logarithm that accepts this positive integer x as argument and returns log2(x).
# (1) Each test case will be a power of 
# (2) Use of Python's standard libraries is not allowed for this problem.
# Input                           Expected Output
# Test Case1
# 4                                     2
# Test Case2
# 16                                    4

def logarithm(x):
    if(x==1):
        return 0
    else:
        return logarithm(x//2) + 1
    
print(logarithm(4))
print(logarithm(16))