# A data science company wants to hire data scientists from IIT Madras. The company follows a certain criteria for 
# selection:for a student to be selected, the number of backlogs should be at most 5 and the CGPA (Cumulative Grade Point 
# Average) should be greater than 6. If the student does not fit the above criteria, then the student is not offered the 
# job. If the student is selected, then the salary offered is equal to 5 times his/her CGPA (in lakhs).
# Accept the number of backlogs (integer) and the CGPA (float) of the student as input. Your task is to determine if the 
# student is selected or not. If the student is selected, then print the package. If not, then print the string Not 
# Selected.
# Input                 Expected Output
# Test Case1
# 6                      Not Selected
# 7.0
# Test Case2
# 4                           40.0
# 8.0

backlogs = int(input("Total Backlogs : "))
cgpa = float(input("CGPA : "))
if (cgpa <= 6 or backlogs > 5):
    print ('Not Selected')
else:
    package = 5 * cgpa
    print(package)