# 그래프 만들고 CHECK 만들기
# 8, 7, 9, 5, 7
# 1부터 가장 개수가 많은 것 만큼을 검사해줘야한다
# check를 초기화 해주어야한다.
# a[y+1][x] a[y-1][x] a[y][x+1] a[y][y+1]가 check가 true이며 이값이 자신보다 작을 시에만 check가 된다

#check는 실제로 썼는지를 검사한다.
#valid는 이게 유효한지 검사한다.
# 사용안했거나 유효하다면 True다 맨처음은 모두다 True다
"""
from collections import deque

n = int(input())
valid = [[True] * n for _ in range(n)]
check = [[True] * n for _ in range(n)]



dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
candidate = []

map = [list(map(int, input().split())) for i in range(n)]
maximum = 0
for i in range(n):
    for j in range(n):
        maximum = max(maximum, map[i][j])




def bfs(a, b):
    global ans
    q = deque()
    q.append((a, b))
    global right
    right =0
    check[a][b] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 유효한 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 다음 공간이 검사할 필요가 있는지 그리고 유효한 것인지 검사
                if check[ny][nx] and valid[ny][nx]:
                    check[ny][nx] = False  # 할당 연산자 오류 수정

                    # 다음 위치에서 범위 체크를 하기 위해 nx, ny로 조건 검사
                    if (ny + 1 < n and map[ny][nx] >= map[ny + 1][nx] and valid[ny + 1][nx]):
                        check[ny + 1][nx] = False
                        right = 1
                    elif (ny - 1 >= 0 and map[ny][nx] >= map[ny - 1][nx] and valid[ny - 1][nx]):
                        check[ny - 1][nx] = False
                        right = 1
                    elif (nx + 1 < n and map[ny][nx] >= map[ny][nx + 1] and valid[ny][nx + 1]):
                        check[ny][nx + 1] = False
                        right = 1
                    elif (nx - 1 >= 0 and map[ny][nx] >= map[ny][nx - 1] and valid[ny][nx - 1]):
                        check[ny][nx-1] = False
                        right = 1
                    if right == 1:
                        q.append((ny, nx))
                        ans += 1
                        right = 0
                else:
                    return
            else:
                return
    return ans


# 기준치를 못넘는 것들을 체크해주는 것
def making(k):
    for i in range(n):
        for j in range(n):
            if map[i][j] <= k:
                valid[i][j] = False


# 사용한 것인지 체크를 해주는 것
def refresh():
    for i in range(n):
        for j in range(n):
            check[i][j] = True
            valid[i][j] = True


for i in range(maximum):
    refresh()
    ans = 0
    making(i)
    for i in range(n):
        for j in range(n):
            candidate.append(bfs(i, j))
    
print(candidate)
print(max(candidate))
"""


#상 하 좌 우 변량

import sys
sys.setrecursionlimit(200000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and not valid[nx][ny] and graph[nx][ny] > h:
            valid[nx][ny] = True
            dfs(nx, ny, h)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
maximum =0
for i in range(n):
    for j in range(n):
        maximum = max(maximum, graph[i][j])
ans = 1
for k in range(maximum):
    valid = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not valid[i][j]:
                cnt += 1
                valid[i][j] = True
                dfs(i, j, k)
    ans = max(ans, cnt)

print(ans)