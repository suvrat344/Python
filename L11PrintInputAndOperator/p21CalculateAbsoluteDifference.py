# Accept two integers a and b as input and print the absolute difference of both the numbers. For example, if a=9,b=8,then the absolute difference is 9−8=1.So,your output should be 1.
# Input       Expected Output
# Test Case1
# 9,10               1
# Test Case2
# 100,10             90

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
square = (b - a) ** 2
root = square ** 0.5
diff = int(root)
print(f"Absolute difference between {a,b} is {diff}.")