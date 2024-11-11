import random

from game import Game
from neural import forward


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


def predict(shape: list[int], parameter: list[tuple[list[list[list[int]]], list[list[int]]]]) -> (int, (int, int)):
    game = Game((4, 4))
    count = 0
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
        count += 1
        if count > 2:
            break
    # print(f"score = {game.score}\tstep = {game.step}\n", "-" * 100)
    return game.score / game.step, (game.score, game.step)


def predictParameters(shape: list[int], parameters: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> list[
    (int, (int, int))]:
    return [predict(shape, parameter) for parameter in parameters]


def evaluate(shape: list[int], parameters: list[list[tuple[list[list[list[int]]], list[list[int]]]]]) -> {str: float}:
    loss, score, step = 0
    n = len(parameters)
    for i in parameters:
        loss += i[0]
        score += i[1][0]
        step += i[1][1]
    return {"loss": loss / n, "score": score / n, "step": step / n}


def select(shape: list[int], weights: list[list[tuple[list[list[list[int]]]], list[list[int]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return sorted(weights, key=lambda x: predict(shape, x))[0][:9] + [random.choice(weights)]


def intersectWeight(numberA: list[int], numberB: list[int]) -> list[int]:
    return [a if random.random() > 0.5 else b for a, b in zip(numberA, numberB)]


def intersect(weights: list[list[tuple[list[list[list[int]]]], list[list[int]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return weights + [[(
        [[intersectWeight(a, b) for a, b in zip(a, b)] for a, b in zip(a[0], b[0])],
        [intersectWeight(a, b) for a, b in zip(a[1], b[1])]
    ) for a, b in zip(a, b)] for a, b in zip(weights, weights[::-1])]


def variableOne(i: int) -> int:
    return 0 if i == 1 else 1


def variableWeight(number: list[int]) -> list[int]:
    return [i if i > 0.01 else variableOne(i) for i in number]


def variable(weights: list[list[tuple[list[list[list[int]]]], list[list[int]]]]) -> list[
    list[tuple[list[list[list[int]]], list[list[int]]]]]:
    return weights + [[(
        [[variableWeight(i) for i in i] for i in i[0]],
        [variableWeight(i) for i in i[1]]
    ) for i in i] for i in weights] * 4
