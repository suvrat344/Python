# Write a function insert that accepts a sorted list L of integers and an integer x as input. The function should return a sorted list with the element x inserted at the right place in the input list. The original list should not be disturbed in the process.
# (1) The only built-in methods you are allowed to use are append and remove. You should not use any other method provided for lists.
# Input                                   Expected Output
# Test Case1
# 1,2,3,5                                   1,2,3,4,5
# 4
# Test Case2
# 1,3,7,10,20                               1,3,7,8,10,20
# 8

def insert(L, x):
    out_L = [ ]         
    inserted = False    
    for elem in L:
        if (not inserted) and (elem > x):
            out_L.append(x)
            inserted = True
        out_L.append(elem)
    if (not inserted):
        out_L.append(x)
    return out_L

print(insert([1,2,3,5],4))