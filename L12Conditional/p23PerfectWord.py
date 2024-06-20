# A word is said to be perfect if it satisfies all the following criteria:
# (1) All the vowels (a,e,i,o,u) should be present in the word.
# (2) Let the vowels be represented as v1=a,v2=e,v3=i,v4=o,v5=u in lexical order.
# if i<j, then the first appearance of vi in the word should come before the first appearance of vj.
# If i<j, then the count of vi should be greater than or equal to the count of vj.
# Accept a word as input and do the following:
# (1) If it is a perfect word, print It is a perfect word
# (2) If the word is not a perfect word, print It is not a perfect word
# Input                             Expected Output
# Test Case1
# and                           It is not a perfect word
# Test Case2
# aeious                        It is a perfect word

word = input("Enter a word : ")
present = False
if('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
    if (word.index('a') < word.index('e') < word.index('i') < word.index('o') < word.index('u')):
        if(word.count('a') >= word.count('e') >= word.count('i') >= word.count('o') >= word.count('u')):
            present = True
if (present):
    print ('It is a perfect word')
else:
    print('It is not a perfect word')