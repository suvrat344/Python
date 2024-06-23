# The distance between two letters in the English alphabet is one more than the number of letters between them. 
# Alternatively, it can be defined as the number of steps needed to move from the alphabetically smaller letter to the 
# larger letter. This is always a non-negative integer. For example:
# Letter-1                 Letter-2                     Letter-Distance
#   a                         a                               0
#   a                         c                               2
#   a                         z                               25
#   z                         a                               25
#   e                         a                               4
# The distance between two words is defined as follows:
# It is -1, if the words are of unequal lengths.
# If the word-lengths are equal, it is the sum of the distances between letters at corresponding positions in the words. 
# For example:dword(dog,cat)=dletter(d,c)+dletter(o,a)+dletter(g,t)=1+14+13=28
# Write a function named distance that accepts two words as arguments and returns the distance between them.
# Input                               Expected Output
# Test Case1
# dog                                     28
# cat
# Test Case2
# greet                                    4
# great

def distance(word_1, word_2):
    if len(word_1) != len(word_2):
        return -1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    size = len(word_1)
    dist = 0
    for i in range(size):
        c1, c2 = word_1[i], word_2[i]
        d = abs(letters.index(c1) - letters.index(c2))
        dist += d
    return dist

print(distance('dog','cat'))