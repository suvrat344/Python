# Two integers are co-prime if the only common divisor between the two integers is one.
# Accept two positive integers as input in two different lines. Print Coprime if the two integers are co-prime, else print Not Coprime. Assume that both the integers are greater than two.
# Input                               Expected Output
# Test Case1
# 16
# 6                                     Not Coprime
# Test Case2
# 19
# 4                                     Coprime

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
coprime = True
for i in range(2, num1):
    if(num1 % i == 0):
        if(num2 % i == 0):
            coprime = False
            break
if(coprime):
    print('Coprime')
else:
    print ('Not Coprime')