import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def dfs(begin):
    visited[begin] = True
    for neighbor in graph[begin]:
        if not visited[neighbor]:
            dfs(neighbor)


vertex_num, edge_num = map(int, input().split())
graph = [[] for _ in range(vertex_num + 1)]
for _ in range(edge_num):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (vertex_num + 1)
cnt = 0
for vertex in range(1, vertex_num + 1):
    if not visited[vertex]:
        dfs(vertex)
        cnt += 1

print(cnt)
