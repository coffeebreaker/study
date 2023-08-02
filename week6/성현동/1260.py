from collections import deque, defaultdict


def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            queue.extend(sorted(graph[v] - visited))


def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            stack.extend(sorted(graph[v] - visited, reverse=True))


v_num, e_num, start = map(int, input().split())
graph = defaultdict(set)

for _ in range(e_num):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1].add(vertex2)
    graph[vertex2].add(vertex1)

dfs(start)
print()
bfs(start)
