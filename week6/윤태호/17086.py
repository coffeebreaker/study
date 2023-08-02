import sys
from collections import deque
input = sys.stdin.readline

# input
n, m = map(int, input().split())
space = [list(map(int,input().split())) for _ in range(n)]

# BFS
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y, 0)])

    while q:
        # print(q.popleft())
        x, y, d = q.popleft()
        if space[x][y] == 1:
            return d
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
                
            
max_dist = -1
for i in range(n):
    for j in range(m):
        max_dist = max(max_dist, bfs(i, j))

print(max_dist)