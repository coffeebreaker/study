from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def calc(i, j):
    if maps[i][j] == 0:
        return 0

    q = deque([(i, j, 0)])
    visited = [[False] * col for _ in range(row)]
    visited[i][j] = True
    while q:
        y, x, dist = q.popleft()
        if maps[y][x] == 2:
            return dist
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if not (0 <= new_y < row and 0 <= new_x < col):
                continue
            if maps[y][x] == 1 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append((new_y, new_x, dist + 1))


row, col = map(int, input().split())
maps = [[int(x) for x in input().split()] for _ in range(row)]
for i in range(row):
    for j in range(col):
        print(calc(i, j), end=' ')
    print()
