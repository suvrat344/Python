# Accept two positive integers x and y as input. Print the number of digits in x^y.
# Input                Expected Output
# Test Case1
# 3                          3
# 5
# Test Case 2
# 2                          4
# 10

x,y = int(input("Enter base : ")),int(input("Enter exponent : "))
print(f'Number of digits in {x}^{y} is {len(str(x**y))}')