import pickle
import time

from genetic import initParameters, select, intersect, variable, evaluate
from line_profiler import LineProfiler


def train(shape, weights):
    for i in range(10000):
        print(f"start the {i} round of training")
        if i < 5:
            startTime = time.time()
        weights = select(shape, weights)
        if i < 5:
            print(f"select successful in ${time.time() - startTime} seconds")
        weights = intersect(weights)
        weights = variable(weights)
        if i % 10 == 0:
            evaluateRes = evaluate(shape, weights)
            print(
                f"{i}次效果如下: loss = {evaluateRes['loss']}, score = {evaluateRes['score']}, step = {evaluateRes['step']}")
            with open(f"output/lastest.pkl", "wb") as file:
                pickle.dump(weights, file)
    evaluateRes = evaluate(shape, weights)
    print(evaluateRes['loss'], evaluateRes['score'], evaluateRes['step'])


def start():
    shape = [16, 20, 10, 4]
    weights = initParameters(shape)
    print("init successful")
    train(shape, weights)


def continueTrain():
    shape = [16, 20, 10, 4]
    weights = initParameters(shape)
    with open(f"output/lastest.pkl", "rb") as file:
        weights = pickle.load(file)
    train(shape, weights)


if __name__ == '__main__':
    continueTrain()

    # profiler = LineProfiler()
    # profiler.add_function(start)
    # profiler.run('start()')
    # profiler.print_stats()
