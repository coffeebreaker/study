from collections import deque

# 2차원 문제번호: 7576

directions = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
col, row, height = map(int, input().split())
box = [[[0] * col for _ in range(row)] for _ in range(height)]

tomato_q = deque()
not_riped = 0
for h in range(height):
    for i in range(row):
        for j, val in enumerate(input().split()):
            val = int(val)
            if val == 1:
                tomato_q.append((h, i, j, 0))
            if val == 0:
                not_riped += 1
            box[h][i][j] = val

if not_riped == 0:
    print(0)
    exit(0)


max_time = 0
while tomato_q:
    h, y, x, time = tomato_q.popleft()
    for dh, dy, dx in directions:
        nh, ny, nx = h + dh, y + dy, x + dx
        if not (0 <= nh < height and 0 <= ny < row and 0 <= nx < col):
            continue
        if box[nh][ny][nx] == 0:
            box[nh][ny][nx] = 1
            tomato_q.append((nh, ny, nx, time + 1))
            not_riped -= 1
    max_time = time

if not_riped == 0:
    print(max_time)
else:
    print(-1)
