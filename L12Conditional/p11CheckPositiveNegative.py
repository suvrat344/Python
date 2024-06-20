# Accept a non-zero integer as input. Print positive if it is greater than zero and negative if it is less than zero.
# Input                Expected Output
# Test Case1
# 10                    positive
# Test Case2
# -10                   negative

num = int(input("Enter non-zero integer : "))
res = print("negative") if num<0 else print("positive")