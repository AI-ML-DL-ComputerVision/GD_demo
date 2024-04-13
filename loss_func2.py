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
history_theta = []
while True:
    gradient = dj(theta)
    last_theta = theta
    history_theta.append(theta)
    theta = theta - eta * gradient

    if (abs(J(theta) - J(last_theta)) < epsilon):
        break
plt.plot(x, J(x))
plt.plot(np.array(history_theta), J(np.array(history_theta)), 'r', marker='+')
plt.show()
print("Total steps: ", len(history_theta))