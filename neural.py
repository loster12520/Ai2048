import random
from typing import Tuple

import numpy as np

from genetic import uncoding, roulette_selection


def sigmoid(X: np.ndarray) -> np.ndarray:
    return 1/(1+np.exp(-X))

def relu(X: np.ndarray) -> np.ndarray:
    return np.maximum(0, X)

def prev(A_prev: np.matrix[float], W: np.matrix[float], b: np.matrix[float], activate: str) -> np.ndarray:
    Z = np.dot(A_prev, W) + b
    if activate == 'sigmoid':
        A = sigmoid(Z)
    elif activate == 'relu':
        A = relu(Z)
    return A

def forward(X: np.ndarray, parameters: list[Tuple[list[list[list[int]]], list[list[int]]]], shape: list[int]) -> int:
    A = np.array(X)
    A = A.reshape(1, -1)
    L = len(shape)
    for i in range(L - 2):
        W, b = parameters[i]
        W = np.array([[uncoding(item) for item in col] for col in W])
        b = np.array([uncoding(item) for item in b])
        print(f"W.shape = {W.shape}, b.shape = {b.shape} ,A.shape = {A.shape}")
        A = prev(A, W, b, activate='relu')
    W, b = parameters[L - 2]
    W = np.array([[uncoding(item) for item in col] for col in W])
    b = np.array([uncoding(item) for item in b])
    AL = prev(A, W, b, activate='sigmoid')
    res = roulette_selection(AL)
    return res
