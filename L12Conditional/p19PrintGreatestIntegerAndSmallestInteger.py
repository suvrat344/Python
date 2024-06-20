# Accept a real number x as input and print the greatest integer less than or equal to x on the first line, followed by the
# smallest integer greater than or equal to x on the second line.
# Input                Expected Output
# Test Case1
# 1.3                          1
#                              2
# Test Case2
# 5.8                          5
#                              6
x = float(input("Enter a number : "))
if(x>0):
    floor = int(x)
    if(floor==x):
        ceil = floor
    else:
        ceil = floor + 1
elif(x<0):
    ceil = int(x)
    if(ceil == x):
        floor = ceil
    else:
        floor = ceil - 1

print(floor)
print(ceil)