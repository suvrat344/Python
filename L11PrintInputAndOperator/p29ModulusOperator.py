# Accept two positive integers M and N as input. There are two cases to consider:
# (1) If M < N, then print M as output.
# (2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N, then subtract N from M1 and call the difference M2.
# Keep doing this operation until you reach a value k, such that, Mk < N. You have to print the value of Mk as output. 
# Input                 Expected Output
# Test Case1
# 5                         1
# 2
# Test Case2
# 5                         5
# 10

m = int(input("Enter first number : "))
n = int(input("Enter second number : "))
print(f"Remainder of {m,n} is {m%n}")