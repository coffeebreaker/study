# https://www.acmicpc.net/problem/10026
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
picture_1 = [list(input()) for _ in range(n)]
picture_2 = []

for row in picture_1:
    append_list = []
    for col in row:
        if col == 'G':
            append_list.append('R')
        else:
            append_list.append(col)
    picture_2.append(append_list)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(picture):
    visited = [[0]*n for _ in range(n)]    
    space_num = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                space_num += 1
                visited[i][j] = 1
                color = picture[i][j]

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if (0 <= nx < n) and (0 <= ny < n) and (not visited[nx][ny]) and (picture[nx][ny] == color):
                            visited[nx][ny] = 1
                            q.append([nx, ny])
    # for row in visited:
    #     print(*row)
    return space_num


spot_1 = bfs(picture_1)
spot_2 = bfs(picture_2)

print(spot_1, spot_2)