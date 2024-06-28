# The scores of a class of students in the online degree program is represented as a CSV file with the following header:
# Name,Gender,CT,Python,PDSA
# The name of the file is given by the variable filename. The first line will be the header.
# Write a function named improvement which accepts the filename as argument. It should return the number of students whose scores have increased across the three courses. That is, the number of students whose scores are in this order: 
# CT < Python < PDSA.
# (1) filename is a string variable that holds the filename. For example, in the first test case, it is public_1.txt.
# Input                                           Expected Output
# Test Case1
# public_1.txt                                        3
# Test Case2
# public_2.txt                                        8

def improvement(filename):
    f = open(filename, 'r')
    f.readline()
    count = 0
    for line in f:
        name, gender, ct, python, pdsa = line.strip().split(',')
        ct, python, pdsa = int(ct), int(python), int(pdsa)
        if ct < python < pdsa:
            count += 1
    f.close()
    return count