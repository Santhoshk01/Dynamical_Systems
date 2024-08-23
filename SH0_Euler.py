# Program to solve SHO using Euler

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# parameters
w = 1.0     # angular frequency
dt = 0.00001   # time step
T = 50      # total time
N = int(T / dt)     # number of time steps

# initialize array
time = np.linspace(0,T,N)
x = np.zeros(N)
v = np.zeros(N)

# initial condition
x[0] = 1.0  # initial position
v[0] = 0.   # intial velocity

# Euler integration
for n in range(0,N-1):
    x[n+1] = x[n] + v[n]* dt
    v[n+1] = v[n] - w**2 * x[n] * dt

# plot time series
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(time,x)
plt.title("Time Series")
plt.xlabel("Time")
plt.ylabel("Position")

# plot phase plot
plt.subplot(1,2,2)
plt.plot(x,v)
plt.title("Phase Plot")
plt.xlabel("Position")
plt.ylabel("Velocity")

plt.tight_layout()
plt.show()
