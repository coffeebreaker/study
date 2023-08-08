from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def name_town(i, j):
    q = deque([(i, j)])
    town_list.append(0) # 이 함수 들어온 순간 새 마을 진입했음을 의미하므로 바로 새 원소 추가
    visited[i][j] = True # 중요. 시작점도 반드시 방문 처리
    while q:
        y, x = q.popleft()
        town_list[-1] += 1
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if not (0 <= new_x < size and 0 <= new_y < size): # 필수 조건1: 범위 내
                continue
            if maps[new_y][new_x] == 1 and not visited[new_y][new_x]: # 필수조건 2,3: 미방문, 1인 곳
                visited[new_y][new_x] = True
                q.append((new_y, new_x))


size = int(input())
maps = [list(map(int, list(input()))) for _ in range(size)]

visited = [[False] * size for _ in range(size)]
town_list = [] # 마을 번호는 중요하지않으므로 굳이 딕셔너리 불필요
for y in range(size):
    for x in range(size):
        if maps[y][x] == 1 and not visited[y][x]:
            name_town(y, x)

print(len(town_list))
for value in sorted(town_list):
    print(value)
