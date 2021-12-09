"""
https://adventofcode.com/2021/day/9
"""

with open('day-09/input.txt', 'r') as fp:
    grid = [list(map(int, list(x))) for x in fp.read().split('\n')]

nr = len(grid) - 1
nc = len(grid[0]) - 1


def is_low_point(i, j):
    if j and grid[i][j - 1] <= grid[i][j]:
        return False
    if i and grid[i - 1][j] <= grid[i][j]:
        return False
    if i < nr and grid[i + 1][j] <= grid[i][j]:
        return False
    if j < nc and grid[i][j + 1] <= grid[i][j]:
        return False
    return True


risk = 0
low_points = list()
for ir in range(nr+1):
    for ic in range(nc+1):
        if is_low_point(ir, ic):
            risk += 1 + grid[ir][ic]
            low_points.append((ir, ic))

print(f'problem 1: {risk}')

visited = set(low_points)
sizes = [0] * len(low_points)
for idx, (ly, lx) in enumerate(low_points):
    stack = [(ly, lx)]
    size = 1
    while stack:
        y, x = stack.pop(0)
        for yp, xp in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (yp, xp) not in visited and (0 <= yp <= nr) and (0 <= xp <= nc):
                visited.add((yp, xp))
                if grid[yp][xp] < 9:
                    stack.append((yp, xp))
                    size += 1
    sizes[idx] = size

tot = 1
for _ in range(3):
    biggest = max(sizes)
    tot *= biggest
    sizes.remove(biggest)
print(f"problem 2: {tot}")
