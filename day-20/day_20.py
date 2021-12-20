"""
https://adventofcode.com/2021/day/20
"""

import numpy as np
import scipy.ndimage as ndimage

with open('day-20/input.txt', 'r') as fp:
    algo, image = fp.read().strip().split('\n\n')

algo = np.array(list(algo.replace('\n', '')))


def str2int(c):
    return 0 if c == '.' else 1


# light pixels (#) and dark pixels (.)
str2intvec = np.vectorize(str2int)
image = str2intvec(np.array(list(map(list, image.split('\n')))))
init = image.copy()

mult = 2 ** np.arange(8, -1, -1).astype(int)


def ints2idx(ints):
    return int(np.sum(mult * ints))


def func(x, invert=False):
    return str2int(algo[ints2idx(x if not invert else ~x + 2)])


def simulate(n, input_image):
    pad_val = 0
    for i in range(n):
        input_image = np.pad(
            input_image, pad_width=2, mode='constant', constant_values=pad_val)
        input_image = ndimage.generic_filter(
            input_image, function=func, size=3, origin=0, mode='constant', cval=pad_val)
        pad_val = func(np.array([pad_val] * 9))
    return input_image.sum()


print(f'p1: {simulate(2, image)}')
print(f'p2: {simulate(50, image)}')
