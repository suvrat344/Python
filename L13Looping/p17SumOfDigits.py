# Accept a positive integer as input and print the sum of the digits in the number.
# Input                               Expected Output
# Test Case1
# 123456                                  21
# Test Case2
# 67127                                   23

num = int(input("Enter a positive integer : "))
s = 0
while(num>0):
    s = s + num%10
    num //=10
print(s)