# Program to solve vanderpol oscillator

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameters
u = 2.5     # control parameter
dt = 0.001
T = 100
time = np.arange(0,T,dt)

# initial conditon
x0 = 1.0
y0 = -0.87
ic = [x0,y0]

# define the system
def vanderpol_osc(z,t,u):
    x,y = z
    dxdt = y
    dydt = u * (1-x**2) * y - x
    return [dxdt,dydt]

# solve ode
sol = odeint(vanderpol_osc,ic, time, args=(u,))

# extract the values
x = sol[:, 0]
y = sol[:, 1]

# plot the results
plt.figure(figsize=(12,6))

# plot the time series
plt.subplot(1,2,1)
plt.plot(time,x, 'b')
plt.title("TimeSeries")
plt.xlabel("Time")
plt.ylabel("Position")

# plot the phase plot
plt.subplot(1,2,2)
plt.plot(x,y, 'b')
plt.title("Phase Plot")
plt.xlabel("Position")
plt.ylabel("Velocity")

plt.tight_layout()
plt.show()
