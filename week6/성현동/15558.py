from collections import deque

dest, jump = map(int, input().split())
cells = [[int(cell) for cell in input()] for _ in range(2)]
dir = [[0, 1], [0, -1], [1, jump]]
visited = [[0]*dest for _ in range(2)]

q = deque([(0, 0, 0)])
visited[0][0] = 1
while q:
    line, step, time = q.popleft()
    for d_line, d_step in dir:
        next_line = line ^ d_line
        next_step = step + d_step
        if next_step <= time:
            continue
        if next_step >= dest:
            print(1)
            exit()
        if cells[next_line][next_step] == 0 or visited[next_line][next_step]:
            continue
        visited[next_line][next_step] = 1
        q.append((next_line, next_step, time + 1))

print(0)
