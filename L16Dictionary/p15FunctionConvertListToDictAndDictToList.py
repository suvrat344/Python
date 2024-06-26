# Write the following functions:
# (1) dict_to_list: accept a dictionary D as argument. Return the key-value pairs in D as a list L of tuples. That is, every element of L should be of the form (key, value) such that D[key] = value. Going the other way, every key-value pair in the dictionary should be present as a tuple in the list L.
# (2) list_to_dict: accept a list of tuples L as argument. Each element of L is of the form (x, y). Return a dict D such that each tuple (x, y) corresponds to a key-value pair in D. That is, D[x] = y.
# (1) For the function dict_to_list(D), the order in which the key-value pairs are appended to the list doesn't matter.
# (2) For the function list_to_dict(L), you can assume that if (x1, y1) and (x2, y2) are two different elements in L, x1 != x2. Why is this assumption important?
# Input                                                            Expected Output
# Test Case1
# dict_to_list({'abc': 3, 'def': 10})                            [('abc', 3), ('def', 10)]
# Test Case2
# list_to_dict([('def', 10), ('abc', 3)])                        {'abc': 3, 'def': 10}

def dict_to_list(D):
    res = []
    for i in D:
        res.append((i,D[i]))
    return res

def list_to_dict(L):
    d1 = {}
    for i in L:
        if(i[0] not in d1):
            d1[i[0]] = i[1]
    return d1

print(dict_to_list({'abc': 3, 'def': 10}))
print(list_to_dict([('def', 10), ('abc', 3)]))