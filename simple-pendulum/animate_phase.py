from simple_pendulum import SimplePendulum
from phase_space import multiple_phase_plot
from energy import plot_energy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import yaml

with open('parameters.yaml') as file:
            data = yaml.load(file, Loader = yaml.FullLoader)

planet = data["planet"]
if planet.lower() == "earth":
    g = 9.81
elif planet.lower() == "moon":
    g = 1.6
elif planet.lower() == "mars":
    g = 3.72076
m = data["m"]
L = data["L"]
totalTime= data["totalTime"]
step_size = data["step_size"]
initialAngle = data["initialAngle"]

pendulum = SimplePendulum(initialAngle = initialAngle, g = g, m = m, L = L, totalTime = totalTime, step_size = step_size)
time, _, _, _ = pendulum.non_linear_rk4()
theta, omega = multiple_phase_plot(initialAngles = initialAngle, m = m, L = L, g = g, totalTime = totalTime, step_size = step_size)
_, Kinetic_Energy, Potential_Energy, Energy = plot_energy(initialAngle = initialAngle, m = m, L = L, g = g, totalTime = totalTime, step_size = step_size)

maxTime = max(time)

fig, ax = plt.subplots(nrows = 2, ncols = 2)

ax[0, 0].plot(theta, omega, "r-")
particle1, = ax[0, 0].plot([], [], 'bo')

ax[0, 1].plot(time, theta, "r-")
particle2, = ax[0, 1].plot([], [], 'bo')


ax[1, 0].plot(time, Kinetic_Energy, label = "Kinetic Energy")
ax[1, 0].plot(time, Potential_Energy, label = "Potential Energy")
ax[1, 0].plot(time, Energy, label = "Total Energy")
ax[1, 0].legend("lower right")
particle3, = ax[1, 0].plot([], [], "bo")


plt.tight_layout()

def init():
    particle1.set_data([], [])
    particle2.set_data([], [])
    particle3.set_data([], [])
    return particle1, particle2, particle3

def animate(i):
    particle1.set_data(theta[i], omega[i])
    particle2.set_data(time[i], theta[i])
    particle3.set_data(time[i], Potential_Energy[i])
    return particle1, particle2, particle3

frames = np.floor(np.linspace(0, len(theta) - 1, int(5 * maxTime))).astype(np.int)

anim = FuncAnimation(fig, animate, frames, init_func = init)

plt.show()