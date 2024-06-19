# Accept two words as input and print the two words after adding a space between them.
# Input                           Expected Output
# Test Case1
# hello                             hello world
# world
# Test Case2
# good                              good job
# job

n1 = input("Enter first word : ")
n2 = input("Enter second word : ")
print(f'New word after joining {n1,n2} is {n1 + " " + n2}.')