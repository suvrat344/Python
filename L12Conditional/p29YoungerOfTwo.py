# You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).
# The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
# Input                                                      Expected Output
# Test Case1
# Harsh
# 10-03-1990                                                       Harsh
# Sparsh
# 18-12-1987
# Test Case2
# Harsh
# 18-01-2000                                                       Sparsh
# Sparsh
# 18-03-2000

c1_name = input("Enter name : ")  
c1_dob = input("Enter date of birth : ")    
c2_name = input("Enter name : ")   
c2_dob = input("Enter date of birth : ")   

c1_dob_day, c1_dob_month, c1_dob_year = int(c1_dob[: 2]), int(c1_dob[3 : 5]), int(c1_dob[6: ])
c2_dob_day, c2_dob_month, c2_dob_year = int(c2_dob[: 2]), int(c2_dob[3 : 5]), int(c2_dob[6: ])

younger = '' 

if c1_dob_year > c2_dob_year:
    younger = c1_name  
elif c2_dob_year > c1_dob_year:
    younger = c2_name  
else:
    if c1_dob_month > c2_dob_month:
        younger = c1_name
    elif c2_dob_month > c1_dob_month:
        younger = c2_name
    else:
        if c1_dob_day > c2_dob_day:
            younger = c1_name
        elif c2_dob_day > c1_dob_day:
            younger = c2_name
        else:
            if c1_name < c2_name:
                younger = c1_name  
            else:
                younger = c2_name  
print(younger)