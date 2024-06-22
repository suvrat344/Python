# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# Example
# N = 4
# append 1: Append 1 to the list,arr = [1]
# append 2: Append 2 to the list,arr = [1,2]
# insert 3 1: Insert 3 at index 1,arr = [1,3,2]
# print: Print the array
# : Append  to the list, .
# Output:
# [1, 3, 2]

N = int(input("Enter number of operation you want to perform : "))
l = []

for i in range(N):
    n = input("Enter operation : ").split()
    if(n[0] == "insert"):
        l.insert(int(n[1]),int(n[2]))
    elif(n[0] == "append"):
         l.append(int(n[1]))
    elif(n[0] == "remove"):
        l.remove(int(n[1]))
    elif(n[0] == "sort"):
        l.sort()   
    elif(n[0] == "pop"):
        l.pop()
    elif(n[0] == "reverse"):
        l = l[::-1]
    else:
        print(l)