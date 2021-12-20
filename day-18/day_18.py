"""
https://adventofcode.com/2021/day/18
"""
from math import ceil

with open('day-18/input.txt', 'r') as fp:
    lines = list(map(eval, fp.read().strip().split('\n')))


class Node:
    def __init__(self, val, parent, depth):
        self.val = val
        self.parent = parent
        self.depth = depth
        self.left = self.right = None
        if type(val) is int:
            return
        left, right = val
        if not (type(left) is type(right) is int):
            self.val = None
        self.left = Node(left, self, depth+1)
        self.right = Node(right, self, depth+1)

    def split(self):
        lval = int(self.val/2)
        rval = ceil(self.val/2)
        self.val = 0
        self.left = Node(lval, self, self.depth + 1)
        self.right = Node(rval, self, self.depth + 1)

    def flatten(self):
        if not (self.left is None or self.right is None):
            return self.left.flatten() + self.right.flatten()
        if self.left is None and self.right is None:
            return [self]
        if self.left is None:
            return [self.right.flatten()]
        else:
            return [self.left.flatten()]

    def print(self):
        if not (self.left is None or self.right is None):
            return [self.left.print() + self.right.print()]
        if self.left is None and self.right is None:
            return [self.val]
        if self.left is None:
            return [self.right.print()]
        else:
            return [self.left.print()]

    def increment(self, val):
        self.val += val

    def update(self, val):
        self.val = val


def pprint(line):
    print("".join(str(x) for x in line))


def reduce(tree):
    nodes = tree.flatten()
    # search for exploding pair
    exploded = False
    for i, node in enumerate(nodes):
        if node.depth == 5 and i < len(nodes)-1 and nodes[i+1].depth == 5:
            exploded = True
            if i:  # increment left number
                nodes[i-1].increment(node.val)
            if i < len(nodes) - 2:  # increment right number
                nodes[i+2].increment(nodes[i+1].val)
            nodes[i].parent.update(0)
            nodes[i].left = None
            nodes[i].right = None
            node.parent.left = node.parent.right = None
            break
    if exploded:
        return reduce(tree)
    # search for split
    split = False
    for i, node in enumerate(nodes):
        if node.val > 9:
            split = True
            node.split()
            break
    if split:
        return reduce(tree)
    return tree


def p1(numbers):
    temp = numbers.copy()
    head = Node(temp.pop(0), None, 0)
    while len(temp):
        new_num = [head.print()[0], temp.pop(0)]
        head = reduce(Node(new_num, None, 0))
    return head.print()[0]


def magnitude(x):
    if type(x) is int:
        return x
    left, right = x
    if type(left) is type(right) is int:
        return 3*left + 2*right
    return magnitude([magnitude(left), magnitude(right)])


print(f'p1: {magnitude(p1(lines))}')

maxnum = 0
for num1 in lines:
    for num2 in lines:
        maxnum = max(maxnum, magnitude(p1([num1, num2])), magnitude(p1([num2, num1])))
print(f'p2: {maxnum}')
