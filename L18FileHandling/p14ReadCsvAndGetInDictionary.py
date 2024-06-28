# filename points to a CSV file that has two columns. The first column is the name of a student, the second column is this student's age. The first line of the file will always be the header. A sample file is given below for your reference:
# Name,Age
# Arti,20
# Kalam,60
# Atul,25
# Krishnan,24
# Sahana,20
# Write a function named get_dict that accepts the filename as argument and returns a dictionary where the keys are the student names and the values are the corresponding ages of the students.
# (1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.
# Input                       Expected Output
# Test Case1
# public_1.txt                  Archana:49
#                               Dhawan:39
#                               Ganguly:34
#                               Kohli:23
#                               Manohar:41
#                               Meerabai:54
#                               Sachin:27
#                               Saina:36
#                               Sania:25
#                               Shifali:33
# Test Case2
# public_2.txt                     Archana:32
#                                  Dhawan:48
#                                  Ganguly:37
#                                  Kohli:34
#                                  Manohar:30
#                                  Meerabai:49
#                                  Sachin:39
#                                  Saina:27
#                                  Sania:48
#                                  Shifali:21

def get_dict(filename):
    d = {}
    with open(filename,"r") as f:
        x = f.readlines()
        line = 0
        for i in x:
            line = line + 1
            y = i.split(",")
            if(y[0] not in d and y[0]!="Name" and len(x)!=line):
                d[y[0]] = int(y[1][:-1])
            elif(y[0]!="Name" and len(x)==line):
                d[y[0]] = int(y[1])
    return d