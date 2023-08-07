from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def name_town(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        town_dict[town_id] += 1
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_x < size and 0 <= new_y < size and maps[new_y][new_x] == 1 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append((new_y, new_x))

size = int(input())
maps = [list(map(int, list(input()))) for _ in range(size)]

visited = [[False] * size for _ in range(size)]
town_dict = {}
town_id = 1
for y in range(size):
    for x in range(size):
        if maps[y][x] == 1 and not visited[y][x]:
            town_dict[town_id] = 0
            name_town(y, x)
            town_id += 1

print(len(town_dict))
for value in sorted(town_dict.values()):
    print(value)
