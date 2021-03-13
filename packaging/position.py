from packaging.space import *


class Position:
    pos = []

    def __init__(self, x: float, y: float, z: float):
        self.pos = [x, y, z]

    @staticmethod
    def convert(space: FreeSpace, pos):
        res = space.pos
        for i in range(len(res.pos)):
            res.pos[i] += pos.pos[i]

        return res
