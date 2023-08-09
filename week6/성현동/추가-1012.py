from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def calc_worm(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if not (0 <= new_y < row and 0 <= new_x < col):
                continue
            if not visited[new_y][new_x] and field[y][x] == 1:
                visited[new_y][new_x] = True
                q.append((new_y, new_x))


for _ in range(int(input())):
    col, row, planted = map(int, input().split())
    field = [[0] * col for _ in range(row)]
    for _ in range(planted):
        x, y = map(int, input().split())
        field[y][x] = 1

    visited = [[False] * col for _ in range(row)]
    cnt = 0
    for y in range(row):
        for x in range(col):
            if not visited[y][x] and field[y][x] == 1:
                calc_worm(y, x)
                cnt += 1
    print(cnt)
