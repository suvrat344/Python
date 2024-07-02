# Write a Python program to print the roll number of the student. Student's first name is given in a file named 'name.txt' resides in the same folder as python program file.
# The output of the python program is only roll number.  
# For example, if the first name of the student is 'Vikas'. Then output must be CS01 only. Note: No spaces.

import mysql.connector 

f = open('D:/Programming/Python/L21DatabaseConnectivity/name.txt','r')
name = f.read()

try:
    conn = None
    conn = mysql.connector.connect(database = "library1",user = "root",password = "Aayushi@123",host = '127.0.0.1',auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select roll_no from students where student_fname = %s",(name,))
    result = cur.fetchall()
    for i in result:
        print(i[0])
    cur.close()
    conn.commit()
    
except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)
    
finally:
    if conn is not None:
        conn.close()