# Write a recursive function named fibo that accepts a positive integer n as argument and returns the nth Fibonacci number.
# For this problem, F1=F2 are the first two Fibonacci numbers.
# Test Case 1
# Input                               Expected Output
# 3                                        2
# Test Case2
# 10                                       55

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(3))