from simple_pendulum import SimplePendulum
import matplotlib.pyplot as plt
from numpy import cos


def plot_energy(initialAngle, m = 1, L = 1, g = 9.8, cycles = 10, step_size = 0.001, plotting = False):
    pend = SimplePendulum(initialAngle = initialAngle, g = g, m = m, L = L, cycles = cycles, step_size = step_size)
    time, theta, thetaDot, _ = pend.non_linear_rk4()
    
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
    import yaml
    with open('parameters.yaml') as file:
        data = yaml.load(file, Loader = yaml.FullLoader)

    g = data["g"]
    m = data["m"]
    L = data["L"]
    cycles = data["cycles"]
    step_size = data["step_size"]
    initialAngle = data["initialAngle"]

    print("Initial Angle = " + str(initialAngle) + " Degrees")
    print("Acceleration Due to Gravity = " + str(g) + " m/s^2")
    print("Mass of the Bob = " + str(m) + " Kg")
    print("Length of the Pendulum = " + str(L) + " m")
    print("Number of Oscillations = " + str(cycles))
    print("Chosen Step Size for RK4 = " + str(step_size))
    _, _, _, _ = plot_energy(initialAngle = initialAngle, m = m, L = L, g = g, cycles = cycles, step_size = step_size, plotting = True)