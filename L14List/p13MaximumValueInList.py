# Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output.
# Hint
# When in doubt, always print the variables and examine the output.
# num = '1,2,3,4,5'
# L = num.split(',')
# Input                                   Expected Output
# Test Case1
# 1,2,3,4,5                                   5
# 10,30,20,50,40,5,10,20                      50

n = input("Enter comma separted integer : ").split(",")
print(max(n))