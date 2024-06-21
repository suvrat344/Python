# Accept a sequence of words as input and print the the shortest word in the sequence. The input will have n+1 lines, where n denotes the number of terms in the sequence. The ith line in the input will contain the ith word in the sequence for 1≤i≤n.The last line of the input will always be the string abcdefghijklmnopqrstuvwxyz. This string is not a part of the sequence. You can assume that each test case corresponds to a non-empty sequence of words. If there are multiple words that have the same minimum length, print the first such occurrence.
# Input                               Expected Output
# Test Case1
# one
# two                                     one
# three
# abcdefghijklmnopqrstuvwxyz
# Test Case2
# long
# short                                   the
# the
# abcdefghijklmnopqrstuvwxyz

length = 100
while(True):
    n = input("Enter a word : ")
    if(len(n)<length):
        length = len(n)
        word = n
    elif(n=="abcdefghijklmnopqrstuvwxyz"):
        break
print(word)