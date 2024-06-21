# Accept a phone number as input. A valid phone number should satisfy the following constraints.
# (1) The number should start with one of these digits: 6, 7, 8, 9
# (2) The number should be exactly 10 digits long.
# (3) No digit should appear more than 7 times in the number.
# (4) No digit should appear more than 5 times in a row in the number.
# If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.
# Print the string valid if the phone number is valid. If not, print the string invalid.
# Input                                       Expected Output
# Test Case1
# 9852546666                                      valid
# Test Case2
# 9888886754                                      valid
# Test Case3
# 9888888765                                      invalid

number = input("Enter a phone number : ")
# we start with the assumption that the number is valid
valid = True

if len(number) == 10 and number[0] in '6789':
    for digit_index in range(0, 5):
        count = number.count(number[digit_index])
        if count > 7:
            valid = False
            break
        if 6 * number[digit_index] in number: 
            valid = False
            break
else:
    valid = False
if valid:
    print('valid')
else:
    print('invalid')