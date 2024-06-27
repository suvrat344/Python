# Write a recursive function named reverse that accepts a list L as argument and returns the reversed list.
# Input                                  Expected Output
# Test Case1
# [1, 2, 3, 4]                            [4, 3, 2, 1]
# Test Case2
# [10, 5, 1, 4, 9]                        [9, 4, 1, 5, 10]
# Test Case3
# ['a', 'b', 'c', 'd', 'e', 'f']          ['f', 'e', 'd', 'c', 'b', 'a']

def reverse(L):
    if len(L) <= 1:
        return L
    # Bring the last element to the front
    # And reverse the first n - 1 elements
    return [L[-1]] + reverse(L[:-1])

print(reverse([1, 2, 3, 4]))
print(reverse([10, 5, 1, 4, 9]))
print(reverse(['a', 'b', 'c', 'd', 'e', 'f']))