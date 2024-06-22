# Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.
# Hint
# print([1] + [2])
# print([2] + [1])
# Input                                 Expected Output
# Test Case1
# one,two,three                           three,two,one
# Test Case2
# first,second,third,fourth               fourth,third,second,first

n = input("Enter word separated by comma : ").split(",")
for i in n[::-1]:
    if(i==n[0]):
        print(i)
    else:
        print(i,end=",")