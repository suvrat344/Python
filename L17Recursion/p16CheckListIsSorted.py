# Write a recursive function named non_decreasing that accepts a non-empty list L of integers as argument and returns True if the elements are sorted in non-decreasing order from left to right, and False otherwise.
# Input                                              Expected Output
# Test Case1
# [1, 10, 100, 1000]                                       True
# Test Case2
# [10, 1, 100, 1000, 10000]                                False
# Test Case3
# [1, 1, 2, 3, 3, 5]                                       True

def non_decreasing(L):
    if len(L) <= 1:
        return True
    if L[-2] > L[-1]:
        return False
    return non_decreasing(L[:-1])

print(non_decreasing([1, 10, 100, 1000]))
print(non_decreasing([10, 1, 100, 1000, 10000]))
print(non_decreasing([1, 1, 2, 3, 3, 5]))