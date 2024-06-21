# A bot starts at the origin — (0,0) — and can make the following moves:
# (1) UP
# (2) DOWN
# (3) LEFT
# (4) RIGHT
# Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input. The first entry in the sequence is always START while the last entry in the sequence is always STOP. A sample sequence is given below:
# START
# UP
# RIGHT
# LEFT
# LEFT
# DOWN
# UP
# STOP
# Print the Manhattan distance of the bot from the origin. If the bot is at the position (x,y), then its Manhattan distance from the origin is given by the equation:
#                                           D=∣x∣+∣y∣
# Input                                    Expected Output
# Test Case1
# START
# UP
# RIGHT
# LEFT                                         2
# LEFT
# DOWN
# UP
# STOP
# Test Case2
# START
# RIGHT
# RIGHT                                        4
# RIGHT
# UP
# STOP

x, y = 0, 0        
seq = input("Enter UP/DOWN/RIGHT/LEFT/STOP : ")
while seq != 'STOP':
    if seq == 'UP':
        y += 1
    if seq == 'DOWN':
        y -= 1
    if seq == 'LEFT':
        x -= 1
    if seq == 'RIGHT':
        x += 1
    seq = input("Enter UP/DOWN/RIGHT/LEFT/STOP : ")

dist = abs(x) + abs(y)
print(dist)