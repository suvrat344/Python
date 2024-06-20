# Write a program to realize the equation of a line given 2 points (x1,y1) and (x2,y2) in 2D space. The input is in 5 lines where, the first, second, third, and fourth lines represent x1,y1,x2,y2 respectively.The fifth line corresponds to x3.Determine y3 using the equation of a straight line as given below:
#     (x-x1)/(x2-x1)=(y-y1)/(y2-y1)
# The output should be "Vertical Line" if the line is vertical. In other cases, the output should be 2 lined, where the first line is the value of y3 and the second line indicates whether the slope of the line is positive, negative or zero.
# Print "Positive Slope", "Negative Slope" or "Horizontal Line" accordingly.
# Note that all inputs are to be processed as real numbers.
# Input                      Expected Output
# Test Case1
# 1
# 2
# 1                          Vertical Line
# 6
# 5
# Test Case2
# 1
# 4                              4.5
# 5                          Positive Slope
# 6
# 2

x1  = eval(input("Enter x-cordinate of P : "))
y1 = eval(input("Enter y-cordinate of P : "))
x2 = eval(input("Enter x-cordinate of Q : "))
y2 = eval(input("Enter y-cordinate of Q : "))
x3  = eval(input("Enter x-cordinate of R : "))
if(x2-x1==0):
    print("Vertical Line")
else:
    m = (y2-y1)/(x2-x1)
    y3 = (x3-x1)*(y2-y1)/(x2-x1) + y1
    if(m>0):
        print(y3)
        print("Positive Slope")
    elif(m<0):
        print(y3)
        print("Negative Slope")
    elif(m==0):
        print(y3)
        print("Horizontal Line")