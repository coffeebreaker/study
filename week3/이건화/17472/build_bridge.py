from collections import deque

n, m = map(int, input().split())
print(n, m)
land = []
visited = []
for i in range(0, n):
    temp = list(map(int, input().split()))
    temp_visited = [False] * m
    land.append(temp)
    visited.append(temp_visited)

#땅 표시하기
def north_check(i, j):
    if i == 0:
        return False
    elif visited[i - 1][j] == True:
        return False
    elif land[i - 1][j] == 0:
        return False
    return True

def east_check(i, j):
    if j == m - 1:
        return False
    elif visited[i][j + 1] == True:
        return False
    elif land[i][j + 1] == 0:
        return False
    return True

def west_check(i, j):
    if j == 0:
        return False
    elif visited[i][j - 1] == True:
        return False
    elif land[i][j - 1] == 0:
        return False
    return True

def south_check(i, j):
    if i == n - 1:
        return False
    elif visited[i + 1][j] == True:
        return False
    elif land[i + 1][j] == 0:
        return False
    return True

def marking(y, x, mark):
    q = deque()
    q.append((y, x))
    land[y][x] = mark
    visited[y][x] = True
    land_temp = []
    while q:
        i, j = q.popleft()
        land_temp.append((i, j))
        if north_check(i, j):
            land[i - 1][j] = mark
            visited[i - 1][j] = True
            q.append((i - 1, j))
        if south_check(i, j):
            land[i + 1][j] = mark
            visited[i + 1][j] = True
            q.append((i + 1, j))
        if east_check(i, j):
            land[i][j + 1] = mark
            visited[i][j + 1] = True
            q.append((i, j + 1))
        if west_check(i, j):
            land[i][j - 1] = mark
            visited[i][j - 1] = True
            q.append((i, j - 1))
    return land_temp

mark = 1
land_list = []
for i in range(n):
    for j in range(m):
        if land[i][j] != 0 and not visited[i][j]:
            land_list.append(marking(i, j, mark))
            mark += 1
#edge 찾기
edge = [[0 for j in range(mark)] for i in range(mark)]
def find_north(i, j, mark) :
    temp_i, temp_j = i, j
    weight = 0
    while True :
        temp_i -= 1
        weight += 1
        if temp_i == -1 :
            return False
        if land[temp_i][temp_j] == 0:
            continue
        if land[temp_i][temp_j] == mark :
            return False
        if land[temp_i][temp_j] != mark :
            break
    if weight < 3 :
        return False
    else :
        weight -= 1
        f = mark
        t = land[temp_i][temp_j]
        if edge[f][t] == 0 :
            edge[f][t] = weight
        elif edge[f][t] > weight :
            edge[f][t] = weight

def find_east(i, j, mark) :
    temp_i, temp_j = i, j
    weight = 0
    while True :
        temp_j += 1
        weight += 1
        if temp_j == m :
            return False
        if land[temp_i][temp_j] == 0:
            continue
        if land[temp_i][temp_j] == mark :
            return False
        if land[temp_i][temp_j] != mark :
            break
    if weight < 3 :
        return False
    else :
        weight -= 1
        f = mark
        t = land[temp_i][temp_j]
        if edge[f][t] == 0 :
            edge[f][t] = weight
        elif edge[f][t] > weight :
            edge[f][t] = weight

def find_south(i, j, mark) :
    temp_i, temp_j = i, j
    weight = 0
    while True :
        temp_i += 1
        weight += 1
        if temp_i == n :
            return False
        if land[temp_i][temp_j] == 0:
            continue
        if land[temp_i][temp_j] == mark :
            return False
        if land[temp_i][temp_j] != mark :
            break
    if weight < 3 :
        return False
    else :
        weight -= 1
        f = mark
        t = land[temp_i][temp_j]
        if edge[f][t] == 0 :
            edge[f][t] = weight
        elif edge[f][t] > weight :
            edge[f][t] = weight

def find_west(i, j, mark) :
    temp_i, temp_j = i, j
    weight = 0
    while True :
        temp_j -= 1
        weight += 1
        if temp_j == -1 :
            return False
        if land[temp_i][temp_j] == 0:
            continue
        if land[temp_i][temp_j] == mark :
            return False
        if land[temp_i][temp_j] != mark :
            break
    if weight < 3 :
        return False
    else :
        weight -= 1
        f = mark
        t = land[temp_i][temp_j]
        if edge[f][t] == 0 :
            edge[f][t] = weight
        elif edge[f][t] > weight :
            edge[f][t] = weight

# for i in land :
#     print(i)
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if land[i][j] != 0:
            find_north(i, j, land[i][j]) 
            find_west(i, j, land[i][j])
            find_east(i, j, land[i][j])
            find_south(i, j, land[i][j])
for i in range(0, mark) :
        print(edge[i])

# key, p(parent), mst 준비
INF = float('inf')
key = [INF] * (mark - 1) # key는 무한대로 초기화
p = [-1] * (mark - 1)   # p(parent)는 -1로 초기화
mst = [False] * (mark - 1)

# 시작점 선택 : 0번 선택
key[0] = 0
cnt = 1
result = 0
while cnt < (mark - 1):
    # 아직 mst가 아니고, key가 최소인 정점 선택 : u
    MIN = INF
    u = -1
    for i in range(1, (mark - 1)):
        if not mst[i] and key[i] <MIN:
            MIN = key[i]
            u = i
    # u를 mst로 선택
    mst[u] = True
    result += MIN
    cnt+=1
    # key 값을 갱신
    # u에 인접하고, 아직 mst가 아닌 정점 w에서 key[w] > u - w 가중치  이면 갱신!
    for w in range(1, (mark - 1)):
        if edge[u][w] > 0 and not mst[w] and key[w] > edge[u][w]:
            key[w] = edge[u][w]
            p[w] = u

print(key) # [0, 21, 31, 34, 46, 18, 25]
print(p) # [-1, 2, 0, 4, 2, 3, 2]
print(result) # 175
