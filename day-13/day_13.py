"""
https://adventofcode.com/2021/day/13
"""
import time

import matplotlib.pyplot as plt
import numpy as np
import pyocr.builders
from PIL import Image

t0 = time.time()

with open('day-13/test_input.txt', 'r') as fp:
    lines = fp.read().split('\n')
    points = list()
    instructions = list()
    for i, line in enumerate(lines):
        if not line:
            break
        points.append([int(i) for i in line.split(',')])
    for j in range(i + 1, len(lines)):
        var, num = lines[j].split()[-1].split('=')
        instructions.append((var, int(num)))

# p1
new_pts = set()
for dim, value in instructions[:1]:
    for x, y in points:
        if dim == 'y':
            y = y if y <= value else value - (y - value)
        else:
            x = x if x <= value else value - (x - value)
        new_pts.add((x, y))
print(f"problem 1: {len(new_pts)}")

# p2
points = set(tuple(x) for x in points)
for dim, value in instructions:
    new_pts = set()
    for x, y in points:
        if dim == 'y':
            y = y if y <= value else value - (y - value)
        else:
            x = x if x <= value else value - (x - value)
        new_pts.add((x, y))
    points = new_pts

# get size of paper after final folds
xfolds = [i for i, x in enumerate(instructions) if x[0] == 'x']
yfolds = [i for i, x in enumerate(instructions) if x[0] == 'y']
width = instructions[xfolds[-1]][1]
height = instructions[yfolds[-1]][1]

# binary grid
grid = np.zeros((height + 2, width + 1))
for x, y in points:
    grid[height - y, x + 1] = 1

# save image with interpolation
fig, ax = plt.subplots(figsize=(width + 1, height + 2))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.imshow(grid, origin='lower', cmap='Greys', interpolation='spline36')
ax.axis('off')
plt.savefig('characters.jpg')
plt.close()

# binarize image
im = Image.open('characters.jpg')
im = im.point(lambda p: p > 220 and 255)
im.save('thresholded.jpg')

# open image and detect chars using pyocr
tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[0]
txt = tool.image_to_string(
    Image.open('thresholded.jpg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)

print(f"problem 2: {txt}")

print(f"time: {time.time() - t0}")
