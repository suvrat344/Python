# Accept a positive integer n as input, where n>1. Print PRIME if n is a prime number and NOTPRIME otherwise.
# Input                               Expected Output
# Test Case1
# 11                                     PRIME
# Test Case2
# 17                                     PRIME

n = int(input("Enter a positive integer : "))
isprime = 0
if(n>1):
    for i in range(2,n//2+1):
        if(n%i==0):
            isprime = 0
            break
        else:
            isprime = 1
else:
    print("NOTPRIME")
    
if(isprime or n==2):
    print("PRIME")
else:
    print("NOTPRIME")