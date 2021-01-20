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

title = "g = " + str(g) + " m/s^2 " + "|" + " m = " + str(m) + " Kg " + "|" + " L = " + str(L) + " m " + "|" + " Initial Angle = " + str(initialAngle) + " Degrees"
fig.suptitle(title)

ax[0, 0].plot(theta, omega, "r-")
ax[0, 0].set_title("Phase Space")
ax[0, 0].set_xlabel(r"$\theta$")
ax[0, 0].set_ylabel(r"$\dot{\theta}$")
particle1, = ax[0, 0].plot([], [], 'bo')

ax[0, 1].plot(time, theta, "r-")
ax[0, 1].set_title(r"$\theta$")
ax[0, 1].set_xlabel("Time (s)")
ax[0, 1].set_ylabel(r"$\theta$")
particle2, = ax[0, 1].plot([], [], 'bo')


ax[1, 0].plot(time, Kinetic_Energy, label = "Kinetic Energy")
ax[1, 0].plot(time, Potential_Energy, label = "Potential Energy")
ax[1, 0].plot(time, Energy, label = "Total Energy")
ax[1, 0].legend("lower right")
particle3, = ax[1, 0].plot([], [], "bo")


X = L * np.sin(theta)
Y = - L * np.cos(theta)

if abs(min(X)) > abs(min(Y)):
    Scale = abs(min(X))
else:
    Scale = abs(min(Y))

maxTime = max(time)
line, = ax[1, 1].plot([], [])
trajectory, = ax[1, 1].plot([],[])
ax[1, 1].set_title("Pendulum Animation")
time_template = r"$t = %.1fs$"
time_text = ax[1, 1].text(0, 0, "")
theta_template = r"$\theta = %.1f degrees$"
theta_text = ax[1, 1].text(0, 0.02, "")


plt.tight_layout()

def init():
    particle1.set_data([], [])
    particle2.set_data([], [])
    particle3.set_data([], [])

    line.set_data([], [])
    trajectory.set_data([],[])
    time_text.set_text("")
    theta_text.set_text("")
    return particle1, particle2, particle3, line, trajectory, time_text, theta_text

def animate(i):
    particle1.set_data(theta[i], omega[i])
    particle2.set_data(time[i], theta[i])
    particle3.set_data(time[i], Potential_Energy[i])

    line.set_data([0, X[i]], [0, Y[i]])
    trajectory.set_data(X[:i],Y[:i])
    time_text.set_text(time_template % (i * step_size))
    theta_text.set_text(theta_template % (theta[i] * 57.296))
    return particle1, particle2, particle3, line, trajectory, time_text, theta_text

frames = np.floor(np.linspace(0, len(theta) - 1, int(5 * maxTime))).astype(np.int)

anim = FuncAnimation(fig, animate, frames, init_func = init)

plt.show()