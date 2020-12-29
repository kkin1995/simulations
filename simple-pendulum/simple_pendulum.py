import numpy as np
import matplotlib.pyplot as plt
import sys


class SimplePendulum:
    def __init__(self, initialAngle, g = 9.8, L = 1, cycles = 10, step_size = 0.001):
        self.g = g
        self.L = L
        self.cycles = cycles
        self.step_size = step_size
        self.initialAngle = initialAngle
        self.time = np.arange(start = 0, stop = cycles, step = step_size)

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

        if plotting:
            plt.plot(self.time, self.theta)
        return self.time, self.theta, self.omega

    def linear_approximation(self, plotting = False):
        self.omegaLinear = np.sqrt(self.g/self.L)
        self.thetaLinear = np.array([np.radians(self.initialAngle) * np.cos(self.omegaLinear * t) for t in self.time])
        
        if plotting:
            plt.plot(self.time, self.thetaLinear)
        return self.thetaLinear

    def plot_the_solution(self):
        
        plt.title("Initial Angle: " + str(self.initialAngle) + " Degrees")
        plt.xlabel("Time")
        plt.ylabel("Angle (Radians)")
        plt.legend(["Non-Linear", "Linear"], loc="upper right")
        plt.show()



if __name__ == "__main__":
    # Initial Conditions
    initialAngle = int(sys.argv[1]) # Degrees

    pendulum = SimplePendulum(initialAngle)
    pendulum.non_linear_rk4()
    pendulum.linear_approximation()
    pendulum.plot_the_solution()
