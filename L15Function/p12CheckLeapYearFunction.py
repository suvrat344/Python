# In the Gregorian calendar, a leap year has a total of 366 days instead of the usual 365 as a result of adding an extra day (February 29) to the year. This calendar was introduced in 1582 to replace the flawed Julian Calendar. The criteria given below are used to determine if a year is a leap year or not.
# If a year is divisible by 100 then it will be a leap year if it is also divisible by 400.
# If a year is not divisible by 100, then it will be a leap year if it is divisible by 4.
# Write a function named check_leap_year that accepts a year between 1600 and 9999 as argument. It should return True if 
# the year is a leap year and False otherwise.
# Input                   Expected Output
# Test Case1
# 2020                      True
# Test Case2
# 2021                      False

def check_leap_year(year):
    if(year%100==0 and year%400==0):
        return True
    elif(year%100!=0 and year%4==0):
        return True
    else:
        return False
    
print(check_leap_year(2004))