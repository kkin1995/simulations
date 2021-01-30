from spring_pendulum import SpringPendulum
import numpy as np
import matplotlib.pyplot as plt
import yaml


# Initial Conditions
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
l0 = data["l0"]
k = data["k"]
totalTime = data["totalTime"]
step_size = data["step_size"]
initialAngle = data["initialAngle"]
initialExtension = data["initialExtension"]

print("Initial Angle = " + str(initialAngle) + " Degrees")
print("Acceleration Due to Gravity = " + str(g) + " m/s^2")
print("Mass of the Bob = " + str(m) + " Kg")
print("Fixed Length of the Pendulum = " + str(l0) + " m")
print("Total Time = " + str(totalTime))
print("Chosen Step Size for RK4 = " + str(step_size))

pendulum = SpringPendulum(initialAngle = initialAngle, initialExtension = initialExtension, g = g, m = m, l0 = l0, k = k, totalTime = totalTime, step_size = step_size)
time, b, theta, v_b, v_theta = pendulum.non_linear_rk4()


fig, ax = plt.subplots(1, 2)
fig.suptitle("Phase Space")

ax[0].plot(theta, v_theta)
ax[0].set_title("Pendulum")
ax[0].set_xlabel(r"$\theta$")
ax[0].set_ylabel(r"$\dot{\theta}$")

ax[1].plot(b, v_b)
ax[1].set_title("Spring")
ax[1].set_xlabel(r"$x$")
ax[1].set_ylabel(r"$\dot{x}$")

plt.show()