# Accept three positive integers as input and check if they form the sides of a right triangle. Print YES if they form one,and NO if they do not. The input will have three lines, with one integer on each line. The output should be a single line containing one of these two strings: YES or NO.
# Input                    Expected Output
# Test Case1
# 1
# 2                              NO
# 3
# Test Case2
# 3
# 4                              YES
# 5

x = int(input("Enter length of first side of the triangle : "))
y = int(input("Enter length of second side of the triangle : "))
z = int(input("Enter length of third side of the triangle : "))

if ((x ** 2 + y ** 2 == z ** 2) or (y ** 2 + z ** 2 == x ** 2) or (z ** 2 + x ** 2 == y ** 2)):
  print('YES')
else:
  print('NO')