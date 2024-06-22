# You are given a sequence of n points, (xi,yi), 1≤i≤n, in the 2-D plane as input. Also, you are given a point P with coordinates (x,y). Print all points in the sequence that are nearest to P. If multiple points have the same least distance from P, print the points in the order of their appearance in the sequence.
# The first line of the input is an integer n, representing the number of points in the sequence. Each of the next n lines contains the co-ordinates of a point separated by comma. The last line contains the x and y co-ordinates of the point P. 
# Assume that all the x and y co-ordinates are integers.
# The distance between two points (x1,y1) and (x2,y2) is ((x1 − x2)**2+(y1−y2)**2)**0.5.You can assume that the maximum distance from P to any point will not exceed 1000.
# Input                                  Expected Output
# Test Case1
# 3                                           3,5
# 1,2
# 3,5
# 6,12
# 4,6
# Test Case2
# 2                                           3,4
# 3,4                                         1,2
# 1,2
# 2,3                                            

n = int(input("Enter number of coordinate you want to enter : "))
L = [ ]
for i in range(n):
    L.append(input("Enter coordinate separated by comma : "))

point = input("Enter coordiante of P for which u want to calculate minmum distance : ").split(',')
x = int(point[0])
y = int(point[1])

min_list = []
min_dist = 1000
for i in range(n):
    temp = L[i].split(',')
    temp_x = int(temp[0])
    temp_y = int(temp[1])
    dist = ((x - temp_x) ** 2 + (y - temp_y) ** 2) ** 0.5
    if (dist < min_dist):
        min_dist = dist
        min_list = [L[i]]
    elif dist == min_dist:
        min_list.append(L[i])
for point in min_list:
    print(point)