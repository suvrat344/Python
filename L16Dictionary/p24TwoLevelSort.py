# Write a function named two_level_sort that accepts a list of tuples named scores as argument. Each element in this list is of the form (Name, Marks) and represents the marks scored by a student in a test: the first element is the student's name and the second element is his or her marks.
# The function should return a list of tuples sorted that is sorted in two levels:
# Level-1: ascending order of marks
# Level-2: alphabetical order of names among those students who have scored equal marks
# Each element in the returned list should also be of the form (Name, marks). Note that level-2 should not override level-1.That is, after the second level of sorting, the list should still be sorted in ascending order of marks.
# Additionally, the students having the same marks should appear in alphabetical order.
# Sample input-output behaviour
# scores                                                                two_level_sort(scores)
# [('Harish', 80), ('Aparna', 90), ('Harshita', 80)]            [('Harish', 80), ('Harshita', 80), ('Aparna', 90)]
# [('Sachin', 85), ('Yuvan', 65), ('Anita', 85)]                [('Yuvan', 65), ('Anita', 85), ('Sachin', 85)]
# (1) You should not use any built-in sort functions to solve this problem.
# Input                                                                     Expected Output
# Test Case1
# [('Harish', 80), ('Ram', 90), ('Harshita', 80)]                            Harish:80
#                                                                            Harshita:80
#                                                                            Ram:90
# Test Case2
# [('Sachin', 70), ('Sam', 69), ('Anirudh', 70), ('Anita', 80)]              Sam:69
#                                                                            Anirudh:70
#                                                                            Sachin:70
#                                                                            Anita:80

def two_level_sort(scores):
    sorted_L = [ ]
    while scores != [ ]:
        minentry = scores[0]
        for i in range(len(scores)):
            if scores[i][1] < minentry[1]:
                minentry = scores[i]
            elif (scores[i][1] == minentry[1] and
                  scores[i][0] < minentry[0]):
                minentry = scores[i]
        sorted_L.append(minentry)
        scores.remove(minentry)
    return sorted_L

print(two_level_sort([('Harish', 80), ('Ram', 90), ('Harshita', 80)]))
print(two_level_sort([('Sachin', 70), ('Sam', 69), ('Anirudh', 70), ('Anita', 80)]))