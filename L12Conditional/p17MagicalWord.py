# A sequence of five words is called magical if the ith  word is a substring of the (i+1)th word for every i in the range 
# 1<=i<5.Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and
# non-magical otherwise.
# Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.
# Input                    Expected Output
# Test Case1
# a
# ab
# abc                         magical
# abcd
# abcde
# Test Case2
# a
# ab
# acdb                        non-magical
# efghi
# abcdefghi

word1 = input("Enter first word : ")
word2 = input("Enter second word : ")
word3 = input("Enter third word : ")
word4 = input("Enter fourth word : ")
word5 = input("Enter fifth word : ")

if(word1 in word2 and word2 in word3 and word3 in word4 and word4 in word5):
    print("magical")
else:
    print("non-magical")