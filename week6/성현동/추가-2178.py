from collections import deque

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

row, col = map(int, input().split())
maze = [[0] * col for _ in range(row)]
for i in range(row):
    maze[i] = [int(n) for n in input()]

q = deque([(0, 0, 0)])
visited = [[False] * col for _ in range(row)]
visited[0][0] = True
while q:
    y, x, moved = q.popleft()
    if y == row - 1 and x == col - 1:
        print(moved + 1)
        exit()

    for dy, dx in dir:
        new_y, new_x = y + dy, x + dx
        if new_y >= row or new_y < 0 or new_x >= col or new_x < 0:
            continue
        if maze[new_y][new_x] == 0:
            continue
        if not visited[new_y][new_x]:
            visited[new_y][new_x] = True
            q.append((new_y, new_x, moved + 1))
