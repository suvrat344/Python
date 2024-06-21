# Accept a positive integer n as input and print all the factors of n, one number on each line.
# Input                 Expected Output
# Test Case1
# 10                       1
#                          2
#                          5
#                          10
# Test Case2
# 18                       1
#                          2
#                          3
#                          6
#                          9
#                          18

n = int(input("Enter a number : "))
for i in range(1,n+1):
    if(n%i==0):
        print(i)