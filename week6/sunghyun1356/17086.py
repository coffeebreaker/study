
# 시간초과뜸
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [1, -1, 1, -1, 0, 0, 1, -1]

shark = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            shark.append((i, j))

def BFS(a, b):
    q = deque()
    q.append((a, b))
    visited = [[False] * M for _ in range(N)]
    visited[a][b] = True
    distance = [[-1] * M for _ in range(N)]  
    distance[a][b] = 0  

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

    return distance

max_safety_distance = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:  
            shark_distances = [BFS(shark[k][0], shark[k][1]) for k in range(len(shark))]
            min_distance_from_sharks = min(shark_distances[k][i][j] for k in range(len(shark)))
            max_safety_distance = max(max_safety_distance, min_distance_from_sharks)

print(max_safety_distance)
