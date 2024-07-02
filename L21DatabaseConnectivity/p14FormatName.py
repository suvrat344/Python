# In this question, you must write a Python program to output the name of the main referee for a given match date (in yyyy-mm-dd format). The input to your program is a file named “date.txt” that has the match date as the first word of the file. Your program must assume that date.txt resides in the same folder as your Python program. 
# The output name has to be formatted as follows. The last name is displayed followed by the initials of the first name, then a full stop, a space and then the initials of the middle name (if the middle name exists), followed by a full stop.
# 1. For example, if the name of the main referee is "Kennedy Sapam", the output must be "Sapam K.” .
# 2. If the name of the main referee is “Asit Kumar Sarkar”, the output must be ”Sarkar A. K.”

import mysql.connector

f = open('D:/Programming/Python/L21DatabaseConnectivity/date.txt','r')
date = f.read()
date = date.split("-")
    
try:
    conn = None
    conn = mysql.connector.connect(database = "football",user = "root",password = "Aayushi@123",host = "127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select r.name,matches.match_date from referees r inner join match_referees m on r.referee_id = m.referee inner join matches on m.match_num = matches.match_num")
    rows = cur.fetchall()
    for row in rows:
        name = row[0].split(" ")
        match_date = str(row[1]).split("-")
        if(match_date==date):
            if(len(name)==3):
                first_name = name[0]
                middle_name = name[1]
                last_name = name[2]
                print(last_name+" "+first_name[0]+". "+middle_name[0]+".")
            else:
                first_name = name[0]
                last_name = name[1]
                print(last_name+" "+first_name[0]+".")
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