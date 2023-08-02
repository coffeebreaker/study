#실버2 시간초과남 근데 틀린건 모르겠음
# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 1 2 3 4 5 6
# 2 1 4 3 2 4
# 5 5   6

# 1 2 5
# 3 4 6

import sys
sys.setrecursionlimit(10**6)

def dfs(c,count):
    visited[c] = True
    count[0] += 1
    for i in dots[c]:
        if visited[i]==False:
            count[0] += 1
            dfs(i,count)

N, M = map(int, input().split())

dots = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    dots[a].append(b)
    dots[b].append(a)
for i in range(1, N+1):
    dots[i].sort()

visited = [False] * (N+1)
res = 0

count = [0]
for c in range(1, N+1):
    count[0] = 0 
    if visited[c]==False:
        dfs(c,count)
    if count[0]!=0:
        res += 1

print(res)