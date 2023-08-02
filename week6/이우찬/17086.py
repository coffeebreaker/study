#실버2 맞았당
# 문제
# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

# 안전 거리가 가장 큰 칸을 구해보자. 

# 입력
# 첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

# 출력
# 첫째 줄에 안전 거리의 최댓값을 출력한다.

# input
# 0 0 1 0
# 0 0 0 0
# 1 0 0 0
# 0 0 0 0
# 0 0 0 1

# filtered
# 0 2 2 2
# 2 2 2 2
# 2 2 0 0
# 2 2 2 2
# 0 0 2 2

# res
# 2 0 0 0
# 0 0 0 0
# 0 0 2 2
# 0 0 0 0
# 2 2 0 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(a,b):
    distance = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = []
    q.append([a,b])

    while q:
        x,y = q.pop(0)
        for i in range(8):
            #8방위 시작
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                # 상어 만나면 그게 최소거리값
                if matrix[nx][ny] == 1:
                    res[a][b] = distance[x][y] + 1
                    return
                # 안만나면 증가
                else:
                    visited[nx][ny] = True
                    q.append([nx,ny])
                    distance[nx][ny] = distance[x][y] + 1


# 다 상어 방지용
def one(matrix):
    for row in matrix:
        for element in row:
            if element != 1:
                return False
    return True

# filter로 다 걸러진 경우
def two(matrix):
    for row in matrix:
        for element in row:
            if element != 2:
                return False
    return True

#input
N,M = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    input_line = input().split()
    for j in range(M):
        matrix[i][j] = int(input_line[j])

# 미리 예방
if one(matrix):
    print(0)
    exit()

# 상어위치랑 상어 테두리는 다 제껴버리는 filtered. (탐색 줄이기 위함 = 만약 다 제껴지면 안전거리 1 1밖에 없으면 0임)
filtered = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            filtered[i][j] = 2
            # 8방향을 검사하여 주변의 0을 2로 바꿈
            for k in range(8):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                    filtered[nx][ny] = 2

# 안전거리 1 예방
if two(filtered):
    print(1)
    exit()

# 거리들을 담는 res
res = [[0 for _ in range(M)] for _ in range(N)]

#bfs 돌리자
for i in range(N):
    for j in range(M):
        if filtered[i][j] == 0:
            bfs(i,j)

max_value = max(max(row) for row in res)
print(max_value)