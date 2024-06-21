# Accept a positive integer n as input and print the first n positive integers, one number on each line.
# Input                          Expected Output
# Test Case1
# 3                                  1
#                                    2
#                                    3
# Test Case2
# 5                                  1
#                                    2
#                                    3
#                                    4
#                                    5

n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(i)