# filename points to the name of some text file. Each line in this file is missing a period at the end of the line. Write a function named add_period that accepts filename as argument and creates a new file named out.txt. The function should copy the contents of filename into out.txt and add a period at the end of each line.
# (1) filename is a string variable that holds the filename. For example, in the first test case, it is public_1.txt.
# Test Case1
# Input
# public_1.txt
# Expected Output
# 1,Numbing the pain for a while will make it worse when you finally feel it.
# 2,Every human life is worth the same, and worth saving.
# 3,It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.
# Test Case2
# Input
# public_2.txt
# Expected Output
# 1,Books! And cleverness! There are more important things, friendship and bravery.

def add_period(filename):
    f = open(filename, 'r')
    g = open('out.txt', 'w')
    for line in f:
        line = line.strip()
        g.write(line + '.' + '\n')
    f.close()
    g.close()