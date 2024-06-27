# Write a recursive function named count that accepts the following arguments:
# L: list of words
# word: a word, could be any string
# This function should return the number of occurrences of word in L.
# (1) You cannot use the built-in count method for lists in this problem.
# (2) All words will be in lower case.
# Input                                                         Expected Output
# Test Case1
# ['good', 'string', 'good', 'again', 'good']                       3
# good
# Test Case2
# ['a', 'small', 'big', 'a', 'the']                                 1
# small

def count(L, word):
    if len(L) == 0:
        return 0
    if L[-1] == word:
        return 1 + count(L[:-1], word)
    else:        
        return count(L[:-1], word)
    
print(count(['good', 'string', 'good', 'again', 'good'],'good'))
print(count(['a', 'small', 'big', 'a', 'the'],'small'))