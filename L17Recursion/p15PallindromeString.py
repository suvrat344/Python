# Write a recursive function named palindrome that accepts a string word as argument and returns True if it is a palindrome and False otherwise.
# Input                             Expected Output
# Test Case1
# mom                                   True
# Test Case2
# random                                False

def palindrome(word):
    if(len(word)==0):
        return True
    else:
        return (word[0]==word[-1]) and palindrome(word[1:-1])
    
print(palindrome('mom'))
print(palindrome('random'))