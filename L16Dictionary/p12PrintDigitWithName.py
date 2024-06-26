# Accept a positive integer as input and print the digits present in it from left to right. Each digit should be printed as a lower case word on a separate line. How would you use dictionaries to solve this problem?
# Input                        Expected Output
# Test Case1
# 123                              one
#                                  two
#                                  three
# Test Case2
# 5440                             five
#                                  four
#                                  four
#                                  zero

n = input("Enter a positive number : ")
d  = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for i in n:
    if(int(i) in d):
        print(d[int(i)])