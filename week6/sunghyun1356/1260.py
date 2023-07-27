import sys
from collections import deque

max = 10000

input = sys.stdin.readline
N, M, V = map(int, input().split())

#2차원 배열로 만들어서 graph를 생성해준다
d_graph = [[] for _ in range(max)]
b_graph = [[] for _ in range(max)]

d_check = [False] * max
b_check = [False] * max


for _ in range(M):
    first, end = map(int, input().split())

    d_graph[first].append(end)
    d_graph[end].append(first)

    b_graph[first].append(end)
    b_graph[end].append(first)

for i in range(1, N + 1):
    b_graph[i].sort()
    d_graph[i].sort()


def DFS(a):
    # 스택에 첫번쨰 꺼를 넣어준다
    d_stack = [a]
    # 사용한건 TRUE로 만들어준다
    d_check[a] = True
    print(a, end=" ")
    while d_stack:
        current = d_stack.pop()
        #맨 마지막것을 가져오고
        for next_node in d_graph[current]:
            #현재것에서 다음으로 이거지는 애들을 검사한다
            if not d_check[next_node]:
                # 만약 그놈이 False 즉, 사용되지 않았더라면
                # 출력해주고
                print(next_node, end=" ")
                d_check[next_node] = True
                #사용했다고 해주고
                # current와 next를 넣어준다 -> 왜냐면 하나를 쭉 팔것이기 때문
                d_stack.append(current)
                d_stack.append(next_node)
                break


def BFS(a):
    q = deque([a])
    b_check[a] = True
    while q:
        x = q.popleft()
        print(x, end=" ")
        for y in b_graph[x]:
            if not b_check[y]:
                q.append(y)
                b_check[y] = True
                # 여기서 dfs랑 다른점은 넓이로 여러가지를 이동하면서 할것이기 떄문


DFS(V)
print()
BFS(V)
