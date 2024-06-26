# Write the following functions:
# (1) is_key: accept a dictionary D and a variable key as arguments. Return True if the variable key is a key of the 
#     dictionary D, and False otherwise.
# (2) value: accept a dictionary D and a variable key as arguments. If the variable key is not a key of the dictionary D, 
#     return None, otherwise, return the value corresponding to this key.
# Input                                            Expected Output
# Test Case1
# is_key({'good': 4, 'day': 3}, 'good')                 True
# Test Case2
# value({'good': 4, 'day': 3}, 'day')                    3

def is_key(D, key):
    if(key in D):
        return True
    else:
        return False

def value(D, key):
    if(is_key(D,key)):
        return D[key]
    else:
        return None
    
print(is_key({'good': 4, 'day': 3}, 'good'))
print(value({'good': 4, 'day': 3}, 'day'))