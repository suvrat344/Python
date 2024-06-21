# Accept a positive integer n, with n>1, as input from the user and print all the prime factors of n in ascending order.
# Input                          Expected Output
# Test Case1
# 15                                   3
#                                      5
# Test Case2
# 79                                  79
# Test Case3
# 8                                    2

n = int(input("Enter a positive number : "))
for f in range(2, n + 1):
    # first check if f is a factor of n
    if n % f == 0:
        # now check if f is a prime
        is_prime = True
        for i in range(2, f):
            if f % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f)