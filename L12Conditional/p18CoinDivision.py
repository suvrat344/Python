# You have n gold coins with you. You wish to divide this among three of your friends under the following conditions:
# (1) All three of them should get a non-zero share.
# (2) No two of them should get the same number of coins.
# (3) You should not have any coins with you at the end of this sharing process.
# The input has four lines. The first line contains the number of coins with you. The next three lines will have the share given to your three friends. All inputs shall be non-negative integers. If the division satisfies these conditions, then print the string FAIR. If not, print UNFAIR.
# Input           Expected Output
# Test Case1
# 10
# 2                 FAIR
# 5
# 3
# Test Case2
# 10
# 4                 UNFAIR
# 4
# 2

n =  int(input("Total gold coins : "))
f1 = int(input("Share of first person : "))
f2 = int(input("Share of second person : "))
f3 = int(input("Share of third person : "))

share = True
if f1 + f2 + f3 != n:
    share = False
if f1 == f2 or f2 == f3 or f3 == f1:
    share = False
if f1 == 0 or f2 == 0 or f3 == 0:
    share = False
if share:
    print('FAIR')
else:
    print('UNFAIR')