# Assume that several IITs start offering online degrees across multiple branches. The email-id of a student is defined as follows:branch_degree_year_roll@student.onlinedegree.institute.ac.in
# For example, if the email-id is CS_BT_21_7412@student.onlinedegree.iitm.ac.in, then this student is from the computer science branch, pursuing a BTech degree from IITM, starting from the year 2021, with 7412 as the roll number. branch, degree and year are codes of length two, while roll and institute are codes of length four. Accept a student's email-id as input and print the following details, one item on each line:
# (1) Branch
# (2) Degree
# (3) Year
# (4) Roll number
# (5) Institute
# Input                                                   Expected Output
# Test Case1
# CS_BT_21_7412@student.onlinedegree.iitm.ac.in              CS
#                                                            BT
#                                                            21
#                                                            7412
#                                                            iitm
# Test Case2
# MA_MT_24_1948@student.onlinedegree.iitd.ac.in              MA
#                                                            MT
#                                                            24
#                                                            1948
#                                                            iitd

email = input("Enter email : ")
branch = email[:2]
degree = email[3: 5]
year = email[6:8]
roll = email[9:13]
institute = email[-10:-6]

print(f"Branch : {branch}")
print(f"Degree : {degree}")
print(f"Year : {year}")
print(f"Roll : {roll}")
print(f"Institute : {institute}")