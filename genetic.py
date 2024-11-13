import random

from game import Game
from neural import forward

from concurrent.futures import ThreadPoolExecutor


def randomNumber(times: int = 32) -> list[int]:
    return [0 if random.random() > 0.5 else 1 for _ in range(times + 2)]


def initParameter(shape: list[int], times: int = 32) -> list[tuple[list[list[list[int]]], list[list[int]]]]:
    return [
        (
            [[randomNumber(times) for _ in range(shape[index + 1])] for _ in range(value)],
            [randomNumber(times) for _ in range(shape[index + 1])]
        )
        for index, value in enumerate(shape[:-1])
    ]


def initParameters(shape: list[int], times: int = 32) -> list[list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return [initParameter(shape, times) for _ in range(100)]


def predict(shape: list[int], parameter: list[tuple[list[list[list[int]]], list[list[int]]]]) -> (
        int, (int, int), list[tuple[list[list[list[int]]], list[list[int]]]]):
    game = Game((4, 4))
    while game.isContinue():
        direct = forward(game.getPanel(), parameter, shape)
        if direct == 0:
            game.move("left")
        elif direct == 1:
            game.move("right")
        elif direct == 2:
            game.move("up")
        elif direct == 3:
            game.move("down")
        # game.print()
        if random.random() < 0.01:
            direct = int(random.random() * 4)
            if direct == 0 or direct == 4:
                game.move("left")
            elif direct == 1:
                game.move("right")
            elif direct == 2:
                game.move("up")
            elif direct == 3:
                game.move("down")
            # game.print()
    # print(f"score = {game.score}\t step = {game.step}\n", "-" * 100)
    return game.score, (game.score, game.step), parameter


def predictMore(shape: list[int], parameter: list[tuple[list[list[list[int]]], list[list[int]]]], times: int = 5):
    with ThreadPoolExecutor() as executor:
        predictList = list(executor.map(lambda x: predict(shape, parameter), range(times)))
    loss, score, step = 0, 0, 0
    for i in predictList:
        loss += i[0]
        score += i[1][0]
        step += i[1][1]
    loss, score, step = loss / times, score / times, step / times
    return score, (score, step), parameter


def predictParameter(shape: list[int], parameter: list[list[tuple[list[list[list[int]]], list[list[int]]]]]):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda x: predictMore(x[0], x[1]), [(shape, w) for w in parameter]))


def evaluate(shape: list[int], parameters: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> {str: float}:
    loss, score, step = 0, 0, 0
    n = len(parameters)
    for i in predictParameter(shape, parameters):
        loss += i[0]
        score += i[1][0]
        step += i[1][1]
    return {"loss": loss / n, "score": score / n, "step": step / n}


def select(shape: list[int], weights: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    with ThreadPoolExecutor(max_workers=100) as executor:
        predictParas = list(executor.map(lambda x: predictMore(x[0], x[1]), [(shape, w) for w in weights]))
    return [i[2] for i in sorted(predictParas, key=lambda x: x[0])[-8:]] + [random.choice(weights),
                                                                            initParameter(shape)]


def intersectWeight(numberA: list[int], numberB: list[int]) -> list[int]:
    return [a if random.random() > 0.5 else b for a, b in zip(numberA, numberB)]


def intersect(weights: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return weights + [[(
        [[intersectWeight(a31, b31) for a31, b31 in zip(a21, b21)] for a21, b21 in zip(a1[0], b1[0])],
        [intersectWeight(a22, b22) for a22, b22 in zip(a1[1], b1[1])]
    ) for a1, b1 in zip(a0, b0)] for a0, b0 in zip(weights, weights[::-1])]


def variableOne(i: int) -> int:
    return 0 if i == 1 else 1


def variableWeight(number: list[int]) -> list[int]:
    return [i if i > 0.01 else variableOne(i) for i in number]


def variable(weights: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return weights + [[(
        [[variableWeight(i) for i in i] for i in t[0]],
        [variableWeight(i) for i in t[1]]
    ) for t in i] for i in weights] * 4
