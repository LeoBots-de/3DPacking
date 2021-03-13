from packaging import Space


class Article:
    dimensions: Space
    cost: float

    def __init__(self, x: float, y: float, z: float, cost: float):
        dimensions = Space(x, y, z)
        cost = cost