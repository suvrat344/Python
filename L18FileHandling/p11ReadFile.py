# Write a function named read_file that accepts a text file named filename as argument. Within the function, read the file and print each line of the file on a separate line in the console. You shouldn't print any extra characters at the end of a line. There shouldn't be an empty line between any two consecutive lines(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 
# 'public_1.txt'.                                                     
# Test Case1
# Input
# public_1.txt
# Expected Output
# 1,It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.
# 2,Numbing the pain for a while will make it worse when you finally feel it.
# 3,Never trust anything that can think for itself if you can't see where it keeps its brain.
# 4,It does not do to dwell on dreams and forget to live.
# 5,Differences of habit and language are nothing at all if our aims are identical and our hearts are open.
# Test Case2
# Input
# public_2.txt
# Expected Output
# 1,Do not pity the dead, Harry. Pity the living, and, above all those who live without love.
# 2,Books! And cleverness! There are more important things, friendship and bravery.
# 3,Every human life is worth the same, and worth saving.
# 4,Differences of habit and language are nothing at all if our aims are identical and our hearts are open.
# 5,We are only as strong as we are united, as weak as we are divided.

def read_file(filename):
    with open(filename,"r") as f:
        x = f.readlines()
        for i in range(len(x)):
            if(i+1==len(x)):
                print(x[i])
            else:
                print(x[i][:-1])
    f.close()