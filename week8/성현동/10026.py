from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(i, j, visited):
    q = deque([(i, j, picture[i][j])])
    while q:
        y, x, color = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < size and 0 <= nx < size and not visited[ny][nx]):
                continue
            nc = picture[ny][nx]
            if nc != color:
                continue
            visited[ny][nx] = True
            q.append((ny, nx, nc))


def transform_color(picture):
    for i in range(size):
        for j in range(size):
            if picture[i][j] == 'G':
                picture[i][j] = 'R'
    return picture


def calculate(mode):
    visited = [[False] * size for _ in range(size)]
    area_cnt = 0
    if mode == 1:
        transform_color(picture)
    for i in range(size):
        for j in range(size):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, visited)
                area_cnt += 1

    return area_cnt


size = int(input())
picture = [[color for color in input()] for _ in range(size)]
for i in range(2):
    print(calculate(i), end=" ")
