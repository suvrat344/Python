# Accept a point in 2D space as input and find the region in space that this point belongs to. A point could belong to one of the four quadrants, or it could be on one of the two axes, or it could be the origin. The input is given in 2 lines: 
# the first line is the x-coordinate of the point while the second line is its y-coordinate. The possible outputs are first,second, third, fourth, x-axis, y-axis, and origin. Any other output will not be accepted. Note that all outputs should be in lower case.
# Input               Expected Output
# Test Case1
# 1
# 2                     first
# Test Case2
# 1.8
# -1                    fourth


x = float(input("Enter x-coordinate : "))
y = float(input("Enter y-coordinate : "))
if(x==0 and y==0):
    print("origin")
elif(x>0 and y>0):
    print("first")
elif(x<0 and y>0):
    print("second")
elif(x<0 and y<0):
    print("third")
elif(x>0 and y<0):
    print("fourth")
elif(x==0 and (y>0 or y<0)):
    print("y-axis")
elif(y==0 and (x>0 or x<0)):
    print("x-axis")
else:
    print("any other output will not be accepted.")