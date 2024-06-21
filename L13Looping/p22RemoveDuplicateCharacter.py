# Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. Print this new string as output. You can assume that all input strings will be in lower case.
# Input                         Expected Output
# Test Case1
# aeiou                      
# this is a python program      ths s  pythn prgrm
# Test Case2
# lo
# hello python                  he pythn

string1 = input("Enter first string : ")
string2 = input("Enter second string : ")
temp = ''   # there is no space between the quotes
for i in range(0, len(string1)):
    for j in range(0, len(string2)):
        if (string1[i] == string2[j]):
            continue
        else:
            temp = temp + string2[j]
    string2 , temp = temp , ''
print(string2)