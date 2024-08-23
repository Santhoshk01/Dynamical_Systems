# Program to solve the Duffing oscillator

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameters
a = -1.
b = 1.
g = 0.5
d = 0.3
w = 1.22

# time
time = np.arange(0,500,0.01)

# initial conditon
x0 = 1.
y0 = 0.
ic = [x0,y0]

#define system
def duffing(z, t, a, b, g, d, w):
    x, y = z
    dxdt = y
    dydt = g * np.cos(w*t) - d * y - a * x - b * x**3
    return [dxdt, dydt]

# solve ode
sol = odeint(duffing,ic,time,args=(a,b,g,d,w))

# extract values
x = sol[:, 0]
y = sol[:, 1]

# plot results
plt.figure(figsize=(12,4))

# time series
plt.subplot(1,2,1)
plt.plot(time,x,'b')
plt.title("Time Series")
plt.xlabel("Time")
plt.ylabel("x")

# plot phase plot
plt.subplot(1,2,2)
plt.plot(x,y,'b')
plt.title("Phase plot")
plt.xlabel("x")
plt.ylabel("y")

plt.tight_layout()
plt.show()
