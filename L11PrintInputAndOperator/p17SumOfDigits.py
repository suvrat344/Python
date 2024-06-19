# Accept a five digit number as input and print the sum of its digits as output.
# Test Case 1
# Input               Expected Output
# 12345                     15
# Test Case 2
# 67890                     30

n1 = int(input("Enter five digit number : "))
n2  = n1
r1 = n1 % 10
n1 = n1 // 10
r2 = n1 % 10
n1 = n1 // 10
r3 = n1 % 10
n1 = n1 // 10
r4 = n1 % 10
n1 = n1 // 10
r5 = r1 + r2 + r3 + r4 + n1
print(f"Sum of 5 digit number {n2} is {r5}.")