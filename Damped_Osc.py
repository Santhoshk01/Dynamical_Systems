# same previous problem using odeint

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameters
w = 1.0
b = 0.1
dt = 0.01
T = 50
time = np.arange(0,T,dt)

# intial conditions
x0 = 1.0
v0 = 0
initial_condition = [x0,v0]

# define the system
def damped_osc(y,t,w,b):
    x,v = y
    dydt = [v, -2*b*v - w**2 *x]
    return dydt

# solve ode
solution = odeint(damped_osc, initial_condition, time, args=(w,b))

# extract the results
x = solution[:,0]
v = solution[:,1]

# plot time series
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(time,x,'k')
plt.title("Time Series")
plt.xlabel("Time")
plt.ylabel("Position")

#plot phase plot
plt.subplot(1,2,2)
plt.plot(x,v,'k')
plt.title("Phase Plot")
plt.xlabel("Position")
plt.ylabel("Velocity")

plt.tight_layout()
plt.show()
