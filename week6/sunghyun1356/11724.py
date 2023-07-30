import sys
input = sys.stdin.readline
from collections import deque

# 만약에 check된거면 연결된거니까 bfs돌려서 연결된거 모두다 빼주고 아니면 count+1해준다

def BFS(a):
    q = deque()
    q.append(a)
    check[a] = True
    while q:
        current = q.popleft()
        for i in connect[current]:
            if not check[i]:
                check[i] = True
                q.append(i)

N, M = map(int, input().split())

connect = [[] for _ in range(N + 1)]
check = [False] * (N + 1)

for i in range(M):
    first, second = map(int, input().split())
    connect[first].append(second)
    connect[second].append(first)

count = 0

for i in range(1, N + 1):
    if not check[i]:
        if not connect[i]:
            count += 1
            check[i] = True
        else:
            BFS(i)
            count += 1

print(count)
