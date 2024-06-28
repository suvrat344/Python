# The scores of a class of students in the online degree program is represented as a CSV file with the following header:
# SeqNo,Name,Gender,CT,Python,PDSA
# The name of the file is given by the variable filename. The first line will be the header. The contents of the file will be in increasing order of sequence numbers.
# Write a function named extract_lines that accepts filename as argument. Within the function, read the file and look for all male students who have scored at least 70 marks in Python. Copy these lines into a new file named python.csv. The entries in this file should be in the increasing order of sequence numbers. Also, the first line of python.csv should be the header, which is same as the one in filename.
# (1) filename is a string variable that holds the filename. For example, in the first test case, it is public_1.csv.
# Input                                     Expected Output
# Test Case1
# public_1.csv                         SeqNo,Name,Gender,CT,Python,PDSA
#                                         38,Harshad,M,70,99,74
#                                         22,Harish,M,43,88,57
#                                         25,Aditya,M,78,96,54
#                                         12,Omkar,M,43,92,46
#                                         31,Tanmoy,M,47,70,52
# Test Case2
# public_2.csv                         SeqNo,Name,Gender,CT,Python,PDSA
#                                         41,Bishen,M,41,93,84
#                                         28,Karthik,M,100,94,59
#                                         36,Anirban,M,78,73,53
#                                         43,Danny,M,73,82,85
#                                         12,Deepak,M,85,83,44

def extract_lines(filename):
    f = open(filename, 'r')
    header = f.readline()
    g = open('python.csv', 'w')
    g.write(header)
    for line in f:
        L = line.strip().split(',')
        python = int(L[4])
        gender = L[2]
        if gender == 'M' and python >= 70:
            g.write(line)
    f.close()
    g.close()