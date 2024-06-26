# Two dictionaries D1 and D2 can be merged to create a new dictionary D that has the following structure:
# Each key-value pair in D is present either in D1 or D2.
# Each key in D1 is also a key in D. Likewise, each key in D2 is also a key in D.
# If a particular key is common to both D1 and D2, the value corresponding to this key in one of the two dictionaries is retained in D.
# Write a function named merge that accepts the following arguments:
# D1: first dictionary
# D2: second dictionary
# priority: The is a string variable that denotes the priority given to common keys while merging. That is, if both D1 and D2 have a key in common, then this variable will determine which value needs to be retained. More specifically, priority can take one of these two values:
# "first": retain the value corresponding to the common key present in the first dictionary
# "second": retain the value corresponding to the common key present in the second dictionary
# Input                             Expected Output
# Test Case1
# {1: 2, 2: 3, 3: 4}              {1: 2, 2: 3, 3: 4, 4: 15, 5: 10}            
# {1: 10, 4: 15, 5:10}
# first
# Test Case2
# {'a': 1, 'b': 2}                {'a': 10, 'b': 2, 'c': 3}
# {'a': 10, 'c': 3}
# second

def merge(D1, D2, priority):
    if priority == 'second':
        return merge(D2, D1, 'first')
    D = dict()
    for key in D1:
        value = D1[key]
        D[key] = value
    for key in D2:
        value = D2[key]
        if key not in D:
            D[key] = value
    return D

d1 = {1: 2, 2: 3, 3: 4}
d2 = {1: 10, 4: 15, 5:10}
print(merge(d1,d2,'first'))