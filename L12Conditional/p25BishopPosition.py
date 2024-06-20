# Consider the following image of a chess-board

# Accept two positions as input: start and end. Print YES if a bishop at start can move to end in exactly one move. Print 
# NO otherwise. Note that a bishop can only move along diagonals.
# Input                   Expected Output
# Test Case1
# C3                         YES
# E5
# Test Case2
# B2                         NO
# D3

start = input("Enter starting position : ")
end = input("Enter ending position : ")
s1 = "ABCDEFGH"
if(abs(s1.index(start[0]) - s1.index(end[0])) == abs(int(start[1])-int(end[1]))):
    print("YES")
else:
    print("NO")