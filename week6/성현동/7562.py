import sys
from collections import deque

input = sys.stdin.readline
dir = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


def bfs(i_y, i_x):
    visited = [[False] * size for _ in range(size)]
    q = deque()
    q.append((i_y, i_x, 0))
    while q:
        y, x, move = q.popleft()
        for dx, dy in dir:
            new_y, new_x = y + dy, x + dx
            if new_x < 0 or new_x >= size or new_y < 0 or new_y >= size:
                continue
            if new_x == aim_x and new_y == aim_y:
                return move + 1
            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append((new_y, new_x, move + 1))


case_num = int(input())
for _ in range(case_num):
    size = int(input())
    cur_y, cur_x = map(int, input().split())
    aim_y, aim_x = map(int, input().split())
    if cur_x == aim_x and cur_y == aim_y:
        print(0)
    else:
        print(bfs(cur_y, cur_x))
