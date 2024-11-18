from line_profiler import LineProfiler

import game
from genetic import predict, initParameter, predictMore
from neural import forward, prev, roulette_selection

if __name__ == '__main__':
    shape = [16, 20, 10, 4]
    profiler = LineProfiler()
    profiler.add_function(predictMore)
    profiler.run('predictMore(shape, initParameter(shape))')
    profiler.print_stats()
