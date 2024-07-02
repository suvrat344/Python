# Write a Python program to output the jersey number of the player. Player's name is given in a file named 'player.txt' resides in the same folder as python program file. 
# The output of the python program is only jersey number.  
# For example, if the jersey number of the player is 99. Then output must be 99 only. Note: No spaces.

import mysql.connector

f = open('player.txt','r')
name = f.read()

try:
    conn = None
    conn = mysql.connector.connect(database = "football",user = "root",password = "Aayushi@123",host = "localhost",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select jersey_no from players where name = %s",(name,))
    result = cur.fetchall()
    for i in result:
        print(i[0])
    cur.close()
    
except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)
    
finally:
    if conn is not None:
        conn.close()