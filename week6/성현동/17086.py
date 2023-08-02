import sys
from collections import deque

input = sys.stdin.readline
dir = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


def bfs():
    max_dist = 0
    # 2차원 배열을 선언해 각 셀마다 안전거리를 저장시키는 방법보다 시공간복잡도 상 효율적
    while queue:
        y, x, dist = queue.popleft()
        if dist > max_dist:
            max_dist = dist
        for dx, dy in dir:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= col or new_y < 0 or new_y >= row:
                continue
            if not visited[new_y][new_x]:
                # 이미 방문했다는 소리는 더 가까운 상어가 방문해 안전거리를 구했다는 의미이므로
                # 더 멀리 있는 상어는 안전거리에 영향을 줄 수 없어서 아래로직에 갈 필요가 없음
                visited[new_y][new_x] = True
                queue.append((new_y, new_x, dist + 1))

    return max_dist


row, col = map(int, input().split())
visited = [[False] * col for _ in range(row)]
queue = deque()
for i in range(row):
    row_values = list(map(int, input().split()))
    for j in range(col):
        if row_values[j] == 1:
            # 상어 발견 즉시 바로 큐 추가하면 별도로 상어위치 저장 불필요
            # 큐는 선입선출이라, 상어 기준 거리가 같은 지점부터 순차적으로 조회해나간다.
            # dfs라면 한 상어 기준으로 갈떄까지 갔을 것..
            # 그럼 "특정셀에 대한 모든 상어로부터의 거리의 최솟값"을 그 셀의 안전거리로 두고자하는 문제정의에 반할 수 있다
            queue.append((i, j, 0))
            visited[i][j] = True  # 상어 위치는 방문한것으로 표시해야 안전거리 계산에 반영x

print(bfs())
