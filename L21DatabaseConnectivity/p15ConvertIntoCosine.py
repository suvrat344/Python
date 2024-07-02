# Write a Python program to find the cosine of a number obtained from performing a computation on a value retrieved from the database. 
# 1. Find the sum of scores of all host teams satisfying the following conditions.
# a. host_team_score > guest_team_score
# b. name of the host team starts with the character given in the input file ‘parameter.txt’. You have to read the character from the file and use it in your query to retrieve the expected sum. Your program must assume that parameter.txt resides in the same folder as your Python program. 
# 2. Let this sum be denoted by ‘S’. Compute X = S * 10. 
# 3. Assuming that X is a value in radians, convert it into degrees. That is, let X_deg = X * (pi/180).
# 4. Then, using the math library in Python, find cos(X_deg) correct up to two decimal places, where cos denotes the mathematical trigonometric function cosine.
# 5. For example, if the sum of scores of all host teams satisfying the given conditions is 5, then the output is round(cos(5*10*(pi/180)),2).

import mysql.connector
from math import cos,pi

f = open('D:/programming/Python/L21DatabaseConnectivity/parameter.txt','r')
team = f.read()
try:
    conn = None
    conn = mysql.connector.connect(database = "football",user = "root",password = "Aayushi@123",host = "127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute("select matches.host_team_score,matches.guest_team_score,teams.name from matches inner join teams on \
    matches.host_team_id=teams.team_id")
    rows = cur.fetchall()
    s = 0
    for row in rows:
        if(team == row[2][0]):
            if(row[0]>row[1]):
                s = s + row[0]
    print(round(cos(s*10*(pi/180)),2))
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