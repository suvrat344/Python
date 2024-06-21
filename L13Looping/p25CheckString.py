# Accept a string as input, print Integer if the string is an integer, print Float if it a float, else print None.
# Input                          Expected Output
# Test Case1
# 27.0                                Float
# Test Case2
# Ninety                              None

n = input("Enter a string : ")

chars = '0123456789.'

isstring = False

for i in n:
    if i not in chars:
        isstring = True

if not isstring:
    if '.' in n and n.count('.')==1:
        print('Float')     
    elif n.count('.')==0:
        print('Integer')
    else:
        print('None')
else:
    print('None')