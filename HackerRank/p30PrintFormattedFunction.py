# Given an integer, n, print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
#     int number: the maximum value to print
# Prints
# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should 
# be space-padded to match the width of the binary value of number and the values should be separated by a single space.

def print_formatted(number):
    width = len(bin(number)[2:])
    print(width)
    for i in range(1,number+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
    
print_formatted(17)