# The scores dataset is a list of dictionaries one of whose entries is given below for your reference:
# {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 55}
# Write a function named get_toppers that accepts three arguments in this order:
# scores_dataset
# subject
# gender
# It should a return a list of the names of students who belong to the gender given by the argument gender ('F' or 'M') and have topped in the subject given by the argument subject. As there could be multiple toppers, your output should be a list of names.
# Input                                                                    Expected Output
# Test Case1
# 100
# get_toppers(scores_dataset, 'Mathematics', 'F')                          ['Mary', 'Ramya']
# Test Case2
# 200
# get_toppers(scores_dataset, 'Physics', 'M')                              ['Sachin']

def get_marks(scores_dataset, subject, gender):
    L = [ ]
    for student in scores_dataset:
        if student['Gender'] == gender:
            marks = student[subject]
            name = student['Name']
            L.append((name, marks))
    return L

def get_toppers(scores_dataset, subject, gender):
    L = get_marks(scores_dataset, subject, gender)
    toppers = [ ]
    maxmarks = 0
    for i in range(len(L)):
        if L[i][1] > maxmarks:
            maxmarks = L[i][1]
            toppers = [L[i][0]]
        elif L[i][1] == maxmarks:
            toppers.append(L[i][0])
    return toppers