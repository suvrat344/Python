# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# Input
# 5
# 2 3 6 6 5
# Output
# 5

n = 5 
l = [2,3,6,6,5]

l = sorted(set(l),reverse=True)
print(l[1])