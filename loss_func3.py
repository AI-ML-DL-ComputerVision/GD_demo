import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 6, 141)
y = (x - 2.5) ** 2 - 1
plt.plot(x ,y)
plt.show()
def dj(theta):
    return 2 * (theta - 2.5)
def J(theta):
    return (theta-2.5) ** 2 - 1

theta = 0.0
epsilon = 1e-8
eta = 0.1
theta_history = []

def gradient_descent(initial_theta, eta, epsilon=1e-8):
    theta = initial_theta
    theta_history.append(initial_theta)

    while True:
        gradient = dj(theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)

        if (abs(J(theta) - J(last_theta)) < epsilon):
            break

def plot_theta_history():
    plt.plot(x, J(x))
    plt.plot(np.array(theta_history), J(np.array(theta_history)), 'r', marker='+')
    plt.show()

eta = 1.1
theta_history = []
gradient_descent(0., eta)
plot_theta_history()
len(theta_history)