# A round-robin tournament is one in which each team competes with every other team. Consider a version of the IPL tournament in which every team plays exactly one game against every other team. All these games have a definite result and no match ends in a tie. The winning team in each match is awarded one point.
# Eight teams participate in this round-robin cricket tournament: CSK, DC, KKR, MI, PK, RR, RCB and SH. You are given the details of the outcome of the matches. Your task is to prepare the IPL points table in descending order of wins. If two teams have the same number of points, the team whose name comes first in alphabetical order must figure higher up in the table.
# There are eight lines of input. Each line is a sequence of comma-separated team names. The first team across these eight lines will always be in this order: CSK, DC, KKR, MI, PK, RR, RCB and SH. For a given sequence, all the other terms represent the teams that have lost to the first team. For example, the first line of input could be: CSK,MI,DC,PK. 
# This means that CSK has won its matches against the teams MI, DC and PK and lost its matches against all other teams. 
# If a sequence has just one team, it means that it lost all its matches.
# Print the IPL points table in the following format — team:wins — one team on each line. There shouldn't be any spaces in any of the lines.
# Input                                            Expected Output
# Test Case1
# CSK,DC,KKR,MI,PK,RR,RCB,SH                        CSK:7
# DC,KKR,MI,PK,RR,RCB,SH                            DC:6
# KKR,MI,PK,RR,RCB,SH                               KKR:5
# MI,PK,RR,RCB,SH                                   MI:4
# PK,RR,RCB,SH                                      PK:3
# RR,RCB,SH                                         RR:2
# RCB,SH                                            RCB:1
# SH                                                SH:0                                                                                               
# Test Case2
# CSK,DC,MI,PK                                      SH:5
# DC,RR,RCB,SH                                     KKR:4
# KKR,CSK,DC,RR,MI                                  PK:4
# MI,DC,RCB,RR                                     CSK:3
# PK,DC,KKR,MI,RCB                                  DC:3
# RR,CSK,PK,SH                                      MI:3
# RCB,CSK,KKR,RR                                   RCB:3
# SH,CSK,KKR,MI,PK,RCB                              RR:3
# Test Case3
# CSK,RCB,MI,KKR                                    MI:5
# DC,CSK,KKR,MI,SH                                  DC:4
# KKR,PK,RR,RCB,SH                                 KKR:4
# MI,KKR,PK,RR,SH,RCB                               RR:4
# PK,CSK,DC,RCB                                    CSK:3
# RR,CSK,DC,PK,SH                                   PK:3
# RCB,DC,RR                                         SH:3
# SH,CSK,PK,RCB                                    RCB:2

results = [ ]
for i in range(8):
    L = input("Enter team name separated by comma : ").split(',')
    winner = L[0]       
    losers = L[1: ]    
    results.append((winner, len(losers)))

table = [ ]
while results != [ ]:
    maxteam = results[0]
    for i in range(len(results)):
        team = results[i]
        if team[1] > maxteam[1]:
            maxteam = team
        elif team[1] == maxteam[1] and team[0] < maxteam[0]:
            maxteam = team
    results.remove(maxteam)
    table.append(maxteam)

for team in table:
    print(f'{team[0]}:{team[1]}')