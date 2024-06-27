# Write a recursive function named multiply accepts two positive integers a and b as argument and returns their product. 
# You can only use + and − operators. You are not allowed to use the ∗ symbol anywhere in your code!
# Input                               Expected Output
# Test Case1
# 2                                          6
# 3
# Test Case2
# 5                                          20
# 4

def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b - 1)

print(multiply(2,3))
print(multiply(5,4))