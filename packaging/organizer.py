from .constants import Axis
from .auxiliary_methods import intersect, set_to_decimal
from packaging.package import *
from packaging.article import *

START_POSITION = [0, 0, 0]


class Organizer:
    package_types = []
    articles = []
    bins = []

    def solve(self):

        # self.add_bin(Package(1, 11.5, 6.125, 0.25))
        # self.add_bin(Package(2, 15.0, 12.0, 0.75))
        # self.add_bin(Package(3, 8.625, 5.375, 1.625))
        # self.add_bin(Package(4, 11.0, 8.5, 5.5))
        self.add_bin(Package(5, 13.625, 11.875, 3.375))
        # self.add_bin(Package(6, 12.0, 12.0, 5.5))
        # self.add_bin(Package(7, 23.6875, 11.75, 3.0))

        self.add_item(Article(1, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(2, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(3, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(4, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(5, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(6, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(7, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(8, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(9, 7.8740, 3.9370, 1.9685))

        self.pack(bigger_first=True)

        for b in self.bins:
            print(":::::::::::", b.string())

            print("FITTED ITEMS:")
            for item in b.items:
                print("====> ", item.string())

            print("UNFITTED ITEMS:")
            for item in b.unfitted_items:
                print("====> ", item.string())

            print("***************************************************")
            print("***************************************************")

    def add_bin(self, bin):
        return self.bins.append(bin)

    def add_item(self, item):
        return self.articles.append(item)

    def pack_to_bin(self, bin, item):
        fitted = False

        if not bin.items:
            response = bin.put_item(item, START_POSITION)

            if not response:
                bin.unfitted_items.append(item)

            return

        for axis in range(0, 3):
            items_in_bin = bin.items

            for ib in items_in_bin:
                pivot = [0, 0, 0]
                w, d, h = ib.get_dimension()
                if axis == Axis.WIDTH:
                    pivot = [
                        ib.position[0] + w,
                        ib.position[1],
                        ib.position[2]
                    ]
                elif axis == Axis.DEPTH:
                    pivot = [
                        ib.position[0],
                        ib.position[1] + d,
                        ib.position[2]
                    ]
                elif axis == Axis.HEIGHT:
                    pivot = [
                        ib.position[0],
                        ib.position[1],
                        ib.position[2] + h
                    ]

                if bin.put_item(item, pivot):
                    fitted = True
                    break
            if fitted:
                break

        if not fitted:
            bin.unfitted_items.append(item)

    def pack(self, bigger_first=False, distribute_items=False):

        self.bins.sort(
            key=lambda bin: bin.get_volume()/bin., reverse=bigger_first
        )
        self.articles.sort(
            key=lambda item: item.get_volume(), reverse=bigger_first
        )

        for bin in self.bins:
            for item in self.articles:
                self.pack_to_bin(bin, item)

            if distribute_items:
                for item in bin.articles:
                    self.articles.remove(item)
