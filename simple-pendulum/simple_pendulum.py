import numpy as np
import matplotlib.pyplot as plt
import sys


class SimplePendulum:
    def __init__(self, initialAngle, g = 9.8, m = 1, L = 1, totalTime = 10, step_size = 0.001):
        self.g = g
        self.m = m
        self.L = L
        self.totalTime = totalTime
        self.step_size = step_size
        self.initialAngle = initialAngle
        self.time = np.arange(start = 0, stop = totalTime, step = step_size)

    def omegaDot(self, theta):
        return (-self.g / self.L) * np.sin(theta)

    def non_linear_rk4(self, plotting = False):
    
        N = len(self.time) # Number of time steps
        self.omega = np.zeros(N) # Angular Velocity (Theta Dot)
        self.theta = np.zeros(N) # Angular Position (Theta)
        self.theta[0] = np.radians(self.initialAngle)
        self.omega[0] = np.radians(0.0)
        for i in range(N-1):
            dtheta1 = self.step_size * self.omega[i]
            domega1 = self.step_size * self.omegaDot(self.theta[i])

            dtheta2 = self.step_size * (self.omega[i] + domega1/2)
            domega2 = self.step_size * self.omegaDot(self.theta[i] + dtheta1/2)

            dtheta3 = self.step_size * (self.omega[i] + domega2/2)
            domega3 = self.step_size * self.omegaDot(self.theta[i] + dtheta2/2)

            dtheta4 = self.step_size * (self.omega[i] + domega3)
            domega4 = self.step_size * self.omegaDot(self.theta[i] + dtheta3)

            dtheta = (dtheta1 + 2*dtheta2 + 2*dtheta3 + dtheta4) / 6
            domega = (domega1 + 2*domega2 + 2*domega3 + domega4) / 6

            self.theta[i+1] = self.theta[i] + dtheta
            self.omega[i+1] = self.omega[i] + domega
        
        p_theta = self.m * self.L**2 * self.omega


        plt.plot(self.time, self.theta, label = "Non-Linear")
        return self.time, self.theta, self.omega, p_theta

    def linear_approximation(self, plotting = False):
        self.omegaLinear = np.sqrt(self.g/self.L)
        self.thetaLinear = np.array([np.radians(self.initialAngle) * np.cos(self.omegaLinear * t) for t in self.time])
        
        if plotting:
            plt.plot(self.time, self.thetaLinear, label = "Linear")
        return self.thetaLinear

    def plot_the_solution(self, show = False, save = False):
        
        plt.title("Initial Angle: " + str(self.initialAngle) + " Degrees")
        plt.xlabel("Time")
        plt.ylabel("Angle (Radians)")
        plt.legend(loc="upper right")
        if show:
            plt.show()
        if save:
            plt.savefig("Time vs Theta.png")



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
    L = data["L"]
    totalTime = data["totalTime"]
    step_size = data["step_size"]
    initialAngle = data["initialAngle"]

    print("Initial Angle = " + str(initialAngle) + " Degrees")
    print("Acceleration Due to Gravity = " + str(g) + " m/s^2")
    print("Mass of the Bob = " + str(m) + " Kg")
    print("Length of the Pendulum = " + str(L) + " m")
    print("Total Time = " + str(totalTime))
    print("Chosen Step Size for RK4 = " + str(step_size))

    pendulum = SimplePendulum(initialAngle = initialAngle, g = g, m = m, L = L, totalTime = totalTime, step_size = step_size)
    _, _, _, _ = pendulum.non_linear_rk4(plotting = True)
    _ = pendulum.linear_approximation(plotting = True)
    pendulum.plot_the_solution(save = True)
