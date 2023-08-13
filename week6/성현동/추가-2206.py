from collections import deque

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
row, col = map(int, input().split())
if row == 1 and col == 1: # 엣지 케이스는 초장에 박살내기!!
    print(1)
    exit(0)
maps = [[int(n) for n in input()] for _ in range(row)]

# 특정 셀을 벽을 부순뒤 도착한 것인지, 부수지않고 도착한 것인지 구분해서 불리언값 관리
# 한 셀에 대해 벽을 부수고 온 경우와 다른 방법으로 벽을 부수지 않고 온 경우가 병존 가능하기 때문
visited = {
    'broken': [[False] * col for _ in range(row)],
    'unbroken': [[False] * col for _ in range(row)]
}
q = deque([(0, 0, 1, False)])
visited['unbroken'][0][0] = True # 항상 진입점 초기화 신경쓰기!!
while q:
    y, x, cnt, broken = q.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < row and 0 <= nx < col):
            continue
        # bfs는 종착점이 큐의 마지막에 삽입된다는 보장이 없으므로
        # 모든 지점을 다 방문해야 하는 문제가 아니면 중간 탈출 시키는 것이 바람직
        if [ny, nx] == [row - 1, col - 1]:
            print(cnt+1) # 종착점도 거리에 포함시키라한 조건 유의
            exit(0)

        if maps[ny][nx] == 1 and not visited['broken'][ny][nx] and not broken:
            # 벽은 뚫지 않고 갈 수 없으므로 무조건 broken
            visited['broken'][ny][nx] = True # 반드시 큐 삽입 전에 방문 처리
            q.append((ny, nx, cnt + 1, True))
        elif maps[ny][nx] == 0:
            # 현재 상태에 맞는 visited를 업데이트
            if broken and not visited['broken'][ny][nx]:
                visited['broken'][ny][nx] = True
                q.append((ny, nx, cnt + 1, True))
            elif not broken and not visited['unbroken'][ny][nx]:
                visited['unbroken'][ny][nx] = True
                q.append((ny, nx, cnt + 1, False))

# 중간탈출을 하지 못하고 큐가 비어서 나왔으면
# 가볼만한 데 다가봤으나 종착지는 못갔다는 뜻이므로 도달불가를 의미
print(-1)
