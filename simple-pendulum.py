import numpy as np
import matplotlib.pyplot as plt

# Defining Constants
L = 1
g = 9.8
h = 0.001 # Step Size

cycles = 10 
t = np.arange(start = 0, stop = cycles, step = h)
N = len(t) # Number of time steps

omega = np.zeros(N) # Angular Velocity (Theta Dot)
theta = np.zeros(N) # Angular Position (Theta)

# Initial Conditions
theta[0] = np.radians(90.0)
omega[0] = np.radians(0.0)

def omegaDot(theta):
    return (-g / L) * np.sin(theta)

for i in range(N-1):
    dtheta1 = h * omega[i]
    domega1 = h * omegaDot(theta[i])

    dtheta2 = h * (omega[i] + domega1/2)
    domega2 = h * omegaDot(theta[i] + dtheta1/2)

    dtheta3 = h * (omega[i] + domega2/2)
    domega3 = h * omegaDot(theta[i] + dtheta2/2)

    dtheta4 = h * (omega[i] + domega3)
    domega4 = h * omegaDot(theta[i] + dtheta3)

    dtheta = (dtheta1 + 2*dtheta2 + 2*dtheta3 + dtheta4) / 6
    domega = (domega1 + 2*domega2 + 2*domega3 + domega4) / 6

    theta[i+1] = theta[i] + dtheta
    omega[i+1] = omega[i] + domega


#plt.plot(t, theta)
#plt.plot(t, omega)
#plt.plot(theta, omega)
plt.show()