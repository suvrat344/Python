# Consider a spiral of semicircles. We start at a point P0 on the x-axis with coordinates (l,0). The first arm of the spiral ends at P1 with coordinates (r,0). The second arm of the spiral starts at P1 and ends at the center of the first arm, P2.The third arm starts from P2 and ends at P3 which happens to be the center of the second arm. And finally, the fourth arm starts at P3 and ends at P4, the center of the third arm.

# Write two functions named spiral_iterative and spiral_recursive, each of which accepts three arguments:
# left: x-coordinate of the point P0
# right: x-coordinate of the point P1
# n: the number of arms in the spiral
# Both functions should return the the x-coordinate of Pn, the point at which the nth arm of the spiral ends.
# Input                             Expected Output
# Test Case1
# spiral_recursive
# 0,1,4                                 0.625
# Test Case2
# spiral_iterative
# 0,1,100                               0.667

def spiral_recursive(left, right, n):
    if n == 0:
        return left
    if n == 1:
        return right
    return (spiral_recursive(left, right, n - 1) +
            spiral_recursive(left, right, n - 2)) / 2
    

def spiral_iterative(left, right, n):
    if n == 0:
        return left
    if n == 1:
        return right
    c = 0
    for i in range(n - 1):
        left, right = right, (left + right) / 2
    return right

print(spiral_recursive(0,1,4))
print(spiral_iterative(0,1,100))