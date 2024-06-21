# Accept a positive integer n as input and print a triangle of zeros for n lines. The ith line should have i zeros. There shouldn't be any spaces between consecutive zeros. Do not print a space at the end of a line.
# Input                   Expected Output
# Test Case1
# 4                           0
#                             00
#                             000
#                             0000
# Test Case2
# 6                           0
#                             00
#                             000
#                             0000
#                             00000
#                             000000

n = int(input("Enter a positive integer : "))
for i in range(1,n+1):
    print("0"*i)