# Write the following functions:
# (1) factors: accept a positive integer n as argument. Return the set of all factors of n.
# (2) common_factors: accept two positive integers a and b as arguments. Return the set of common factors of the two numbers. This function must make use of factors.
# (3) factors_upto: accept a positive integer n as argument. Return a dict D, whose keys are integers and values are sets. Each integer in the range [1,n], endpoints inclusive, is a key of D. The value corresponding to a key, is the set of all factors of key. This function must make use of factors.
# The idea we are trying to bring out here is to make use of pre-defined functions whenever needed.
# Input                             Expected Output
# Test Case1
# factors(10)                        {1, 2, 10, 5}
# Test Case2
# common_factors(10, 5)              {1, 5}
# Test Case3
# factors_upto(4)                    {1: {1}, 2: {1, 2}, 3: {1, 3}, 4: {1, 2, 4}}

def factors(n):
    F = set()
    for i in range(1, n + 1):
        if n % i == 0:
            F.add(i)
    return F

def common_factors(a, b):
    fa = factors(a)
    fb = factors(b)
    return fa.intersection(fb)

def factors_upto(n):
    D = dict()
    for i in range(1, n + 1):
        D[i] = factors(i)
    return D

print(factors(10))
print(common_factors(10,5))
print(factors_upto(4))