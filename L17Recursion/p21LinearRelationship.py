# Write a recursive function named linear that accepts the following arguments:
# P: a non-empty list of positive integers
# Q: a non-empty list of positive integers
# k: a positive integer
# It should return True only if both the conditions given below are satisfied:
# P and Q are of same length.
# P[i]=k⋅Q[i], for every integer [0,len(P)−1], endpoints inclusive.
# Input                                Expected Output
# Test Case1
# [2, 4, 6, 8]                             True
# [1, 2, 3, 4]
# 2
# Test Case2
# [10, 20, 30, 40, 50]                     False
# [1, 2, 3, 4, 6]
# 10

def linear(P, Q, k):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] / Q[0] != k:
        return False
    return linear(P[1: ], Q[1: ], k)

print(linear([2, 4, 6, 8],[1, 2, 3, 4],2))
print(linear([10, 20, 30, 40, 50],[1, 2, 3, 4, 6],10))