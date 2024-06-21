# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Function Description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# string string: a long string
# int max_width: the width to wrap to
# Returns
# string: a single string with newline characters ('\n') where the breaks should be
# Input Format
# The first line contains a string, string.
# The second line contains the width, maxwidth
# Sample Input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wrapper = textwrap.TextWrapper(width=4)
# word_list = wrapper.fill(text=string)      # Return in form of list
word_string = wrapper.fill(text=string)      # Return in form of string
print(word_string)