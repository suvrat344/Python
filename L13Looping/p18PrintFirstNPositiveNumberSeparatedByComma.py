# Accept a positive integer n as input and print the first n integers on a line separated by a comma.
# Input                    Expected Output
# Test Case1
# 5                          1,2,3,4,5
# Test Case2
# 10                         1,2,3,4,5,6,7,8,9,10

n = int(input("Enter a positive integer : "))
for i in range(1,n+1):
    if(i<n):
        print(i,end=',')
    else:
        print(i,end='')