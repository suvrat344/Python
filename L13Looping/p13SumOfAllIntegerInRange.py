# Accept two positive integers a and b as input. Print the sum of all integers in the range [1000,2000], endpoints 
# inclusive,that are divisible by both a and b. If you find no number satisfying this condition in the given range, then 
# print 0.
# Input                                         Expected Output
# Test Case1
# 100                                              4500
# 500                                             
# Test Case2
# 2                                                3000
# 1000

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
s = 0
for i in range(1000,2001):
    if(i%a==0 and i%b==0):
        s +=i
print(s)