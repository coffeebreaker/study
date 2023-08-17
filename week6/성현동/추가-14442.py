from collections import deque
import sys

input = sys.stdin.readline
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

row, col, break_max = map(int, input().split())
if row == 1 and col == 1:
    print(1)
    exit(0)
maps = [[int(n) for n in input().strip()] for _ in range(row)]

# visited = [[[False for _ in range(break_max + 1)] for _ in range(col)] for _ in range(row)]
visited = [[float('inf') for _ in range(col)] for _ in range(row)]
q = deque([(0, 0, 0, 1)])
# visited[0][0][0] = True
visited[0][0] = 0
while q:
    y, x, brk_cnt, move_cnt = q.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < row and 0 <= nx < col):
            continue
        if [ny, nx] == [row - 1, col - 1]:
            print(move_cnt + 1)
            exit(0)
        # if maps[ny][nx] == 0 and not visited[ny][nx][brk_cnt]:
        #     visited[ny][nx][brk_cnt] = True
        if maps[ny][nx] == 0 and brk_cnt < visited[ny][nx]:
            visited[ny][nx] = brk_cnt
            q.append((ny, nx, brk_cnt, move_cnt + 1))
        # elif maps[ny][nx] == 1 and brk_cnt < break_max and not visited[ny][nx][brk_cnt + 1]:
        #     visited[ny][nx][brk_cnt + 1] = True
        elif maps[ny][nx] == 1 and brk_cnt < break_max and brk_cnt + 1 < visited[ny][nx]:
            visited[ny][nx] = brk_cnt + 1
            q.append((ny, nx, brk_cnt + 1, move_cnt + 1))

print(-1)
