# Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n], endpoints inclusive. If there are no prime numbers in the given range, then print 0.
# Input                         Expected Output
# Test Case1
# 10                                   17
# Test Case2
# 100                                  1060

n = int(input("Enter a positive integer : "))
s = 0
isPrime = False
for i in range(1,n + 1):
    for j in range(2,i // 2 + 1):
        if(i % j == 0):
            isPrime = False
            break
        else:
            isPrime = True
    if(isPrime or i == 2 or i == 3):
        s = s + i
print(s)