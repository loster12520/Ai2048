from genetic import initParameters, select, intersect, variable, predictParameters

if __name__ == '__main__':
    shape = [16, 20, 30, 50, 40, 25, 10, 4]
    weights = initParameters(shape)
    print("init successful")
    for i in range(1):
        weights = select(shape, weights)
        print("select successful")
        weights = intersect(weights)
        print("intersect successful")
        weights = variable(weights)
        print("variable successful")
        print(len(weights))
        evaluate = evaluate(shape, weights)
        print(evaluate['loss'], evaluate['score'], evaluate['step'])
