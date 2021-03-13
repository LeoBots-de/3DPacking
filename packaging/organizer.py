from .constants import Axis
from .auxiliary_methods import intersect, set_to_decimal
from packaging.package import *
from packaging.article import *
from copy import deepcopy

START_POSITION = [0, 0, 0]


class Organizer:
    packages = []
    articles = []
    bins = []
    costs: float

    def solve(self):

        self.add_bin(Package(1111, 11.5, 6.125, 0.25, 3))
        self.add_bin(Package(2, 15.0, 12.0, 0.75, 5))
        self.add_bin(Package(1113, 8.625, 5.375, 1.625, 3))
        self.add_bin(Package(1114, 11.0, 8.5, 5.5, 4))
        self.add_bin(Package(1115, 13.625, 11.875, 3.375, 5))
        self.add_bin(Package(6, 12.0, 12.0, 5.5, 5))
        self.add_bin(Package(7, 23.6875, 11.75, 3.0, 4))

        self.add_item(Article(1, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(2, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(3, 3.9370, 1.9685, 1.9685))
        self.add_item(Article(4, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(5, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(6, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(7, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(8, 7.8740, 3.9370, 1.9685))
        self.add_item(Article(9, 7.8740, 3.9370, 1.9685))

        self.add_bin(Package(1111, 10, 20, 15, 10))
        self.add_bin(Package(1112, 10, 10, 10, 5))



        self.pack()

        for b in self.packages:
            print(":::::::::::", b.string())

            print("FITTED ITEMS:")
            for item in b.items:
                print("====> ", item.string())

           # print("UNFITTED ITEMS:")
           # for item in b.unfitted_items:
           #     print("====> ", item.string())

            print("***************************************************")
            print("***************************************************")

        # print("SOLLTE LEER SEIN: ------------------------->")
        # for b in self.bins:
        #     print(":::::::::::", b.string())
#
        #     print("FITTED ITEMS:")
        #     for item in b.items:
        #         print("====> ", item.string())
#
        #     print("UNFITTED ITEMS:")
        #     for item in b.unfitted_items:
        #         print("====> ", item.string())
#
        #     print("***************************************************")
        #     print("***************************************************")

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

            return response

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

        return fitted

    # items bereits sortiert
    def testbin(self, bin, items: []):
        rest = []
        fit = False

        for item in items:
            if (self.pack_to_bin(bin, item.copy())):
               # items.remove(item)
                fit = True
            else:
                rest.append(item)
        return fit, rest

    def test(self, bins: [], items: [], pointer: int):
        if (len(bins) <= pointer):
            return [], 0.0
        bin = (bins[pointer]).copy()

        fit, rest = self.testbin(bin, items)

        if (fit and rest):
            packs, costs = self.test(bins, rest, pointer)
            packs.insert(0, bin)
            costs += bin.cost
        else:
            packs, costs = self.test(bins, items, pointer + 1)
            if(fit):
                if(costs>bin.cost or not packs):
                    costs = bin.cost
                    packs = [bin]
        return packs, costs

    def pack(self, bigger_first=True, distribute_items=True):

        self.bins.sort(
            key=lambda bin: bin.get_volume() / bin.cost, reverse=bigger_first
        )
        self.articles.sort(
            key=lambda item: item.get_volume(), reverse=bigger_first
        )

        self.packages, self.costs = self.test(self.bins, self.articles, 0)