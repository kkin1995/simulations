import numpy as np
import matplotlib.pyplot as plt


class SpringPendulum:
    def __init__(self, initialAngle, initialExtension, g = 9.81, m = 1, l0 = 1, k = 1, totalTime = 10, step_size = 0.001):
        self.initialAngle = initialAngle
        self.initialExtension = initialExtension
        self.g = g
        self.m = m
        self.l0 = l0
        self.k = k
        self.totalTime = totalTime
        self.step_size = step_size
        self.time = np.arange(start = 0, stop = totalTime, step = step_size)

    def v_b_dot(self, b, theta, v_theta, m = 1, l0 = 1, g = 9.81, k = 1):
            return ((self.l0 + b) * (v_theta ** 2)) + (self.g * np.cos(theta)) - ((self.k/self.m) * b)

    def v_theta_dot(self, b, v_b, theta, v_theta, l0 = 1, g = 9.81):
            return ((-2 / (self.l0 + b)) * v_b * v_theta) - ((self.g / (self.l0 + b)) * np.sin(theta))


    def non_linear_rk4(self, plotting = False):
        N = len(self.time)

        theta = np.zeros(N)
        b = np.zeros(N)
        v_b = np.zeros(N)
        v_theta = np.zeros(N)

        theta[0] =  np.radians(self.initialAngle)
        b[0] = self.initialExtension
        v_b[0] = 0.0
        v_theta[0] = np.radians(0.0)

        for i in range(N-1):
            db1 = self.step_size * v_b[i]
            dv_b1 = self.step_size * self.v_b_dot(b[i], theta[i], v_theta[i])
            dtheta1 = self.step_size * v_theta[i]
            dv_theta1 = self.step_size * self.v_theta_dot(b[i], v_b[i], theta[i], v_theta[i])

            db2 = self.step_size * (v_b[i] + (dv_b1 / 2))
            dv_b2 = self.step_size * self.v_b_dot(b[i] + db1/2, theta[i] + dtheta1/2, v_theta[i] + dv_theta1/2)
            dtheta2 = self.step_size * (v_theta[i] + (dv_theta1 / 2))
            dv_theta2 = self.step_size * self.v_theta_dot(b[i] + db1/2, v_b[i] + dv_b1/2, theta[i] + dtheta1/2, v_theta[i] + dv_theta1/2)

            db3 = self.step_size * (v_b[i] + (dv_b2 / 2))
            dv_b3 = self.step_size * self.v_b_dot(b[i] + db2/2, theta[i] + dtheta2/2, v_theta[i] + dv_theta2/2)
            dtheta3 = self.step_size * (v_theta[i] + (dv_theta2 / 2))
            dv_theta3 = self.step_size * self.v_theta_dot(b[i] + db2/2, v_b[i] + dv_b2/2, theta[i] + dtheta2/2, v_theta[i] + dv_theta2/2)

            db4 = self.step_size * (v_b[i] + dv_b3)
            dv_b4 = self.step_size * self.v_b_dot(b[i] + db3, theta[i] + dtheta3, v_theta[i] + dv_theta3)
            dtheta4 = self.step_size * (v_theta[i] + dv_theta3)
            dv_theta4 = self.step_size * self.v_theta_dot(b[i] + db3, v_b[i] + dv_b3, theta[i] + dtheta3, v_theta[i] + dv_theta3)

            db = (db1 + 2*db2 + 2*db3 + db4) / 6
            dv_b = (dv_b1 + 2*dv_b2 + 2*dv_b3 + dv_b4) / 6
            dtheta = (dtheta1 + 2*dtheta2 + 2*dtheta3 + dtheta4) / 6
            dv_theta = (dv_theta1 + 2*dv_theta2 + 2*dv_theta3 + dv_theta4) / 6

            b[i+1] = b[i] + db
            v_b[i+1] = v_b[i] + dv_b
            theta[i+1] = theta[i] + dtheta
            v_theta[i+1] = v_theta[i] + dv_theta

        if plotting:
            plt.plot(self.time, b, label = "Spring Extension")
            plt.plot(self.time, theta, label = r"$\theta$")

        return self.time, b, theta, v_b, v_theta

    def plot_the_solution(self, show = False, save = False):
        
        plt.title("Initial Angle: " + str(self.initialAngle) + " Degrees")
        plt.xlabel("Time")
        plt.ylabel("Angle (Radians) / Extension (m)")
        plt.legend(loc="upper right")
        if show:
            plt.show()
        if save:
            plt.savefig("Variation with time.png")


if __name__ == "__main__":
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
    l0 = data["l0"]
    k = data["k"]
    totalTime = data["totalTime"]
    step_size = data["step_size"]
    initialAngle = data["initialAngle"]
    initialExtension = data["initialExtension"]

    print("Initial Angle = " + str(initialAngle) + " Degrees")
    print("Initial Extension = " + str(initialExtension) + " m")
    print("Acceleration Due to Gravity = " + str(g) + " m/s^2")
    print("Mass of the Bob = " + str(m) + " Kg")
    print("Fixed Length of the Pendulum = " + str(l0) + " m")
    print("Total Time = " + str(totalTime))
    print("Chosen Step Size for RK4 = " + str(step_size))

    pendulum= SpringPendulum(initialAngle = initialAngle, initialExtension = initialExtension)
    pendulum.non_linear_rk4(plotting = True)
    pendulum.plot_the_solution(show = True)