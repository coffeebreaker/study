import sys
input = sys.stdin.readline
from collections import deque

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2 ,1, -1, -2, -2, -1]


def BFS(a,b):
    q = deque()
    q.append((a,b))
    
    while q:
        y, x = q.popleft()
        if y == second_y and x == second_x:
            return dp[y][x]-1
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<I and 0<=nx < I and dp[ny][nx]==0 :
                q.append((ny,nx))
                dp[ny][nx] = dp[y][x] +1


            

n =int(input())
for i in range(n):
    I = int(input())
    dp = [[0 for _ in range(I)] for _ in range(I)]
    first_y, first_x = map(int, input().split())
    second_y, second_x = map(int, input().split())
    if first_x == second_x and first_y == second_y:
        print(0)
    else:
        dp[first_y][first_x]=1
        print(BFS(first_y, first_x))

