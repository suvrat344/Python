# Accept the date in DD-MM-YYYY format as input and print the year as output.
# Input              Expected Output
# Test Case1
# 25-01-1992              1992
# Test Case2
# 10-09-2001              2001

date = input("Enter date in format DD-MM-YYYY : ")
year = date[-4: ]
print(f"Fetched year from {date} is {year}.")