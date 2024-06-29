# Consider a file named scores.csv that contains the scores of 25 students in Mathematics and Physics.
# Maths,Physics
# 20,80
# 10,30
# 40,30
# 20,30
# 10,5
# 80,90
# 99,100
# 76,84
# 29,100
# 100,30
# 95,92
# 100,100
# 70,74
# 65,88
# 90,93
# 89,91
# 20,40
# 10,30
# 20,25
# 15,34
# 35,25
# 50,70
# 45,55
# 34,43
# 60,67
# Construct a scatter plot with Mathematics scores on the X-Axis and Physics scores on the Y-Axis. You can use plt.scatter for this purpose. Do you observe anything?

import matplotlib.pyplot as plt
import numpy as np

f = open("D:/Programming/Python/L20Matplotlib/scores.csv","r")
f.readline()
phy = []
math = []
x = f.readlines()
for i in x:
    mathematics,physics = i.strip().split(",")
    phy.append(int(physics))
    math.append(int(mathematics))

plt.title("Marks of Student")
plt.scatter(math,phy)
plt.xlabel("Physics Marks")
plt.ylabel("Maths Marks")
plt.show()