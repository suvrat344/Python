# Plot the functions f(x)=sinx and g(x)=cosx on the same graph.

import matplotlib.pyplot as plt
import numpy as np
from math import floor,pi,cos

x = np.arange(0,4*np.pi,0.1)  
y = np.sin(x)
z = np.cos(x)
plt.title("Sine and Cosine Function")
plt.xlabel("Angle in Radian")
plt.ylabel("Value of sine and cosine function")
plt.plot(x,y,label="Sine")
plt.plot(x,z,label="Cosine")
plt.legend(["blue", "green"])
plt.show()