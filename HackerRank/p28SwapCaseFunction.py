# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and 
# vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description
# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
#    string s: the string to modify
# Returns
#    string: the modified string


def swap_case(s):
    return s.swapcase()

print(swap_case("Pythonist 2"))