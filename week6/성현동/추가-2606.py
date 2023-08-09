from collections import deque

computer_num = int(input())
# 엣지 정보가 주어지면, 그래프는 딕셔너리로 관리하는게 용이
graph = {i: [] for i in range(1, computer_num + 1)}
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = [False] * (computer_num + 1)
cnt = 0
while q:
    node = q.popleft()
    visited[node] = True
    cnt += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            # 미방문 노드 추가 전 반드시 방문처리할 것!
            # 한 노드가 이 노드보다 먼저 pop된 노드의 neighbor인 경우
            # 중복해서 큐에 추가 되는 현상 발생할 수 있기 때문
            visited[neighbor] = True
            q.append(neighbor)

print(cnt - 1)
