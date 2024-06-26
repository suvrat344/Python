# Accept a sequence of words as input. Create a dictionary named freq whose keys are the distinct words in the sequence. 
# The value corresponding to a key (word) should be the frequency of occurrence of the key (word) in the sequence.
# Input                                                              Expected Output
# Test Case1
# one,four,one,six,five,one,four,two,nine,one                             five:1
#                                                                         four:2
#                                                                         nine:1
#                                                                          one:4
#                                                                          six:1
#                                                                          two:1
# Test Case2
# word,words,many,words,some,words,all,words                               all:1
#                                                                          many:1
#                                                                          some:1
#                                                                          word:1
#                                                                          words:4
# (1) You can assume that all words will be in lower case.

st1 = input("Enter comma separated value : ").split(",")
freq  = {}
for i in st1:
    if(i in freq):
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
print(freq)