# The range of a list of numbers is the difference between the maximum and minimum values in the list.
# Write a function named get_range that accepts a list of real numbers as argument. It should return the range of the list.
# Note
# (1) Avoid using built-in function such as max and min.
# Input                                          Expected Output
# Test Case1
# Actual Output
# 1.0,2.0,3.0,4.0,5.0                                4.0
# Test Case2
# 1.0,3.7,8.9,5.5,1.9,6.3,0.1,9.9                    9.8

def get_max(L):
    maxi = L[0]
    for x in L:
        if x > maxi:
            maxi = x
    return maxi

def get_min(L):
    mini = L[0]
    for x in L:
        if x < mini:
            mini = x
    return mini

def get_range(L):
    maxi = get_max(L)
    mini = get_min(L)
    return maxi - mini 

print(get_range([1.0,2.0,3.0,4.0,5.0]))