# Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string 
# to the console. You can assume that the string will only contain letters.
# Input                                  Expected Output
# Test Case1
# Bharatanatyam                           aaaaabhmnrtty
# Test Case2
# montypython                             hmnnoopttyy

text = input("Enter a string : ").lower()
length = len(text)
output_string = '' 
for char in 'abcdefghijklmnopqrstuvwxyz':
    for i in range(0, length):
        if char == text[i]:
            output_string += char
print(output_string)