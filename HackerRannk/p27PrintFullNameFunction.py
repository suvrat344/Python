# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the 
# following:
# Hello firstname lastname! You just delved into python.
# Function Description
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
# string first: the first name
# string last: the last name
# Prints
# string: 'Hello firstname lastname! You just delved into python' where firstname and lastname are replaced with first and last.

def print_full_name(first,last):
    print(f"Hello {first} {last}! You just delved into python.")
    
print_full_name("Ross","Taylor")