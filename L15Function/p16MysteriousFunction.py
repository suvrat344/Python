# A class of English words is called mysterious if it satisfies certain conditions. These conditions are hidden from you. 
# Instead, you are given a function named mysterious that accepts a word as argument and returns True if the word is mysterious and False otherwise.
# Write a function named type_of_sequence that accepts a list of words as an argument. Its return value is a string that depends on the number of mysterious words in the sequence. The exact conditions are given in the following table. If k denotes the number of mysterious words in the sequence, then:
#     k                                                                     Return value
# Less than 2                                                             mildly mysterious
# Greater than or equal to 2 but less than 5                              moderately mysterious
# Greater than or equal to 5                                              most mysterious
# Input                                                                Expected Output
# Test Case1
# ['attention', 'to', 'detail', 'everyone']                         moderately mysterious
# Test Case2
# ['almost', 'there', 'just', 'need', 'some', 'more', 'time']       mildly mysterious


def type_of_sequence(L):
    k = 0
    for i in range(len(L)):
        if(mysterious(L[i])):
            k +=1
    if(k<2):
        return "mildly mysterious"
    elif(k>=2 and k<5):
        return "moderately mysterious"
    else:
        return "most mysterious"
    
L = ['attention', 'to', 'detail', 'everyone'] 
print(type_of_sequence(L))