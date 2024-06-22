# Accept a positive integer n as input and print the list of first n positive integers as output.
# Input                        Expected Output
# Test Case1
# 3                              [1, 2, 3]
# Test Case2
# 5                              [1, 2, 3, 4, 5]

n = int(input("Enter a positive integer : "))
l1 = []
for i in range(1,n+1):
    l1.append(i)
print(l1)