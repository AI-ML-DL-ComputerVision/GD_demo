
import numpy as np

def gradient_descent(X, y, learning_rate, num_iterations):
    theta = np.zeros(X.shape[1])
    m = len(y)
    
    # 梯度下降
    for iteration in range(num_iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradient = (1/m) * np.dot(X.T, errors)
        theta = theta - learning_rate * gradient
    return theta

# 测试
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([2, 3, 4, 5])
learning_rate = 0.1
num_iterations = 1000

theta = gradient_descent(X, y, learning_rate, num_iterations)
print("Theta:", theta)