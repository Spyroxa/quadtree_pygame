from __future__ import annotations
import tkinter as tk
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):

        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg


    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        if not any(isinstance(child, QuadTree) for child in [self.hg, self.hd, self.bd, self.bg]):
            return 1
        else:
            depths = [child.depth if isinstance(child, QuadTree) else 1 for child in
                      [self.hg, self.hd, self.bd, self.bg]]
            return max(depths) + 1


    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, 'r') as file:
            content = file.read().strip()
        return QuadTree._fromString(content)

    @staticmethod
    def _fromString(content: str) -> QuadTree:
        """Method to create a QuadTree from a textual representation"""

        def parse_node(node_data, depth=0):
            if isinstance(node_data, list):
                return QuadTree(*[parse_node(child, depth + 1) for child in node_data])
            else:
                return int(node_data)

        nodes = parse_node(eval(content))
        return nodes

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        return QuadTree._fromString(str(data))


@property
def hg(self):
        return self.hg

@property
def hd(self):
        return self.hd

@property
def bd(self):
        return self.bd

@property
def bg(self):
        return self.bg
class TkQuadTree(QuadTree):

    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.paint()

    def paint(self):
        self.canvas.delete("all")
        self._paint_quadtree(self, 0, 0, 400, 400)


    def _paint_quadtree(self, node, x, y, width, height):
        """Recursively draws the Quadtree on the canvas"""
        if isinstance(node, QuadTree):
            mid_x = x + width / 2
            mid_y = y + height / 2

            self._paint_quadtree(node.hg, x, y, mid_x - x, mid_y - y)
            self._paint_quadtree(node.hd, mid_x, y, width - (mid_x - x), mid_y - y)
            self._paint_quadtree(node.bd, mid_x, mid_y, width - (mid_x - x), height - (mid_y - y))
            self._paint_quadtree(node.bg, x, mid_y, mid_x - x, height - (mid_y - y))
        else:
            color = "black" if node else "green"
            self.canvas.create_rectangle(x, y, x + width, y + height, fill=color)

