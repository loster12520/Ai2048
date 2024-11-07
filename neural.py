import numpy as np

def sigmoid(X):
    return 1/(1+np.exp(-X))

def relu(X):
    return np.maximum(0,X)

def prev(A_prev: np.matrix[float], W: np.matrix[float], b: np.matrix[float], activate: str) -> np.matrix[float]:
    Z = np.dot(W,A_prev) + b
    if activate == 'sigmoid':
        A = sigmoid(Z)
    elif activate == 'relu':
        A = relu(Z)
    return A

