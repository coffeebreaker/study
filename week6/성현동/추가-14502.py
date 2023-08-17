from collections import deque
from itertools import combinations
import copy

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(comb):
    tmp = copy.deepcopy(maps)
    for i, j in comb:
        tmp[i][j] = 1
    virus_q = deque(virus for virus in virus_place)
    visited = [[False] * col for _ in range(row)]
    infected_cnt = 0
    while virus_q:
        y, x = virus_q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < row and 0 <= nx < col) or visited[ny][nx]:
                continue
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                infected_cnt += 1
                visited[ny][nx] = True
                virus_q.append((ny, nx))
    return infected_cnt


row, col = map(int, input().split())
maps = [[0] * col for _ in range(row)]
zero_place, virus_place = [], []
for i in range(row):
    for j, val in enumerate(input().split()):
        val = int(val)
        if val == 0:
            zero_place.append((i, j))
        if val == 2:
            virus_place.append((i, j))
        maps[i][j] = val

max_safe = 0
init_safe = len(zero_place)
for comb in combinations(zero_place, 3):
    cur_safe = init_safe - (bfs(comb) + 3)
    if cur_safe > max_safe:
        max_safe = cur_safe
print(max_safe)
