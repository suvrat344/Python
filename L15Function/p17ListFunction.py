# Write the definition of the following five functions, all of which accept a list L as argument.
# (1) is_empty: return True if the list is empty, and False otherwise.
# (2) first: return the first element if the list is non-empty, return None otherwise.
# (3) last: return the last element if the list is non-empty, return None otherwise.
# (4) init: return the first n−1 elements if the list is non-empty and has size n, return None otherwise. Note that if L 
# 4 has just one element, init(L) should return the empty list.
# (5) rest: return the last n−1 elements if the list is non-empty and has size n, return None otherwise. Note that if L 
# has just one element, rest(L) should return the empty list.
# Input                             Expected Output
# Test Case1
# first([1, 2, 3])                         1
# Test Case2
# last([1, 2, 3, 4])                       4

def is_empty(L):
    if(len(L)>0):
        return False
    else:
        return True
def first(L):
    if(len(L)>0):
        return L[0]
    else:
        return None
        
def last(L):
    if(len(L)>0):
        return L[-1]
    else:
        return None
        
def init(L):
    if(len(L)>1):
        return L[:-1]
    else:
        return None
        
def rest(L):
    if(len(L)>1):
        return L[1:]
    else:
        return None
    
print(first([1,2,3]))