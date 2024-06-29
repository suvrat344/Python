# Plot the following functions using Matplotlib, each on a separate graph.
# f(x)=3x−4
# f(x)=x^2+2x−15
# f(x)=5(x−1)(x−2)(x−3)
# f(x)=e^x
# f(x)=logx
# f(x)=sinx


import matplotlib.pyplot as plt
import numpy as np
from math import floor,pi,cos

x = np.arange(-10,10,1)

y = 3*x - 4
plt.title("f(x)=3x-4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

y = x*x + 2*x - 15
plt.title("f(x)=x^2+2x-15") 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

y = 5*(x-1)*(x-2)*(x-3)
plt.title("f(x)=5(x-1)(x-2)(x-3)") 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

y = np.exp(x)
plt.title("f(x)=e^x") 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

z = np.arange(1,20,1)
y = np.log(z)
plt.title("f(x)=log(x)") 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(z,y)
plt.show()

z = np.arange(-1000,1000,1)
y = np.sin(z * np.pi / 180)
plt.title("f(x)=sin(x)") 
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(z,y)
plt.show()