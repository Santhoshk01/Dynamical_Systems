# Program to solve Lotka-Volterra system

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameters
a = 1.1     # prey growth rate
b = 0.1     # predator destroys prey
g = 1.5     # predator death rate
d = 0.075   # predator growth rate

# time
T = 50
dt = 0.01
time = np.arange(0,T,dt)

# initial condition
x0 = 40
y0 = 9
ic = [x0,y0]

# define the system
def lotka_volterra(z,t,a,b,g,d):
    x,y = z
    dxdt = a * x - b * x * y
    dydt = d * x * y - g * y
    return [dxdt, dydt]

# solve ode
sol = odeint(lotka_volterra,ic,time,args=(a,b,g,d))

# extract the results
x = sol[:, 0]
y = sol[:, 1]

# plot the results
plt.figure(figsize=(12,6))

# plot time series
plt.subplot(1,2,1)
plt.plot(time, x, label = "Prey")
plt.plot(time, y, label = "Predatator")
plt.title("Time Series")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()

# plot phase plot
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Phase plot")
plt.xlabel("Prey Population")
plt.ylabel("Predator Population")

plt.tight_layout()
plt.show()
