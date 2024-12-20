from random import random
from typing import Tuple

import numpy as np
from numpy import ndarray


def sigmoid(X: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-np.clip(X / 1e15, -709, 709)))


def relu(X: np.ndarray) -> np.ndarray:
    return np.maximum(X / 100, X)


def prev(A_prev: np.ndarray, W: np.ndarray, b: np.ndarray, activate: str) -> np.ndarray:
    Z = np.dot(A_prev, W) + b
    if activate == 'relu':
        A = relu(Z)
    elif activate == 'sigmoid':
        A = sigmoid(Z)
    else:
        A = Z
    return A


def forward(X: np.ndarray, parameters: list[Tuple[ndarray, ndarray]], shape: list[int]) -> int:
    A = np.array(X)
    A = A.reshape(1, -1)
    L = len(shape)
    for i in range(L - 2):
        W, b = parameters[i]
        A = prev(A, W, b, activate='relu')
    W, b = parameters[L - 2]
    AL = prev(A, W, b, activate='sigmoid')
    res = roulette_selection(AL)
    return res


def coding(number: float, times: int = 32) -> list[int]:
    res = []
    # 判断是否为负
    if number < 0:
        res.append(0)
        number = -number
    else:
        res.append(1)

    # 判断是否大于1
    if number > 1:
        res.append(1)
        number = 1 / number
    else:
        res.append(0)

    print(bin(int(number * (2 ** times)))[2:].zfill(times))
    print(bin(int(number * (2 ** times))))

    [res.append(int(bit)) for bit in bin(int(number * (2 ** times)))[2:].zfill(times)]

    return res


def uncoding(codingList: list[int], times: int = 32) -> float:
    return (int("".join(str(c) for c in codingList[2:]), 2) / (2 ** times) * (-1 if codingList[0] == 0 else 1)) ** (
        -1 if codingList[1] == 1 else 1)


def uncodingParameter(parameters: list[Tuple[list[list[list[int]]], list[list[int]]]]) -> list[Tuple[ndarray, ndarray]]:
    return [(np.array([[uncoding(item) for item in col] for col in W]), np.array([uncoding(item) for item in b])) for
            W, b in parameters]


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
