import sys
input = sys.stdin.readline

# 특정한 것을 찾는것은 DFS으로 구현하자

n = int(input())

connect = [[] for _ in range(n+1)]

first, second = map(int, input().split())

sachon = int(input())
for i in range(sachon):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

check = [ 0 for _ in range(n+1)]

def DFS(a):
    for i in connect[a]:
        if check[i] == 0:
            check[i] = check[a] +1
            DFS(i)

DFS(first)
print(check[second]  if check[second]>0 else -1)