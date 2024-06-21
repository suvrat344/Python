# Multiple Select Questions (MSQ) could have more than one correct answers. The marks scored by a student in a MSQ will be determined by the following conditions:
# (1) If the question has c correct options, each individual correct option carries n/c marks.
# (2) If a student selects any of the wrong options, the marks awarded for the question will be 0.
# Calculate the marks obtained by the student and print this as float value.
# The input contains four lines.
# (1) First line is the number of marks for the question.
# (2) Second line contains the number of options for the question.
# (3) Third line is a comma-separated sequence of correct options for this question.
# (4) Fourth line is a comma-separated sequence of options given by the student.
# Write a program to print the number of marks scored by a student.
# Note: Options are numbered using positive integers in the range [1,9], endpoints inclusive. A question will have at most nine options. The number of marks and the correct options will always be integers.
# Input                   Expected Output
# Test Case1
# 4
# 4                            2.0
# 1,3
# 1
# Test Case2
# 10
# 5                            0.0
# 1,3,5
# 1,2,5

n = int(input("Marks for the question : "))
choices = int(input(" Number of options in the question : "))
correct = input("Correct option in comma separated form : ")
c = (len(correct) + 1) // 2
selected = input("Selected option by student in comma separated form : ")
marks = 0.0
for i in range(0, len(selected), 2):
    if selected[i] in correct:
        marks += n/c
    else:
        marks = 0.0
        break
print(marks)