# The equation of a circle centered at the origin of radius r is given by the following equation:
# x^2+y^2=r^2
# Draw a circle of radius 5 using Matplotlib using a scatter plot.

import matplotlib.pyplot as plt

x = []
y = []
for i in range(-5,6):
      for j in range(-5,6):
            if(i*i+j*j==25):
                x.append(i)
                y.append(j)
plt.title("Circle of radius 5 unit")
plt.scatter(x,y)
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.show()