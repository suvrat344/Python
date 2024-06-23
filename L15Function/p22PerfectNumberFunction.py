# A perfect number is a positive integer that is equal to the sum of all its divisors excluding itself. For example, 6 is a perfect number as 6=1+2+3.
# Write a function named is_perfect that accepts a positive integer n as argument and returns True if it is perfect, and False otherwise.
# Input                                  Expected Output
# Test Case1
# 8                                          False
# Test Case2
# 6                                          True

def is_perfect(num):
    fsum = 0
    for f in range(1, num):
        if num % f == 0:
            fsum += f
    return fsum == num
print(is_perfect(int(input("Enter a positive integer : "))))