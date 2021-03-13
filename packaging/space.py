from packaging.position import *


class Space:
    dims: []

    def __init__(self, x: float, y: float, z: float):
        self.dims = [x, y, z]

    def space(self):
        s = 1
        for dim in self.dims:
            s *= dim
        return s

    @staticmethod
    def ratio(parent, child, dim: int):
        r = []
        for i in range(len(parent.dims)):
            r.append(child.dims[i] / parent.dims[i])

        r = sorted(r, key=lambda x: max(r[x]), reverse=True)

        res = 1
        for d in range(dim):
            res *= r[d]
        return res


class FreeSpace(Space):
    pos: Position

    def fill(self, s: Space):


        return freespace,position

