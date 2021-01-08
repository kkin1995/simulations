from simple_pendulum import SimplePendulum
import matplotlib.pyplot as plt
from numpy import cos


def plot_energy(initialAngle, m = 1, L = 1, g = 9.8, cycles = 10, step_size = 0.001, plotting = False):
    pend = SimplePendulum(initialAngle = initialAngle, g = g, L = L, cycles = cycles, step_size = step_size)
    time, theta, thetaDot = pend.non_linear_rk4()
    
    Kinetic_Energy = (1/2) * m * (L ** 2) * (thetaDot ** 2)
    Potential_Energy = m * g * L * (1 - cos(theta))
    Energy = Kinetic_Energy + Potential_Energy

    if plotting:
        plt.title("Energy")
        plt.xlabel("Time (s)")
        plt.ylabel("Energy")
        plt.plot(time, Kinetic_Energy, label = "Kinetic Energy")
        plt.plot(time, Potential_Energy, label = "Potential Energy")
        plt.plot(time, Energy, label = "Total Energy")
        plt.legend(loc = "lower right")
        plt.show()
    
    return time, Kinetic_Energy, Potential_Energy, Energy

if __name__ == "__main__":
    initialAngle = 20
    _, _, _, _ = plot_energy(initialAngle = initialAngle, plotting = True)