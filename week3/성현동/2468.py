import sys
import itertools

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def calc_sink(height, rain):
    sink = [[False] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if rain >= height[i][j]:
                sink[i][j] = True
    return sink


def dfs(x, y):
    if x < 0 or x >= size or y < 0 or y >= size:
        return
    if visited[x][y] or sink_result[x][y]:
        return

    visited[x][y] = True

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


size = int(input())
height = [[0] * size for _ in range(size)]
for i in range(size):
    height[i] = [int(h) for h in input().strip().split()]

connected_cnt = []
max_rain = max(list(itertools.chain(*height)))
for rain in range(0, max_rain+1):
    sink_result = calc_sink(height, rain)
    visited = [[False] * size for _ in range(size)]

    num_islands = 0
    for i in range(size):
        for j in range(size):
            if not sink_result[i][j] and not visited[i][j]:
                num_islands += 1
                dfs(i, j)
    connected_cnt.append(num_islands)

if len(connected_cnt) != 0:
    print(max(connected_cnt))
else:
    print(0)
