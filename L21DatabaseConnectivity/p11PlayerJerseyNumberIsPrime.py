# Write a Python program to print the names of the players and the team of each player of all those players whose jersey number is a prime number. 
# 1. The list should be ordered in reverse alphabetical order of player names. If two or more players have the same name, then further sorting should be done on the team name, again in reverse alphabetical order.
# 2. The format of output is as given below: Name of the player, followed by a comma (,), then a space and then the team name.
# For example, if Arjun has jersey number 5 and is playing for All Stars and Pranav, with jersey number 7, is playing for team Amigos, then the output will be:
# Pranav, Amigos
# Arjun, All Stars


import mysql.connector

def isPrime(num):
    if(num==1):
        return False
    elif(num==2 or num==3):
        return True
        
    for i in range(2,num // 2 + 1):
        if(num % i == 0):
            return False
    return True
try:
    conn = None
    conn = mysql.connector.connect(database = "football",user = "root",password = "Aayushi@123",host = "127.0.0.1",auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute('''select  players.name,teams.name,players.jersey_no from players inner join teams on players.team_id = \
    teams.team_id order by players.name desc,teams.name desc''')
    rows = cur.fetchall()
    for row in rows:
        pname = row[0]
        tname = row[1]
        jno = row[2]
        if isPrime(jno):
            print(pname+", "+tname)
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