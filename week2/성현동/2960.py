#2960
n, k = map(int, input().split())
visited = [False for num in range(n + 1)]

cnt = 0
for head in range(2, n + 1):
    if visited[head]:
        continue
    for cur in range(head, n + 1, head):
        if visited[cur]:
            continue
        visited[cur] = True
        cnt += 1
        if cnt == k:
            print(cur)
            exit(0)
