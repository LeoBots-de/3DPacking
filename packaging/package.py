
from .constants import Axis
from .auxiliary_methods import intersect, set_to_decimal

class Package:
    id: int
    width: float
    height: float
    depth: float
    cost: float
    items = []
    unfitted_items = []

    def __init__(self, id:int, x:float, y:float, z:float, cost:float):
        self.id = id
        self.width = x
        self.depth = y
        self.height = z
        self.cost = cost
        self.items = []
        self.unfitted_items = []


    def string(self):
        return "%s(%sx%sx%s) vol(%s) bbb" % (
             self.id, self.width, self.depth, self.height, self.get_volume()
        )

    def get_volume(self):
        return self.width * self.height * self.depth


    def put_item(self, item, pivot):
        fit = True
        valid_item_position = item.position
        item.position = pivot

        dimension = item.get_dimension()

        if (
                self.width < pivot[0] + dimension[0] or
                self.depth < pivot[1] + dimension[1] or
                self.height < pivot[2] + dimension[2]
        ): return False

        for current_item_in_bin in self.items:
            if intersect(current_item_in_bin, item):
                fit = False
                break

        if fit:
            self.items.append(item)
        if not fit:
            item.position = valid_item_position

        return fit

    def copy(self):
        return Package(self.id, self.width, self.depth, self.height, self.cost)