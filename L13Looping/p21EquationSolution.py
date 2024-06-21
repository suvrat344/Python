# Accept a positive integer n as input and find all solutions to the equation:
#                        x**2 + y**2 = z**2
# subject to the following constraints:
# (1) x, y and z are positive integers
# (2) x<y<z<n
# Print each solution triplet on one line — x,y,z — with a comma between consecutive integers. The triplets should be printed in ascending order. If you do not find any solutions satisfying the given constraints, print the string NO SOLUTION as output.
# Order relation among triplets
# Given two triplets T1 = (x1,y1,z1) and T2 = (x2,y2,z2), use the following process to compare them:
# (1) If x1 < x2, then T1 < T2
# (2) If x1 = x2 and y1 < y2, then T1 < T2
# (3) If x1 = x2, y1 = y2, and z1 < z2, then T1 < T2
# Input                         Expected Output
# Test Case1
# 15                               3,4,5
#                                  5,12,13
#                                  6,8,10
# Test Case2
# 20                               3,4,5
#                                  5,12,13
#                                  6,8,10
#                                  8,15,17
#                                  9,12,15

n = int(input("Enter a positive integer : "))
flag = False
for i in range(1,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(i**2 + j**2 == k**2):
                print(f"{i},{j},{k}")
                flag = True
                
if(flag==False):
    print("NO SOLUTION")