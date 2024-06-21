# Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.
# Input                       Expected Output
# Test Case1
# kayak                        PALINDROME
# Test Case2
# random                       NOT PALINDROME

word = input("Enter string : ")

reverse = ''
for char in word:
    reverse = char + reverse

if reverse == word:
    print('PALINDROME')
else:
    print('NOT PALINDROME')