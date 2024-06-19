# You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a 
# substring in the given string. Create a new string by replicating the substring a minimum number of times so that the 
# resulting string is longer than the input string.The input parameters are the string, start index of the substring and
# the end index of substring (endpoints inclusive) each on a different line.
# Input                 Expected Output
# Test Case1
# python                   ppppppp
# 0
# 0
# Test Case2
# mathematics              atheatheathe
# 1
# 4

word  = input("Enter word : ")
start = int(input("Enter start index : "))
end = int(input("Enter end index : "))
x = len(word) // (end - start + 1)
print(f"New substring formed after transformation is {word[start:end+1] * (x+1)}.")