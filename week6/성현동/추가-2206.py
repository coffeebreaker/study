from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
row, col = map(int, input().split())
if row == 1 and col == 1:
    print(1)
    exit(0)
maps = [[int(n) for n in input()] for _ in range(row)]

visited = {
    'broken': [[False] * col for _ in range(row)],
    'unbroken': [[False] * col for _ in range(row)]
}
q = deque([(0, 0, 1, False)])
visited['unbroken'][0][0] = True
while q:
    y, x, cnt, broken = q.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < row and 0 <= nx < col):
            continue
        if [ny, nx] == [row - 1, col - 1]:
            print(cnt+1)
            exit(0)

        if maps[ny][nx] == 1 and not broken and not visited['broken'][ny][nx]:
            visited['broken'][ny][nx] = True
            q.append((ny, nx, cnt + 1, True))
        elif maps[ny][nx] == 0:
            if broken and not visited['broken'][ny][nx]:
                visited['broken'][ny][nx] = True
                q.append((ny, nx, cnt + 1, True))
            elif not broken and not visited['unbroken'][ny][nx]:
                visited['unbroken'][ny][nx] = True
                q.append((ny, nx, cnt + 1, False))

print(-1)
