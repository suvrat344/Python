# Write a function named value_to_keys that accepts a dictionary D and a variable named value as arguments. It should return the list of all keys in the dictionary that have value equal to value. If the value is not present in the dictionary, the function should return the empty list.
# Input                                                             Expected Output
# Test Case1
# value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10)                    [1, 4]
# Test Case2
# value_to_keys({'good': 'boy', 'great': 'expectations'}, 'great')        []

def value_to_keys(D, value):
    res = []
    for i in D:
        if(value == D[i]):
            res.append(i)
    return res
print(value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10))
print(value_to_keys({'good': 'boy', 'great': 'expectations'}, 'great'))