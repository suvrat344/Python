# Accept a space-separated sequence of positive real numbers as input. Convert each element of the sequence into the 
# greatest integer less than or equal to it. Print this sequence of integers as output, with a comma between consecutive 
# integers.
# Input                                     Expected Output
# Test Case1
# 1.2 3.9 4.2 10.0                             1,3,4,10
# Test Case2
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7                  1,2,3,4,5,6,7

n = input("Enter positive real number separated by space : ").split(" ")
for i in n:
    if(i==n[-1]):
        print(int(float(i)))
    else:
        print(int(float(i)),end=",")