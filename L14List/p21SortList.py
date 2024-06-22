# L is a list of real numbers that is already given to you. You have to sort this list in descending order and store the 
# sorted list in a variable called sorted_L.
# Input                           Expected Output
# Test Case1
# 1.1,2.2,3.3                     [3.3, 2.2, 1.1]
# Test Case2
# 3,1,2,4.5                       [4.5, 3, 2, 1]

def solution(L):
    sorted_L = [ ]
    while L != [ ]:
        max_elem = L[0]
        for elem in L:
            if elem > max_elem:
                max_elem = elem
        L.remove(max_elem)
        sorted_L.append(max_elem)
                
    return sorted_L
  
print(solution([1.1,2.2,3.3]))