# In the first line of input, accept a sequence of space-separated words. In the second line of input, accept a single word.If this word is not present in the sequence, print NO. If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.
# Input                                                                        Expected Output
# Test Case1
# a good collection of words                                                         NO
# the
# Test Case2
# no sentence can begin with because because because is a conjunction                YES
# because                                                                             3  

words = input("Enter space separated word : ").split(' ')
test = input("Enter word to be search : ")

if test not in words:
    print('NO')
else:
    print('YES')
    count = 0
    for word in words:
        if test == word:
            count += 1            
    print(count)