import numpy as np

def gradient_descent(X, y, learning_rate, num_iterations):
    theta=np.zeros(X.shape[1])
    k=len(y)

    for i in range (num_iterations):
        predict =np.dot(X,theta)
        error= predict-y
        gradient= (1/k)*np.dot(X.T,error)
        theta=theta-learning_rate*gradient
    return theta

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])

y = np.array([2, 3, 4, 5])
learning_rate = 0.1
num_iteration = 1200

theta = gradient_descent(X, y, learning_rate, num_iteration)
print("Final Theta:", theta)