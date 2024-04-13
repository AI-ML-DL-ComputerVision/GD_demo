import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 6, 141)
y = (x - 2.5) ** 2 - 1
plt.plot(x ,y)
plt.show()
def dj(theta):
    return 2 * (theta - 2.5)
def J(theta):
    try:
        return (theta-2.5) ** 2 - 1
    except:
        return float('inf')

theta = 0.0
epsilon = 1e-8
eta = 0.1
theta_history = []

def gradient_descent(initial_theta, eta, n_iters= 1e4, epsilon=1e-8):
    theta = initial_theta
    theta_history.append(initial_theta)
    
    i_iter = 0


    while i_iter < n_iters:
        gradient = dj(theta)
        # gradient => grad(wi)
        last_theta = theta
        # w = numpy array [w1, w2, w3,..., w100000000]
        # int 
        theta = theta - eta * gradient
        # w1 - grad(w1), w2 - grad(w2)
        # w (numpy array) = w - grad(w)
        theta_history.append(theta)

        if (abs(J(theta) - J(last_theta)) < epsilon):
            break
        i_iter += 1

def plot_theta_history():
    plt.plot(x, J(x))
    plt.plot(np.array(theta_history), J(np.array(theta_history)), 'r', marker='+')
    plt.show()

eta = 1.1
theta_history = []
gradient_descent(0., eta, n_iters=10)
plot_theta_history()
print(theta_history[-1])