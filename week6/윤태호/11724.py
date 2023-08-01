import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for a in adj:
    a.sort()

checked = [False]*(n+1)

def dfs(v):
    checked[v] = True
    for e in adj[v]:
        if not checked[e]:
            dfs(e)

count = 0
for i in range(1, n+1):
    if checked[i]:
        continue

    dfs(i)

    count += 1

print(count)