class Article:
    id: int
    width: float
    height: float
    depth: float
    position = []
    pid: int

    def __init__(self, id: int, x: float, y: float, z: float):
        self.id = id
        self.width = x
        self.depth = y
        self.height = z
        self.position = []
        self.pid = -1

    def string(self):
        return "%s(%sx%sx%s) pos(%s) vol(%s)" % (
            self.id, self.width, self.depth, self.height,
            self.position, self.get_volume()
        )

    def get_volume(self):
        return self.width * self.height * self.depth

    def get_dimension(self):
        return [self.width, self.depth, self.height]

    def copy(self):
        return Article(self.id, self.width, self.depth, self.height)
