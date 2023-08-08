from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
col, row = map(int, input().split())
box = [[int(i) for i in input().split()] for _ in range(row)]

q = deque()
unripe_cnt = 0
for i in range(row):
    for j in range(col):
        if box[i][j] == 0:
            unripe_cnt += 1
        elif box[i][j] == 1:
            q.append((i, j, 0))

ripe_cnt = 0
max_time = 0
while q:
    y, x, time = q.popleft()
    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx
        if not (0 <= new_y < row and 0 <= new_x < col) or box[new_y][new_x] != 0:
            continue
        box[new_y][new_x] = 1 # 1이 된 경우 방문됐음을 의미하므로 굳이 visited 별도 선언 불필요
        q.append((new_y, new_x, time + 1))
        ripe_cnt += 1
    if not q:
        # 큐가 비어있지 않은 동안 마지막 원소 처리. 선입선출이기때문에 필연적으로 현재 팝된것이 가장 time 큼
        max_time = time

# 배열 전체를 순회 해야하는 문제는 while문 내에 강제종료 문을 넣지말고
# 큐가 빌 때까지 순회하도록 냅두자
if ripe_cnt == unripe_cnt:
    print(max_time)
elif ripe_cnt < unripe_cnt:
    print(-1)
