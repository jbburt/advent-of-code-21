"""
https://adventofcode.com/2021/day/11
"""
import numpy as np
from scipy.signal import convolve2d

with open('day-11/input.txt', 'r') as fp:
    energy = np.array([list(map(int, line)) for line in fp.read().split('\n')])
tmp = energy.copy()

# neighbor kernel
kernel = np.ones((3, 3), dtype=int)
kernel[1, 1] = 0

nflash = 0
for step in range(100):
    flashed_this_step = np.zeros(energy.shape, dtype=int)
    energy += 1
    flashed = energy > 9
    while flashed.any():
        flashed_this_step[flashed] = 1
        nflash += flashed.sum()  # increment counter
        energy[flashed] = 0  # reset energy
        n_adjacent_flashes = convolve2d(flashed, kernel, mode='same').astype(int)
        energy += n_adjacent_flashes * np.logical_not(flashed_this_step).astype(int)
        flashed = energy > 9

print(f'problem 1: {nflash}')

energy = tmp.copy()
step = 0
while True:
    flashed_this_step = np.zeros(energy.shape, dtype=int)
    energy += 1
    flashed = energy > 9
    step += 1
    if flashed.all():
        break
    while flashed.any():
        flashed_this_step[flashed] = 1
        nflash += flashed.sum()  # increment counter
        energy[flashed] = 0  # reset energy
        n_adjacent_flashes = convolve2d(flashed, kernel, mode='same').astype(int)
        energy += n_adjacent_flashes * np.logical_not(flashed_this_step).astype(int)
        flashed = energy > 9
    if flashed_this_step.all():
        break
print(f'problem 2: {step}')
