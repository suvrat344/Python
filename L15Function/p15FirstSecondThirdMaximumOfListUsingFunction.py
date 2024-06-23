# Write a function named first_three that accepts a list L of distinct integers as argument. It should return the first 
# maximum, second maximum and third maximum in the list, in this order. You can assume that the input list will have a 
# size of at least three.
# Input                      Expected Output
# Test Case1
# 1,2,3,4,5                     5,4,3
# Test Case2
# 10,-1,4,8,-10                10,8,4

def first_three(L):
    
    sorted_L = [ ]
    while L != [ ]:
        max_elem = L[0]
        for elem in L:
            if elem > max_elem:
                max_elem = elem
        L.remove(max_elem)
        sorted_L.append(max_elem)
    return sorted_L[0],sorted_L[1],sorted_L[2]
  

L = [1,2,3,4,5]
print(first_three(L))