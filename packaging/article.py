from packaging.space import *

from .constants import Axis
from .auxiliary_methods import intersect, set_to_decimal


class Article:
    id: int
    width: float
    height: float
    depth: float
    position = []

    def __init__(self, id: int, x: float, y: float, z: float):
        self.id = id
        self.width = x
        self.depth = y
        self.height = z

    def string(self):
        return "%s(%sx%sx%s) pos(%s) vol(%s)" % (
            self.id, self.width, self.depth, self.height,
            self.position, self.get_volume()
        )

    def get_volume(self):
        return self.width * self.height * self.depth

    def get_dimension(self):
        return [self.width, self.depth, self.height]
