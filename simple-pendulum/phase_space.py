from simple_pendulum import SimplePendulum
import matplotlib.pyplot as plt
import sys

def multiple_phase_plot(initialAngles, plotting = False):
    if type(initialAngles) is not list:
        initialAngles = [initialAngles]

    for initialAngle in initialAngles:
        pend = SimplePendulum(initialAngle = initialAngle)
        _, theta, omega = pend.non_linear_rk4()
        if plotting:
            plt.plot(theta, omega, label = str(initialAngle) + " degrees")

    if plotting:
        plt.title("Phase Space Plot")
        plt.xlabel(r"$\theta$")
        plt.ylabel(r"$\dot{\theta}$")
        plt.legend()
        plt.show()

    

if __name__ == "__main__":
    initialAngles = []
    for element in sys.argv[1:]:
        initialAngles.append(int(element))
    multiple_phase_plot(initialAngles, plotting = True)