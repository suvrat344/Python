# Consider the piece-wise function given below.
#             x+2                 0<x<10
# f(x) =   x**2 + 2               10≤x
#             2                   otherwise
# Accept the value of x as input and print the value of f(x) as output. Note that both the input and output are real 
# numbers.Your code should reflect this aspect. That is, both x and f(x) should be float values.
# Input               Expected Output
# Test Case1
# 5.0                     7.0
# Test Case2
# 15.0                   227.0


x = float(input("Enter a number : "))
if(x>0 and x<10):
    print(float(x+2))
elif(x>=10):
    print(float(x**2 + 2))   
else:
    print(float(0))