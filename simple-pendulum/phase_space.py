from simple_pendulum import SimplePendulum
import matplotlib.pyplot as plt
import sys

def multiple_phase_plot(initialAngles, m = 1, L = 1, g = 9.8, cycles = 10, step_size = 0.001, plotting = False):
    if type(initialAngles) is not list:
        initialAngles = [initialAngles]

    for initialAngle in initialAngles:
        pend = SimplePendulum(initialAngle = initialAngle, m = m, L = L, g = g, cycles = cycles, step_size = step_size)
        _, theta, omega, _ = pend.non_linear_rk4()
        if plotting:
            plt.plot(theta, omega, label = str(initialAngle) + " degrees")

    if plotting:
        plt.title("Phase Space Plot")
        plt.xlabel(r"$\theta$")
        plt.ylabel(r"$\dot{\theta}$")
        plt.legend()
        plt.show()

    return theta, omega


def momentum(initialAngle, m = 1, L = 1, g = 9.8, cycles = 10, step_size = 0.001, plot_time_theta = False, plot_phase_space = False):
    pend = SimplePendulum(initialAngle = initialAngle, m = m, L = L, cycles = cycles, step_size = step_size)
    time, theta, _, p_theta = pend.non_linear_rk4()
    
    if plot_time_theta:
        plt.title("Variation of momentum with time")
        plt.xlabel("Time (seconds)")
        plt.ylabel(r"$p_{\theta}$")
        plt.plot(time, p_theta)
        plt.show()
    
    if plot_phase_space:
        plt.title("Phase Space Plot")
        plt.xlabel(r"$\theta$")
        plt.ylabel(r"$p_{\theta}$")
        plt.plot(theta, p_theta)
        plt.show()
    
    return p_theta
    

if __name__ == "__main__":
    initialAngles = []
    for element in sys.argv[1:]:
        initialAngles.append(int(element))
    multiple_phase_plot(initialAngles, plotting = True)