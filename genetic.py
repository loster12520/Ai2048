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


def initParameters(shape: list[int], times: int = 32) -> Generator[Tuple[list[list[list[int]]],list[int]],None,None]:
    return (
        ([[randomNumber(times) for _ in range(shape[index + 1])]
         for _ in range(value)], randomNumber(times))
        for index, value in enumerate(shape[:-1])
    )


if __name__ == "__main__":
    times = 32
    shape = [16, 20, 30, 50, 40, 25, 10, 4]
