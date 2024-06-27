# Write a recursive function named uniq that accepts a non-empty list L as argument and returns a new list after removing all duplicates from it. Your function must retain the last occurrence of each distinct element in the list.
# Input                                        Expected Output
# Test Case1
# [1, 2, 3, 2, 1, 4]                            [3, 2, 1, 4]
# Test Case2
# [10, 9, 6, 9, 10, 6, 10]                      [9, 6, 10]

def uniq(L):
    if len(L) == 1:
        return L
    if L[0] in L[1: ]:
        return uniq(L[1: ])
    else:
        return [L[0]] + uniq(L[1: ])
    
print(uniq([1, 2, 3, 2, 1, 4]))
print(uniq([10, 9, 6, 9, 10, 6, 10]))