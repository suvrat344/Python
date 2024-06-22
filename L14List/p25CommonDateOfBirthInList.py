# You are given the names and dates of birth of a group of people. Find all pairs of members who share a common date of birth.Note that this date need not be common across all pairs. It is sufficient if both members in a pair have the same date of birth.
# The first line of input is a sequence of comma-separated names. The second line of input is a sequence of 
# comma-separated positive integers. Each integer in the sequence will be in the range [1,365], endpoints inclusive, and stands for some day in the year.
# Find all pairs of names that share a common date of birth and store them in a list called common. Each element of this list is itself a list, and should be of the form [name1, name2], such that name1 comes before name2 in alphabetical order.
# Notes
# (1) The pairs can be appended to the list common in any order. Only the names within a pair should be in dictionary order.
# (2) You can assume that each test case will have at least one pair of members who share the same date of birth.
# (3) You do not have to print the output to the console. This is the responsibility of the autograder. You just have to populate the list common in the required format.
# Sample Input/Output
# For example, consider the input:
# sachin,ramesh,rohit,priya,saina,sandeep,stella
# 100,50,100,20,30,20,20
# Your list common could look like this:
# [['rohit', 'sachin'], ['priya', 'sandeep'], ['priya', 'stella'], ['sandeep', 'stella']]
# Input                                                                       Expected Output
# Test Case 1
# sachin,ramesh,kalam,priya,saina,sandeep,stella                                kalam,sachin
# 100,50,100,20,30,20,20                                                        priya,sandeep
#                                                                               priya,stella
#                                                                               sandeep,stella
# Test Case2
# newton,euler,gauss,pascal,fourier,leibniz,hardy,erdos
# 50,189,246,50,189,365,365,246                                                 erdos,gauss
#                                                                               euler,fourier
#                                                                               hardy,leibniz
#                                                                               newton,pascal

names = input("Enter comma separated names : ").split(',')
bdays = input("Enter comma separated integer in range [1,365] : ").split(',')
n = len(names)
for i in range(n):
    bdays[i] = int(bdays[i])

common = [ ]
for i in range(n):
    for j in range(n):
        if ((i != j) and
            (bdays[i] == bdays[j]) and
            names[i] < names[j]):
            pair = [names[i], names[j]]
            common.append(pair)
print(common)