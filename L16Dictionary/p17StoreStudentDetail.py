# Accept a positive integer n that represents the number of students in the class n blocks of input follow. Each block ismade up of six lines and contains the details of one student in the class. Create a dictionary corresponding to each student. All keys should be strings. The type of the value corresponding to a key and the order in which the inputs should be accepted are shown in the table given below.
# Line number                  Key                      Type of Value
# 1                            Name                       String
# 2                            City                       String
# 3                            SeqNo                      Integer
# 4                            Mathematics                Integer
# 5                            Physics                    Integer
# 6                            Chemistry                  Integer
# Append each dictionary to a list named scores_dataset. This is the list that we will finally use for evaluating your 
# code.The dictionaries corresponding to the students should be appended in the order in which they appear in the sequence 
# of inputs.
# Input                        Expected Output
# Test Case1
# 1
# Atul
# Varanasi                         CORRECT
# 0
# 100
# 80
# 60
# Test Case2
# 2
# Amir
# Ajmer
# 0                                CORRECT
# 98
# 95
# 92
# Mridula
# Madurai
# 1
# 99
# 90
# 92

scores_dataset = []
n = int(input("Enter number of students in class : "))
for i in range(n):
    d  = {}
    name = input("Enter name : ")
    city = input("Enter city : ")
    seq = int(input("Enter sequence number : "))
    math = int(input("Enter maths marks : "))
    phy = int(input(" Enter physics marks : "))
    chem = int(input(" Enter chemistry marks : "))
    d["Name"] = name
    d["City"] = city
    d["SeqNo"] = seq
    d["Mathematics"] = math
    d["Physics"] = phy
    d["Chemistry"] = chem
    scores_dataset.append(d)
    
print(scores_dataset)