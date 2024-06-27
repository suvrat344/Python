# The factorial of a positive integer n is defined as follows:
#                                     n!=1⋅2⋅3⋯n
# Write a recursive function named factorial that accepts a positive integer n as argument and returns the factorial of n.
# Input                                   Expected Output
# Test Case1
# 3                                              6
# Test Case2
# 5                                              120

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(5))