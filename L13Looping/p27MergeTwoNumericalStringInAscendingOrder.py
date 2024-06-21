# Consider two non-empty strings a and b of lengths n1 and n2 respectively, which contain only numbers as their 
# characters.Both the strings are in ascending order, that is a[i]≤a[j] for 0≤i<j<n.The same holds true for b. You need tomerge both the strings into one string of length n1+n2 such that all the characters of this combined string are also in ascending order.
# Accept a and b as input and print this merged string as output.
# Input                          Expected Output
# Test Case1
# 16789                           166677899
# 6679
# Test Case2
# 19                              149
# 4

a = input("Enter first string : ")
b = input("Enter second string : ")
n1 = len(a)
n2 = len(b)
n = n1 + n2
word = ''
while (n > 0):
    if len(a) == 0:
        word = word + b
        break
    elif len(b) == 0:
        word = word + a
        break
    else:
        if (a[0] == b[0]):
            word = word + a[0] * 2
            a = a[1:]
            b = b[1:]
            n -= 2
        elif a[0] > b[0]:
            word = word + b[0]
            b = b[1:]
            n -= 1
        else:
            word = word + a[0]
            a = a[1:]
            n -= 1
print(word)