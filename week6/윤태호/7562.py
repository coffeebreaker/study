from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(I, start, end):
    x, y = start
    q = deque([(x, y, 0)])
    visited = [[False]*I for _ in range(I)]

    while q:
        x, y, d = q.popleft()
        if (x, y) == end:
            return d
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < I) and (0 <= ny < I) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))


for _ in range(int(input())):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    print(bfs(I, start, end))
