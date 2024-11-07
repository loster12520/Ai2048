import random

import numpy as np


class Game:
    def __init__(self, shape):
        self.shape = shape
        self.step = 0
        self.panel = np.zeros(shape, dtype=int)
        self.score = 0
        self.lastPanel = self.panel.copy()
        self.newBlock()

    def move(self, direction):
        self.lastPanel = self.panel.copy()
        if direction == "left":
            for column in range(self.shape[0]):
                queue = []
                for item in self.panel[column]:
                    if item == 0:
                        continue
                    elif len(queue) == 0:
                        queue.append(item)
                    elif item == queue[-1]:
                        queue[-1] = item * 2
                    else:
                        queue.append(item)
                self.panel[column] = np.pad(np.array(queue), (0, self.shape[1] - len(queue)), mode='constant',
                                            constant_values=0)
        elif direction == "right":
            for column in range(self.shape[0]):
                queue = []
                for item in np.flip(self.panel[column]):
                    if item == 0:
                        continue
                    elif len(queue) == 0:
                        queue.insert(0, item)
                    elif item == queue[0]:
                        queue[0] = item * 2
                    else:
                        queue.insert(0, item)
                self.panel[column] = np.pad(np.array(queue), (self.shape[1] - len(queue), 0), mode='constant',
                                            constant_values=0)
        elif direction == "up":
            self.panel = self.panel.T
            for column in range(self.shape[0]):
                queue = []
                for item in self.panel[column]:
                    if item == 0:
                        continue
                    elif len(queue) == 0:
                        queue.append(item)
                    elif item == queue[-1]:
                        queue[-1] = item * 2
                    else:
                        queue.append(item)
                self.panel[column] = np.pad(np.array(queue), (0, self.shape[1] - len(queue)), mode='constant',
                                            constant_values=0)
            self.panel = self.panel.T
        elif direction == "down":
            self.panel = self.panel.T
            for column in range(self.shape[0]):
                queue = []
                for item in np.flip(self.panel[column]):
                    if item == 0:
                        continue
                    elif len(queue) == 0:
                        queue.insert(0, item)
                    elif item == queue[0]:
                        queue[0] = item * 2
                    else:
                        queue.insert(0, item)
                self.panel[column] = np.pad(np.array(queue), (self.shape[1] - len(queue), 0), mode='constant',
                                            constant_values=0)
            self.panel = self.panel.T

        self.step += 1
        self.score = np.sum(self.panel)

        if self.isContinue():
            if not np.array_equal(self.panel, self.lastPanel):
                self.newBlock()
            return self
        else:
            return False

    def isContinue(self):
        panelList = list(self.panel)
        return any(x == 0 for line in panelList for x in line) or any(
            box == panelList[x - 1][y] if x > 0 else False or box == panelList[x][y - 1] if y > 0 else False
            for x, line in enumerate(panelList)
            for y, box in enumerate(line)
        )

    def newBlock(self):
        indexs = np.where(self.panel == 0)
        if len(indexs[0]) == 0:
            return self
        randomIndex = int(len(indexs[0]) * random.random())
        index = (indexs[0][randomIndex], indexs[1][randomIndex])
        self.panel[index[0]][index[1]] = 2 if random.random() < 0.9 else 4
        return self

    def print(self):
        print("-" * 100)
        print(self.panel)
        return self

    def getPanel(self):
        return self.panel.flatten()


if __name__ == "__main__":
    game = Game((4, 4))
