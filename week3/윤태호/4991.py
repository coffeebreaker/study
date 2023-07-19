# 문제
# 오늘은 직사각형 모양의 방을 로봇 청소기를 이용해 청소하려고 한다. 이 로봇 청소기는 유저가 직접 경로를 설정할 수 있다.

# 방은 크기가 1×1인 정사각형 칸으로 나누어져 있으며, 로봇 청소기의 크기도 1×1이다.

# 칸은 깨끗한 칸과 더러운 칸으로 나누어져 있으며, 로봇 청소기는 더러운 칸을 방문해서 깨끗한 칸으로 바꿀 수 있다.

# 일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다.

# 로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 또, 로봇은 같은 칸을 여러 번 방문할 수 있다.

# 방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트케이스로 이루어져 있다.

# 각 테스트 케이스의 첫째 줄에는 방의 가로 크기 w와 세로 크기 h가 주어진다. (1 ≤ w, h ≤ 20) 둘째 줄부터 h개의 줄에는 방의 정보가 주어진다.

# 방의 정보는 4가지 문자로만 이루어져 있으며, 각 문자의 의미는 다음과 같다.

# .: 깨끗한 칸
# *: 더러운 칸
# x: 가구
# o: 로봇 청소기의 시작 위치
# 더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나이다.

# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각각의 테스트 케이스마다 더러운 칸을 모두 깨끗한 칸으로 바꾸는 이동 횟수의 최솟값을 한 줄에 하나씩 출력한다.

# 만약, 방문할 수 없는 더러운 칸이 존재하는 경우에는 -1을 출력한다.
import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline


# 방향 벡터 설정: 오른쪽, 왼쪽, 아래, 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# (x, y)에서 (tx, ty)까지의 최소 이동 거리를 반환하는 BFS 함수
def bfs(x, y, tx, ty):
    visited = [[0]*w for _ in range(h)]  # 방문 여부 및 이동 거리 저장
    queue = deque()  # BFS를 위한 큐 생성
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        # 목표지점에 도달하면 이동 거리 반환
        if x == tx and y == ty:
            return visited[tx][ty] - 1

        # 상하좌우로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 방의 범위를 벗어나면 무시
                continue
            if room[nx][ny] == 'x' or visited[nx][ny]:  # 가구가 있거나 이미 방문한 칸이면 무시
                continue
            visited[nx][ny] = visited[x][y] + 1  # 이동 거리 갱신
            queue.append((nx, ny))  # 큐에 삽입

    # 목표지점까지 도달할 수 없으면 -1 반환
    return -1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 0, 0이 입력되면 종료
        break

    room = [list(map(str, input().strip())) for _ in range(h)]  # 방 정보 입력
    dirty = []  # 더러운 칸의 좌표 저장
    start = ()  # 로봇 청소기의 시작 위치 저장
    for i in range(h):
        for j in range(w):
            if room[i][j] == '*':  # 더러운 칸일 경우
                dirty.append((i, j))  # dirty 리스트에 추가
            if room[i][j] == 'o':  # 로봇 청소기의 시작 위치일 경우
                start = (i, j)  # start 변수에 저장

    dirty.insert(0, start)  # 시작 위치를 dirty 리스트의 첫 번째 요소로 삽입
    dist = [[0]*11 for _ in range(11)]  # 각 칸 사이의 최소 이동 거리를 저장할 리스트
    ok = True
    for i in range(len(dirty)):  # 각 칸 사이의 최소 이동 거리 계산
        for j in range(i+1, len(dirty)):
            dist[i][j] = dist[j][i] = bfs(
                dirty[i][0], dirty[i][1], dirty[j][0], dirty[j][1])
            if dist[i][j] == -1:  # 도달할 수 없는 칸이 있다면
                ok = False  # ok 변수를 False로 설정
    if not ok:  # 도달할 수 없는 칸이 있다면
        print(-1)  # -1 출력 후 다음 테스트 케이스로 이동
        continue

    # 모든 더러운 칸을 방문하는 순서의 모든 경우의 수에 대해 최소 이동 거리 계산
    pmt = list(permutations([i for i in range(1, len(dirty))], len(dirty) - 1))
    answer = float('inf')  # 최소 이동 거리를 저장할 변수
    for p in pmt:
        current = 0
        total = 0
        for next in p:
            total += dist[current][next]  # 이동 거리 누적
            current = next
        answer = min(answer, total)  # 최소 이동 거리 갱신

    print(answer)  # 최소 이동 거리 출력
