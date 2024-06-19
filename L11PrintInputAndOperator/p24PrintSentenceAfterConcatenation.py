# Accept five words as input and print the sentence formed by these words after adding a space between consecutive words 
# and a full stop at the end.
# Input                 Expected Output
# Test Case1
# this                this is a good idea.
# is
# a
# good
# idea
# Test Case2
# one                 one and two are numbers.
# and
# two
# are
# numbers

word1 = input("Enter first word : ")
word2 = input("Enter second word : ")
word3 = input("Enter third word : ")
word4 = input("Enter fourth word : ")
word5 = input("Enter fifth word : ")
space = ' '
stop = '.'
sentence = word1 + space + word2 + space + word3 + space + word4 + space + word5 + stop
print(f"Sentence formed after combining {word1,word2,word3,word4,word5} is {sentence}")