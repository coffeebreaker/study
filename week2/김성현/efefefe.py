import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
map = [list(input().rstrip())for _ in range(2)]
visited = [[False] * n for _ in range(2)]


def bfs():
    q = deque()
    q.append((0,0))
    for i in range(n):
        for j in range(len(q)):
            x,y = q.popleft()
            for nx, ny in (x,y-1), (x,y+1), (not x, y+k):
                if ny >= n :
                    print(1)
                    return
                if ny > i and not visited[nx][ny] and map[nx][ny] =='1':
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    print(nx, ny)
    print(0)

bfs()




