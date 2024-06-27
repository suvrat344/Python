# The Collatz function is defined for a positive integer n as follows.
# f(n)= 3n+1     if n is odd
#       n/2      if n is even
# We consider the repeated application of the Collatz function starting with a given integer n, which results in the following sequence:
# f(n),f(f(n)),f(f(f(n))),…
# It is conjectured that no matter which positive integer n you start from, the sequence will always reach 1. For example, 
# if n=10, the sequence is:
# Seq No              n                               f(n)
# 1                   10                               5
# 2                   5                                16
# 3                   16                               8
# 4                   8                                4
# 5                   4                                2
# 6                   2                                1
# Thus, if you start from n=10, you need to apply the function f six times in order to first reach 1.
# Write a recursive function named collatz that accepts a positive integer n as argument, where 1<n≤32,000, and returns the number of times f has to be applied repeatedly in order to first reach 1.
# Input                    Expected Output
# Test Case1
# 7                             16
# Test Case2
# 10                            6
# Test Case3
# 101                           25

def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)
    
print(collatz(7))
print(collatz(10))
print(collatz(101))