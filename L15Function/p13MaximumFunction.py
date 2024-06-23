# Write a function maxval that accepts three integers a, b and c as arguments. It should return the maximum among the three numbers.
# Input                      Expected Output
# Test Case1
# 1,2,3                           3
# Test Case2
# 9,4,7                           9

def maxval(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(maxval(1,2,3))