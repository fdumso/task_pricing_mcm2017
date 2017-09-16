# !/usr/bin/env python3

from math import acos, sin, cos
from random import shuffle


# a and b are two tuples (latitude, longitude)
def centralAngle(a, b):
    return acos(sin(a[0]) * sin(b[0]) + cos(a[0]) * cos(b[0]) * cos(a[1] - b[1]))


class QuadNode(object):
    def __init__(self, key):
        self.key = key
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None


def quadTreeInsert(tree, node):
    if not tree:
        return node
    if node.key[0] < tree.key[0]:
        if node.key[1] < tree.key[1]:
            tree.c1 = quadTreeInsert(tree.c1, node)
        else:
            tree.c2 = quadTreeInsert(tree.c2, node)
    elif node.key[1] < tree.key[1]:
        tree.c3 = quadTreeInsert(tree.c3, node)
    else:
        tree.c4 = quadTreeInsert(tree.c4, node)


def buildQuadTree(data):
    tree = None
    for task in shuffle(data):
        tree = quadTreeInsert(tree, QuadNode((task.latitude, task.longitude)))
    return tree


def queryRange(tree, lower, upper):
    if not tree:
        return []
    return []


# returns the index of the nearest user
def nearestUser(task, users):
    taskcoord = (task.latitude, task.longitude)
    indices = [(centralAngle(taskcoord, (users[i].latitude, users[i].longitude)), i) for i in range(len(users))]
    return min(indices, key=lambda x: x[0])[1]