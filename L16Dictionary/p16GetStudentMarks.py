# Each student-entry in the dataset is represented as a dictionary. For example, one of the entries would look like this:
# {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}
# All keys of the dict are strings. For SeqNo and all the subjects, the corresponding values are integers. The values corresponding to Name, Gender and City are strings.
# The entire dataset is represented as a list of dictionaries. That is, each element of the list will be a dictionary like the one given above. This list is named scores_dataset. The SeqNo is a unique identifier for each student that runs from n−1, where  is the total number of students in the dataset.
# Write a function named get_marks that accepts the scores_dataset and a variable named subject as arguments. It should return the marks scored by all students in subject as a list of tuples. Each element in this list is of the form (Name, Marks). The order in which the tuples are appended to the list doesn't matter.
# Input                                   Expected Output
# Test Case1
# 100                                         Arshad:89
# get_marks(scores_dataset, 'Physics')        Clarence:50
#                                             Harshad:50
#                                             Rajneesh:77
#                                             Vincent:47
# Test Case2
# 200
# get_marks(scores_dataset, 'History')       Ramya:94
#                                            Clarence:45
#                                            Danny:76
#                                            Kareena:71
#                                            Deepak:41

def get_marks(scores_dataset, subject):
    marks = []
    for i in range(len(scores_dataset)):
        for j in scores_dataset[i]:
            if(j==subject):
                t1 = (scores_dataset[i]["Name"],scores_dataset[i][j])
                marks.append(t1)
                break
    return marks