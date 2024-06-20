# EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer. On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table:

# The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied.
# The sum of the employee-ids of every pair of adjacent employees at the table must be an even number.
# They are so lazy that they won't move around to satisfy the above condition. If the current seating plan doesn't satisfy 
# the condition, the meeting will be canceled. You are given the employee-id of all five employees. Your task is to decide 
# if the meeting happened or not.
# The input will be five lined, each line containing an integer. The ith line will have the employee-id of Ei. The output 
# will be a single line containing one of these two strings: YES or NO.
# Input              Expected Output
# Test Case1
# 1
# 2
# 3                       NO
# 4
# 5
# Test Case2
# 2
# 4
# 6                       YES
# 8
# 10

e1 = int(input("Enter emp-id of first employee : "))
e2 = int(input("Enter emp-id of second employee : "))
e3 = int(input("Enter emp-id of third employee : "))
e4 = int(input("Enter emp-id of fourth employee : "))
e5 = int(input("Enter emp-id of fifth employee : "))
# Check if the sum is odd for each pair of adjacent employees
if (e1 + e2) % 2 != 0:
    print('NO')
elif (e2 + e3) % 2 != 0:
    print('NO')
elif (e3 + e4) % 2 != 0:
    print('NO')
elif (e4 + e5) % 2 != 0:
    print('NO')
elif (e5 + e1) % 2 != 0:
    print('NO')
# If the sum is even for every pair of adjacent employees,then the else block gets executed
else:
    print('YES')