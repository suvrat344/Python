# Write a Python program to print the ISBN numbers of books which are published in a given year. Here, the year is obtained as the value of function L(x) (given after the sample output) at x. You have to read the value of x from the input file "number.txt", and use it to find the value of L(x). Your program must assume that the file number.txt resides in the same folder as your Python program.
# You have to iterate through the list and print each value separately as shown in the output below: 
# 9789352921171
# 9789351343202
# 9789353333380
# The line function is given below:
# L3(x) = 2000 + 5*x + 3

import mysql.connector

f = open("D:/Programming/Python/L21DatabaseConnectivity/number.txt","r")
x = f.read()
try:
    l = 2000 + 5 * int(x) + 3
    conn = None
    conn = mysql.connector.connect(database="library1",user="root",password="Aayushi@123",host="127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select ISBN_no from book_catalogue where year = %s",(l,))
    rows = cur.fetchall()
    for i in rows:
        print(i[0])
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