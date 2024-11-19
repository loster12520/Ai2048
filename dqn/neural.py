from random import random
from typing import Tuple

import numpy as np
from numpy import ndarray


def initParameter(shapes: list[int]):
    return [(np.zeros(value,shapes[index+1]),np.zeros(shapes[index+1])) for index, value in enumerate(shapes[:-1])]

def sigmoid(X: np.ndarray) -> np.ndarray:
    return 1/(1+np.exp(-X))


def relu(X: np.ndarray) -> np.ndarray:
    return np.maximum(0, X)


def relu_backward(dA, cache):

    Z = cache
    dZ = np.array(dA, copy=True)

    dZ[Z <= 0] = 0

    assert (dZ.shape == Z.shape)

    return dZ


def sigmoid_backward(dA, cache):

    Z = cache

    s = 1 / (1 + np.exp(-Z))
    dZ = dA * s * (1 - s)

    assert (dZ.shape == Z.shape)

    return dZ


def prev(A_prev: np.ndarray, W: np.ndarray, b: np.ndarray, activate: str) -> (np.ndarray,()):
    Z = np.dot(A_prev, W) + b
    if activate == 'relu':
        A = relu(Z)
    elif activate == 'sigmoid':
        A = sigmoid(Z)
    else:
        A = Z
    return A, (A_prev, W, b, Z)


def forward(X: np.ndarray, parameters: list[Tuple[ndarray, ndarray]], shape: list[int]) -> int:
    A = np.array(X)
    A = A.reshape(1, -1)
    L = len(shape)
    caches = []
    for i in range(L - 2):
        W, b = parameters[i]
        A, cache = prev(A, W, b, activate='relu')
        caches.append(cache)
    W, b = parameters[L - 2]
    AL, cache = prev(A, W, b, activate='sigmoid')
    caches.append(cache)
    res = roulette_selection(AL)
    return res


def roulette_selection(weights):
    counter = 0
    for i in weights[0]:
        counter += i
    random_num = random() * counter
    count = 0
    for index, value in enumerate(weights[0]):
        if (value + count) > random_num:
            return index
        else:
            count += value
    return 0
