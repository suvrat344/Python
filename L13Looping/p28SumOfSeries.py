# Accept a positive integer n as input and print the sum of the first n terms of the series given below:
#                         1+(1+2)+(1+2+3)+(1+2+3+4)+⋯
# Just to be clear, the first term in the series is 1, the second term is (1+2) and so on.
# Input                           Expected Output
# Test Case1
# 3                                      10
# Test Case2
# 5                                      35

n = int(input("Enter number of term : "))
total = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        total = total + j
print(total)