import numpy as np

def gradient_descent(X, y, learning_rate, num_iterations):
    """
    Perform gradient descent to find the optimal parameters for a linear regression model.
    
    Parameters:
    X : numpy.ndarray
        The input features matrix where each row represents a training example 
        and each column represents a feature. The first column should be all ones to 
        account for the intercept term in the linear model.
    y : numpy.ndarray
        The output/target vector where each element corresponds to the output value 
        for the corresponding training example.
    learning_rate : float
        The learning rate (step size) used in the gradient descent update rule.
    num_iterations : int
        The number of iterations to perform the gradient descent.
        
    Returns:
    numpy.ndarray
        The final parameters (including the intercept) after performing gradient descent.
    """
    
    pass

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])

y = np.array([2, 3, 4, 5])
learning_rate = 0.1
num_iteration = 1000

theta = gradient_descent(X, y, learning_rate, num_iteration)
print("Final Theta:", theta)