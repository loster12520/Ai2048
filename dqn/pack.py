import collections
import random


class ReplayBuffer:
    def __init__(self, size: int = 20):
        self.list = collections.deque(maxlen=size)

    def append(self, experience):
        self.list.append(experience)

    def replay(self):
        return random.choice(self.list)

