# A simple algorithm has to be designed to find out whether a student belongs to the Data Science branch or not. The input will be a student's roll number, which is of the form BR18B0000. Here, BR represents the branch code,18 represents the year of joining, B represents the education level and 0000 represents the specific identification given to the student of that batch. The branch code for Data Science is DS. Print True if the student belongs to Data Science branch and False otherwise.
# Input             Expected Output
# Test Case1
# DS18M0001           True
# Test Case2
# ME14B1008           False

rno = input("Enter roll number : ")
branch = rno[:2]
print(f"Student belongs to Data Science => {branch =='DS'}.")