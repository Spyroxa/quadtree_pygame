from __future__ import annotations
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.__hg = hg
        self.__hd = hd
        self.__bd = bd
        self.__bg = bg


    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        if isinstance(self.hg, QuadTree):
            return 1 + self.hg.depth  # Vous pouvez prendre n'importe quel fils, tous auront la même profondeur
        else:
            return 1



    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, 'r') as file:
            content = file.read().strip()  # Assuming the file contains a formatted representation of the QuadTree
        return QuadTree._fromString(content)



    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        pass

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        if isinstance(self.hg, QuadTree):
            return f"Q[{self.hg.paint()},{self.hd.paint()},{self.bg.paint()},{self.bd.paint()}]"
        else:
            return "B" if self.hg else "W"

@property
def hg(self):
        return self.__hg

@property
def hd(self):
        return self.__hd

@property
def bd(self):
        return self.__bd

@property
def bg(self):
        return self.__bg