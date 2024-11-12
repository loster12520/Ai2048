import pickle
import time

from genetic import initParameters, select, intersect, variable, evaluate

if __name__ == '__main__':
    shape = [16, 20, 10, 4]
    weights = initParameters(shape)
    print("init successful")
    for i in range(1000):
        print(f"start the {i} round of training")
        start_time = time.time()
        weights = select(shape, weights)
        print(f"select successful in {time.time() - start_time} seconds")
        weights = intersect(weights)
        print("intersect successful")
        weights = variable(weights)
        print("variable successful")
        if i % 10 == 0:
            evaluateRes = evaluate(shape, weights)
            print(
                f"{i}次效果如下: loss = {evaluateRes['loss']}, score = {evaluateRes['score']}, step = {evaluateRes['step']}")
            with open(f"output/weights{i}.pkl", "wb") as file:
                # noinspection PyTypeChecker
                pickle.dump(weights, file)
    evaluateRes = evaluate(shape, weights)
    print(evaluateRes['loss'], evaluateRes['score'], evaluateRes['step'])
