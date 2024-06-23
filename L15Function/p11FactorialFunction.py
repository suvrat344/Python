# Write a function named factorial that accepts an integer n as argument. It should return the factorial of n if n is a positive integer. It should return −1 if n is a negative integer, and it should return 1 if n is zero.
# Input                     Expected Output
# Test Case1
# 5                             120
# Test Case2
# 7                             5040

def factorial(n):
    if(n>1):
        fact = 1 
        for i in range(1,n+1):
            fact = fact * i
        return fact
    elif(n==1 or n== 0):
        return 1
    else:
        return -1
    
print(factorial(5))