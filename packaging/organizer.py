from time import time

from packaging.constants import Axis
from packaging.package import *
from packaging.article import *
from random import random, seed

START_POSITION = [0, 0, 0]


class Organizer:
    packages = []
    articles = []
    bins = []
    costs: float

    def example(self):

        self.add_bin(Package(1111, 11.5, 6.125, 0.25, 3))
        self.add_bin(Package(1112, 15.0, 12.0, 0.75, 5))
        self.add_bin(Package(1113, 8.625, 5.375, 1.625, 3))
        self.add_bin(Package(1114, 11.0, 8.5, 5.5, 4))
        self.add_bin(Package(1115, 13.625, 11.875, 3.375, 5))
        self.add_bin(Package(1116, 12.0, 12.0, 5.5, 5))
        self.add_bin(Package(1117, 23.6875, 11.75, 3.0, 4))
        self.add_bin(Package(1118, 10, 20, 15, 10))
        self.add_bin(Package(1119, 10, 10, 10, 5))

        seed(10)

        for i in range(20):
            self.add_item(Article(i, random() * 12, random() * 12, random() * 5))
        print("for END")
        start = time()
        self.pack()
        dt = time() - start

        for b in self.packages:
            print("============", b.string())

            print("ITEMS:")
            for item in b.items:
                print("====> ", item.string())

            print("#########################")

        print(dt)

    def add_bin(self, bin):
        return self.bins.append(bin)

    def add_item(self, item):
        return self.articles.append(item)

    def pack_to_bin(self, bin, item):
        fitted = False

        if not bin.items:
            response = bin.put_item(item, START_POSITION)

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

        return fitted

    # items bereits sortiert
    def testbin(self, bin, items: []):
        rest = []
        fit = False

        for item in items:
            if (self.pack_to_bin(bin, item.copy())):
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
            if (fit):
                if (costs > bin.cost or not packs):
                    costs = bin.cost
                    packs = [bin]
        return packs, costs

    def pack(self, bigger_first=True, distribute_items=True):

        self.bins.sort(
            key=lambda bin: (bin.get_volume() / bin.cost), reverse=bigger_first
        )
        self.articles.sort(
            key=lambda item: item.get_volume(), reverse=bigger_first
        )

        self.packages, self.costs = self.test(self.bins, self.articles, 0)

        usedpack = []
        usedarticle = []

        for p in self.packages:
            usedpack.append(p.id)
            usedarticle.extend(p.items)

        usedarticle.sort(
            key=lambda item: item.id
        )

        anothernewlist = []
        for a in usedarticle:
            anothernewlist.append([a.pid, a.position[0], a.position[1], a.position[2]])
        return usedpack, anothernewlist
