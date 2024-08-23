# Program to solve SHO using RK4

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0  # Angular frequency
dt = 0.01    # Time step
T = 10.0     # Total time
N = int(T / dt)  # Number of time steps

# Initialize arrays
time = np.linspace(0, T, N)
x = np.zeros(N)
v = np.zeros(N)

# Initial conditions
x[0] = 1.0  # Initial position
v[0] = 0.0  # Initial velocity

# Define the derivatives
def f(x, v):
    return v

def g(x, v):
    return -omega**2 * x

# RK4 integration
for n in range(N-1):
    k1_x = f(x[n], v[n]) * dt
    k1_v = g(x[n], v[n]) * dt
    
    k2_x = f(x[n] + 0.5 * k1_x, v[n] + 0.5 * k1_v) * dt
    k2_v = g(x[n] + 0.5 * k1_x, v[n] + 0.5 * k1_v) * dt
    
    k3_x = f(x[n] + 0.5 * k2_x, v[n] + 0.5 * k2_v) * dt
    k3_v = g(x[n] + 0.5 * k2_x, v[n] + 0.5 * k2_v) * dt
    
    k4_x = f(x[n] + k3_x, v[n] + k3_v) * dt
    k4_v = g(x[n] + k3_x, v[n] + k3_v) * dt
    
    x[n+1] = x[n] + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    v[n+1] = v[n] + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6

# Plot time series
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(time, x)
plt.title('Time Series')
plt.xlabel('Time')
plt.ylabel('Position')

# Plot phase plot
plt.subplot(1, 2, 2)
plt.plot(x, v)
plt.title('Phase Plot')
plt.xlabel('Position')
plt.ylabel('Velocity')

plt.tight_layout()
plt.show()
