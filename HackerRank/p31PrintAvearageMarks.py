# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Example
# marks key:value pairs are
# 'alpha' : [20,30,40]
# 'beta' : [30,50,70]
# The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0

student_marks = {"alpha":[20,30,40],"beta":[30,50,70]}
query = "alpha"
average = sum(student_marks[query]) / 3
print("{}'s avearge score is {:.2f}".format(query,average))