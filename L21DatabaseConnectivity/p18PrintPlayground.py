# write a Python program to print the playground of the given team id. team_id is given in a file named 'team.txt' resides in the same folder as python program file.
# 1. The output of the python program is only playground name.
# 2. For example, if the team_id is 'T0002' . Then output must be Villa Park only

import mysql.connector

f = open('D:/Programming/Python/L21DatabaseConnectivity/team.txt','r')
team = f.read()

try:
    conn = None
    conn = mysql.connector.connect(database = 'football',user = 'root',password = 'Aayushi@123',host = "127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select playground from teams where team_id = %s",(team,))
    result = cur.fetchall()
    for i in result:
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