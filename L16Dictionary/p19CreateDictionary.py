# Accept a sequence of words as input. Create a dictionary named real_dict whose keys are the letters of the English alphabet. For each key (letter), the corresponding value should be a list of words that begin with this key (letter). For any given key, the words should be appended to the corresponding list in the order in which they appear in the sequence. 
# You can assume that all words of the sequence will be in lower case.
# Input                                                                Expected Output
# Test Case1
# apple,and,oranges,are,only,fruits                                     a:apple,and,are
#                                                                       f:fruits
#                                                                       o:oranges,only
# Test Case2
# no,word,in,this,sentence,has,a,length,greater,than,ten                a:a
#                                                                       g:greater
#                                                                       h:has
#                                                                       i:in
#                                                                       l:length
#                                                                       n:no
#                                                                       s:sentence
#                                                                       t:this,than,ten
#                                                                       w:word

L = input("Enter words separated by comma : ").split(',')
real_dict = dict()

for word in L:
    start = word[0]
    if start not in real_dict:
        real_dict[start] = [ ]
    real_dict[start].append(word)
print(real_dict)