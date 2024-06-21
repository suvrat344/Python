# Accept a sequence of positive integers as input and print the the maximum number in the sequence. The input will have n+1 lines, where n denotes the number of terms in the sequence. The ith line in the input will contain the ith term in the sequence for 1≤i≤n. The last line of the input will always be the number 0. Each test case will have at least one term in the sequence
# Input             Expected Output
# Test Case1
# 1
# 2                     3
# 3
# 0
# Test Case2
# 3
# 2                      10
# 10
# 0

max = 0
while(True):
    n = int(input("Enter a positive integer : "))
    if(n>max):
        max = n
    elif(n==0):
        break
print(max)