# A list L of words is already given to you as a part of the prefix code. Print the longest word in the list. If there are multiple words with the same maximum length, print the one which appears at the rightmost end of the list
# Input                                     Expected Output
# Test Case1
# this,sentence,is,quite,long                 sentence
# Test Case2
# this,is,a,good,word                         word

L = input("Enter word separated by comma : ").split(',')
max = len(L[0])
for i in range(1,len(L)):
    if(len(L[i])>=max):
        max = len(L[i])
        s = L[i]
print(s)