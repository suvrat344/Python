# You are given two non-empty text files file1 and file2 that have f1 and f2 lines respectively. Each file is a collection of ten-digit phone numbers, one number per line. It is also known that 0<f1≤f2.
# The following relations are defined on these two files:
# Subset: file1 is a subset of file2 if the phone number in the ith line of file1 is equal to the number in the ith line of file2, for 1≤i≤f and f1<f2.
# Equal: file1 is equal to file2 if the phone number in the ith line of file1 is equal to the number in the ith line of file2 for 1≤i≤f ,and f1=f2.
# Write a function named relation that accepts these two text files as arguments. It should return the string Subset if file1 is a subset of file2. It should return Equal if file1 is equal to file2. If both these conditions are not satisfied, it should return the string No Relation.
# (1) file1 and file2 are string variables that hold the names of the two files. For example, in the first test case, 
# it is file1 = 'public_1_1.txt' and file2 = 'public_1_2.txt'.
# Input                                       Expected Output
# Test Case1
# public_1_1.txt                                 Subset
# public_1_2.txt
# Test Case2
# public_2_1.txt                                 No Relation
# public_2_2.txt
# Test Case3
# public_3_1.txt                                 Equal
# public_3_2.txt

def relation(file1, file2):
    f1 = open(file1, 'r')
    L1 = f1.readlines()
    for i in range(len(L1)):
        L1[i] = L1[i].strip()
    f1.close()

    f2 = open(file2, 'r')
    L2 = f2.readlines()
    for i in range(len(L2)):
        L2[i] = L2[i].strip()    
    f2.close()

    if L1 == L2:
        return 'Equal'

    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return 'No Relation'
    return 'Subset'