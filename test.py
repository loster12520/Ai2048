from line_profiler import LineProfiler

import game
from genetic import predict, initParameter, predictMore
from neural import forward, prev, roulette_selection

if __name__ == '__main__':
    shape = [16, 20, 10, 4]
    profiler = LineProfiler()
    profiler.add_function(predict)
    profiler.add_function(forward)
    profiler.add_function(game.Game.move)
    profiler.add_function(prev)
    profiler.add_function(roulette_selection)
    profiler.run('predict(shape, initParameter(shape))')
    profiler.print_stats()
