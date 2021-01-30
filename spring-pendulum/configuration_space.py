from spring_pendulum import SpringPendulum
import numpy as np
import matplotlib.pyplot as plt
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

plt.plot(b, theta)
plt.title("Configuration Space")
plt.xlabel("Extension of Spring (m)")
plt.ylabel("Angle of the Pendulum (radians)")
plt.show()