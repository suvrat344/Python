# Accept a sequence of words as input, append all these words to a list in the order in which they are entered, and print this list as output. The first line in the input is a positive integer n that denotes the number of words in the sequence.The next n lines will have one word on each line.
# Input                             Expected Output
# Test Case1
# 4
# a                              ['a','list','of','words']
# list
# of
# words
# Test Case2
# 2
# smaller                        ['smaller', 'list']
# list

l1  = []
n = int(input("Enter no of words you want to enter in a list : "))
for i in range(n):
    word  = input("Enter word : ")
    l1.append(word)
print(l1)