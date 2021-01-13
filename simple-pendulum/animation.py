import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from simple_pendulum import SimplePendulum

import yaml
# Initial Conditions
with open('parameters.yaml') as file:
    data = yaml.load(file, Loader = yaml.FullLoader)

#g = data["g"]
planet = data["planet"]
if planet.lower() == "earth":
    g = 9.81
elif planet.lower() == "moon":
    g = 1.6
elif planet.lower() == "mars":
    g = 3.72076
m = data["m"]
L = data["L"]
totalTime = data["totalTime"]
step_size = data["step_size"]
initialAngle = data["initialAngle"]

pendulum = SimplePendulum(initialAngle = initialAngle, g = g, m = m, L = L, totalTime = totalTime, step_size = step_size)
time, theta, _, _= pendulum.non_linear_rk4()

X = L * np.sin(theta)
Y = - L * np.cos(theta)

if abs(min(X)) > abs(min(Y)):
    Scale = abs(min(X))
else:
    Scale = abs(min(Y))

maxTime = max(time)

fig, ax = plt.subplots()

title = "g = " + str(g) + " m/s^2 " + "|" + " m = " + str(m) + " Kg " + "|" + " L = " + str(L) + " m " + "|" + " Initial Angle = " + str(initialAngle) + " Degrees"
ax.set_title(title)

ax.set(xlim = (-Scale, Scale), ylim = (-3 * Scale, Scale))

line, = ax.plot([],[])
trajectory, = ax.plot([],[])
time_template = r"$t = %.1fs$"
time_text = ax.text(-0.5 * Scale, -0.5 * Scale, "")
theta_template = r"$\theta = %.1f degrees$"
theta_text = ax.text(0.5 * Scale, -0.5 * Scale, "")

def init():
    line.set_data([], [])
    trajectory.set_data([],[])
    time_text.set_text("")
    theta_text.set_text("")
    return line, trajectory, time_text, theta_text

def animate(i):
    line.set_data([0, X[i]], [0, Y[i]])
    trajectory.set_data(X[:i],Y[:i])
    time_text.set_text(time_template % (i * step_size))
    theta_text.set_text(theta_template % (theta[i] * 57.296))
    return line, trajectory, time_text, theta_text

frames = np.floor(np.linspace(0, len(X) - 1, int(5 * maxTime))).astype(np.int)

anim = animation.FuncAnimation(fig, animate, frames, init_func = init)

plt.show()