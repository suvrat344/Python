# Accept the registration number of a vehicle as input and print its state-code as output.
# Input              Expected Output
# Test Case1
# TN-10-AB-2010             TN
# Test Case2
# HR-15-XZ-1999             HR

n1 = input("Enter registration number : ")
print(f"State Code of registration number {n1} is {n1[0:2]}.")