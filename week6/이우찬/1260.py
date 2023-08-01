#실버2
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 1 2 3 4 5
# 2 4 4 
# 3
# 4

# 1 2 3 4 5
# 2 1 1 3 2
# 3 5 4 5 4

#dfs
# V에서 시작
def dfs(V):
    dfs_res.append(V)
    visited[V] = True
    for i in range(len(dots[V])):
        if visited[dots[V][i]]==False:
            dfs(dots[V][i])

def bfs(V):
    q = []
    q.append(V)
    bfs_res.append(V)
    visited[V] = True

    while q :
        V = q.pop(0)
        for i in range(len(dots[V])):
            if visited[dots[V][i]]==False :
                q.append(dots[V][i])
                bfs_res.append(dots[V][i])
                visited[dots[V][i]] = True

#input
N, M, V = map(int, input().split())

dots = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    dots[a].append(b)
    dots[b].append(a)
for i in range(N+1):
    dots[i].sort()

dfs_res = []
bfs_res = []
visited = [False] * (N+1)

dfs(V)
visited = [False] * (N+1)
bfs(V)

print(*dfs_res)
print(*bfs_res)