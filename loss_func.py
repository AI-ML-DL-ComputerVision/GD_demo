import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 6, 141) # Initilize some points in the function
y = (x - 2.5) ** 2 - 1 # y = (theta - 2.5)^2 - 1
plt.plot(x ,y)
plt.show()
def dj(theta):
    return 2 * (theta - 2.5) # 2 (theta - 2.5)
def J(theta): 
    return (theta-2.5) ** 2 - 1

theta = 0.0 # Initialization w set 
epsilon = 1e-8 # threshold
eta = 0.1 # step size 
# ======================== gradient decent ========================
while True:
    gradient = dj(theta)
    last_theta = theta
    theta = theta - eta * gradient

    if (abs(J(theta) - J(last_theta)) < epsilon):
        break
# ========================= gradient decent =========================
print(theta)
print(J(theta))