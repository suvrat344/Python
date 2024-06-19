# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

s = "qA2"

isAlnum = False
isAlpha = False
isDigit = False
isLower = False
isUpper = False
for i in s:
    if(i.isalnum()):
        isAlnum = True
    if(i.isalpha()):
        isAlpha = True
    if(i.isdigit()):
        isDigit = True
    if(i.islower()):
        isLower = True
    if(i.isupper()):
        isUpper = True
print(isAlnum)
print(isAlpha)
print(isDigit)
print(isLower)
print(isUpper)