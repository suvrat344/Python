# Write a recursive function named search that accepts the following arguments:
# (1) L: a sorted list of integers
# (2) k: integer
# The function should return True if k is found in the list L, and False otherwise.
# Input                                         Expected Output
# Test Case1
# [1, 2, 3, 4]                                      True
# 2
# Test Case2
# [10, 20, 30, 40, 50]                              False
# 15

def search(L, k):
    if len(L) == 0:
        return False
    left, right = 0, len(L) - 1
    mid = (left + right) // 2
    if L[mid] == k:
        return True
    if L[mid] < k:
        left, right = mid + 1, right
    elif L[mid] > k:
        left, right = left, mid - 1
    return search(L[left: right + 1], k)

print(search([1, 2, 3, 4],2))
print(search([10, 20, 30, 40, 50],15))