# Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
# Input                 Expected Output
# Test Case1
# 1,2,3,4,5                 120
# Test Case2
# 6,7,8,9,0                  0

num = input("Enter five number separated by commas : ")
d1 = int(num[0])
d2 = int(num[2])
d3 = int(num[4])
d4 = int(num[6])
d5 = int(num[8])
dprod = d1 * d2 * d3 * d4 * d5
print(f"Product of 5 single digit number {d1,d2,d3,d4,d5} is {dprod}.")