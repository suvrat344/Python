# P is a dictionary of father-son relationships that has the following structure: for any key in the dictionary, its corresponding value is the father of key. As an example:
# P = {
#     'Jahangir': 'Akbar', 
#     'Akbar': 'Humayun', 
#     'Humayun': 'Babur'    
# }
# If 'Jahangir' is the key, then 'Akbar', his father, is the value. This is true of every key in the dictionary.
# Write a recursive function named ancestry that accepts the following arguments:
# P: dictionary of relationships
# present: name of a person, string
# past: name of a person, string
# It should return the sequence of ancestors of the person named present, traced all the way back up to person named past. 
# For example, ancestry(P, 'Jahangir', 'Babur') should return the list:
# L = ['Jahangir', 'Akbar', 'Humayun', 'Babur']
# In more Pythonic terms, L[i] is the father of L[i - 1], for 1≤i<len(L), with the condition that L[0] should be present 
# and L[-1] should be past.
# (1) You can assume that no two persons in the dictionary have the same name. However, a given person could either appear as a key or as a value in the dictionary.
# (2) A given person could appear multiple times as one of the values of the dictionary. For example, in test-case-2, 
# Prasanna has two sons, Mohan and Krishna, and hence appears twice (as a value).
# Input                                                                              Expected Output
# Test Case1
# {'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'}                   ['Jahangir', 'Akbar', 'Humayun', 'Babur']
# Jahangir
# Babur
# Test Case2
# {'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'}  ['Anil', 'Krishna', 'Prasanna']   
# Anil
# Prasanna

def ancestry(P, present, past):
    if present == past:
        return [past]
    return [present] + ancestry(P, P[present], past)

print(ancestry({'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'},'Jahangir','Babur'))
print(ancestry({'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'},'Anil','Prasanna'))