#2960
n, k = map(int, input().split())
visited = [False for num in range(n + 1)]

step = 2
cnt = 0
for i in range(2, n + 1):
    if visited[i]:
        continue
    for j in range(i, n + 1, i):
        if visited[j]:
            continue
        visited[j] = True
        cnt += 1
        if cnt == k:
            print(j)
            exit(0)
