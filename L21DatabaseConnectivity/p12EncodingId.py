# Write a Python program to print an encoding of the ids of the teams whose jersey colour at home is different from the jersey colour when they play away from home.
# 1. The encoding must be using a shift cipher, which is detailed below.
# An alphabet is mapped to another alphabet as follows. For a given alphabet α, let pos be the position at which α occurs in the alphabet listing (A at 1, B at 2, …. Z at 26). Then the encoding of α is the alphabet at the position (pos + 7) mod 26.
# For example, if M is the alphabet, then the position at which M occurs in the alphabet listing is 13. Then, the encoding of M is the alphabet at the position (13 + 7) mod 26 = 20, which is T. 
# For each digit β, the encoding of β is (β+7) mod 10.
# For example, if 3 is the digit, then the encoding of 3 is the number (3 + 7) mod 10 = 0.
# The ids should be listed in the ascending order before performing the encoding.
# Each line in the output of the program must correspond to one row retrieved from the table.

import mysql.connector

try:
    conn = None
    conn = mysql.connector.connect(database = "football",user = "root",password = "Aayushi@123",host = "localhost",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute('''select team_id from teams where jersey_home_color <> jersey_away_color''')
    rows = cur.fetchall()
    letter = "ABCDEFGHIJKLMNOPQRSTUUVWXYZ"
    for row in rows:
        s = ""
        for j in row[0]:
            if(j.isalpha()):
                s = s + letter[(letter.index(j)+7)%26]
            else:
                s = s + str((int(j) + 7) % 10)
        print(s)
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