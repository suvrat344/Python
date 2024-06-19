# The following expression is called a continued fraction:
# x + 1 / (x + 1 / (x + 1 / x + 1 / x + 1 / x + 1 / ))


# Accept a positive integer x as input, compute the value of this continued fraction and store the result in a variable 
# named cfrac. We will round off your answer to exactly two decimal places.
# Input             Expected Output
# Test Case1
# 2                      2.41
# Test Case2
# 3                      3.30

x = int(input("Enter a number : "))
l0 = x + 1 / x
l1 = x + 1 / l0
l2 = x + 1 / l1
l3 = x + 1 / l2
cfrac  = x + 1 / l3
print(f"Value of above fraction at {x} is {round(cfrac,2)}")