# Perform the following experiment:
# (1) Throw a standard, unbiased, six-sided dice n times.
# (2) Get the frequency of occurrence of the numbers from 1 to 6.
# (3) Convert the frequencies to probabilities.
# (4) Represent the probabilities of obtaining each of the six numbers in the form of a bar plot. You can use plt.bar for this purpose.
# Run this experiment for the following values of n:10,100,1000,10000,100000,1000000 and note down your observations.

import matplotlib.pyplot as plt
import numpy as np
import random

def random_number(n):
    l = []
    for i in range(n):
        l.append(random.randint(1,6))
    freq(l)

def freq(l):
    d = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in l:
        if(i in d):
            d[i] = d[i] + 1
    calculate_probability(len(l),d)

def calculate_probability(n,d):
    d1 = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in d:
        if(i in d1):
            d1[i] = d[i] / n
    bar_plot(n,d1)

def bar_plot(n,d):
    plt.title(f"Barplot for tossing  a die for n ={n}")
    plt.xlabel("Possible Outcomes")
    plt.ylabel("Probabilty of outcomes")
    plt.bar(list(d.keys()),list(d.values()))
    plt.show()
    
x1 = random_number(10)
x2 = random_number(100)
x3 = random_number(1000)
x4 = random_number(10000)
x5 = random_number(100000)
x6 = random_number(100000)