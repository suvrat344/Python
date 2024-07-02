# Write a Python program to print the student's first name, the corresponding department name and the respective year of date of birth, if the year is even then print "Even" or else "Odd".
# Student's first name is given in a file named 'name.txt' resides in the same folder as python program file.
# The output of the python program is only student's first name, the corresponding department name and year of date of birth,if the year is even then "Even" or else "Odd".
# For example, 'Suman' and 'Computer Science' is the name and department name of the student. '2002' is the year he was born in. '2002' is even. Then, the final output will be Suman,Computer Science,Even only. Note: No spaces.
# For example, 'Vinod' and 'Electrical Engineering' is the name and department name of the student. '2003' is the year he was born in. '2003' is not even. Then, the final output will be Vinod,Electrical Engineering,Odd only. Note: No spaces.

import mysql.connector

f = open('name1.txt','r')
name = f.read()

try:
    conn = None
    conn = mysql.connector.connect(database = 'library',user = 'root',password = 'India@122',host = "127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select s.student_fname,d.department_name,s.dob from students s inner join departments d on \
                s.department_code = d.department_code where s.student_fname=%s",(name,))
    rows = cur.fetchall()
    for row in rows:
        date = int(str(row[2]).split("-")[0])
        if(date%2==0):
            print(row[0],row[1],"Even")
        else:
                      print(row[0],row[1],"Odd")
    conn.commit()
    cur.close()
    
except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)
    
finally:
    if conn is not None:
        conn.close()
