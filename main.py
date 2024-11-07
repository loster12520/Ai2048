from game import Game
from genetic import initParameter
from neural import forward

if __name__ == '__main__':
    shape = [16, 20, 30, 50, 40, 25, 10, 4]
    parameter = initParameter(shape)
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
        game.print()
    print(f"score = {game.score}\nstep = {game.step}")