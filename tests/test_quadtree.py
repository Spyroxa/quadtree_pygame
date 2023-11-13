
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
import pytest
from src import QuadTree, TkQuadTree
import tkinter as tk
@pytest.fixture
def tk_root():
    root = tk.Tk()
    yield root
    #root.destroy()
def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 4

def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1


def test_create():
    # Test creating a QuadTree from a list of data
    data = [
        [0, 0, 0, [0, 1, 0, 0]],
        [0, 0, [1, 0, 0, 0], 0],
        [0, 0, 0, [0, 1, 0, 0]],
        [0, 0, [0, 1, 0, 0], 0]
    ]
    quadtree = QuadTree.fromList(data)
    assert quadtree.depth == 3

def test_visualization(tk_root):
    # Test visualization
    quad_tree = TkQuadTree(master=tk_root, hg=True, hd=False, bd=False, bg=True)
    tk_root.update_idletasks()

    # Create image
    tk_root.after(500, lambda: tk_root.destroy())
    tk_root.mainloop()

def test_quadtree_easy(tk_root):
    # Test draw quadtree_easy
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    quad_tree = TkQuadTree(master=tk_root, hg=q.hg, hd=q.hd, bd=q.bd, bg=q.bg)
    tk_root.update_idletasks()
    tk_root.after(500, lambda: tk_root.destroy())
    tk_root.mainloop()

def test_quadtree(tk_root):
    # Test draw quadtree
    filename = "files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    quad_tree = TkQuadTree(master=tk_root, hg=q.hg, hd=q.hd, bd=q.bd, bg=q.bg)
    tk_root.update_idletasks()
    tk_root.after(500, lambda: tk_root.destroy())
    tk_root.mainloop()

def test_create_from_data(tk_root):
    # Test draw from a new data created
    data = [
        [0, 0, 0, [0, 1, 0, 0]],
        [0, 0, [1, 0, 0, 0], 0],
        [0, 0, 0, [0, 1, 0, 0]],
        [0, 0, [0, 1, 0, 0], 0]
    ]
    q = QuadTree.fromList(data)
    quad_tree = TkQuadTree(master=tk_root, hg=q.hg, hd=q.hd, bd=q.bd, bg=q.bg)
    tk_root.update_idletasks()
    tk_root.after(500, lambda: tk_root.destroy())
    tk_root.mainloop()

def test_create_creeper(tk_root):
    # Test draw an quadtree creeper
    data = [
        [0,0,[1,0,0,1],[0,1,1,0]],
        [0,0,[1,0,0,1],[0,1,1,0]],
        [[1,0,1,1],0,0,[1,1,1,0]],
        [0,[0,1,1,1],[1,1,0,1],0]
    ]

    q = QuadTree.fromList(data)
    quad_tree = TkQuadTree(master=tk_root, hg=q.hg, hd=q.hd, bd=q.bd, bg=q.bg)
    tk_root.update_idletasks()
    tk_root.mainloop()