import random
from typing import Generator, Tuple

import numpy as np


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


def randomNumber(times: int = 32) -> list[int]:
    return [0 if random.random() > 0.5 else 1 for _ in range(times + 2)]


def initParameter(shape: list[int], times: int = 32) -> list[Tuple[list[list[list[int]]], list[list[int]]]]:
    return [
        (
            [[randomNumber(times) for _ in range(shape[index + 1])] for _ in range(value)],
            [randomNumber(times) for _ in range(shape[index + 1])]
        )
            for index, value in enumerate(shape[:-1])
    ]


def roulette_selection(weights):
    # 生成一个随机浮点数
    random_num = np.random.rand() * np.sum(weights)

    # 使用二分查找找到所属的区间
    left, right = 0, len(weights) - 1
    while left <= right:
        mid = (left + right) // 2
        if weights[mid] >= random_num:
            right = mid - 1
        else:
            left = mid + 1

    # 根据找到的区间返回对应的索引
    return left