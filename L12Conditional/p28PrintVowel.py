# Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output. Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.
# Input                                                                               Expected Output
# Test Case1
# Moon flowers bloom only at night, closing during the day.                                  aeiou
# Test Case2
# 1 YARD (yd) = 3 FEET (ft).                                                                 ae

input_string = input("Enter a string : ").lower()
vowels = ""
if "a" in input_string:
    vowels += "a"
if "e" in input_string:
    vowels += "e"
if "i" in input_string:
    vowels += "i"
if "o" in input_string:
    vowels += "o"
if "u" in input_string:
    vowels += "u"
# check if vowels is non-empty
if vowels != "":
    print(vowels)
else:
    print('none')