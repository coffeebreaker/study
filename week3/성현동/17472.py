import sys

# 기본세팅
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 섬 및 다리 형성 관련 메서드들

# I. name_islande: 땅(1)덩어리를 찾아 해당 섬의 셀들에 1~n까지의 번호를 매겨줌(dfs사용)
def name_islands(x, y):
    if x < 0 or x >= row_num or y < 0 or y >= col_num:
        return
    if visited[x][y] or map_info[x][y] == 0:
        return

    # 해당 셀이 지도 안에 있고, 방문한 적 없고, 땅이면
    # 방문표시 한 뒤, 현재 섬 번호로 셀 정보 업데이트
    visited[x][y] = True
    map_info[x][y] = island_id

    name_islands(x + 1, y)
    name_islands(x - 1, y)
    name_islands(x, y + 1)
    name_islands(x, y - 1)


# II. search_borders: 효율적인 탐색을 위해, 바다를 접한 해안가 셀 좌표만 찾아서 저장
def search_borders():
    island_borders = [set() for _ in range(island_id + 1)]  # 각 섬 번호별로 해안가 좌표를 저장하는 셋을 할당
    for i in range(row_num):
        for j in range(col_num):
            if map_info[i][j] > 0:  # 땅이면
                for dir in range(4):
                    new_x, new_y = i + dx[dir], j + dy[dir]  # 상하좌우 방향으로 탐색 전개
                    if 0 <= new_x < row_num and 0 <= new_y < col_num:  # 이동 시 맵을 벗어나지 않고
                        if map_info[new_x][new_y] == 0:  # 그 이동한 곳이 바다면, 해당 셀이 해안가라는 의미므로
                            island_borders[map_info[i][j]].add((i, j))  # 해당 섬의 셋에 좌표 저장
    return island_borders  # 각 섬별로 해안가 좌표들이 중복없이 저장된 셋 리스트를 반환


# III. build_bridges: 한 해안가 셀에서 다른 섬에 도달하는 길이 2이상의 다리 리스트를 구하는 함수
def build_bridges():
    for i in range(1, island_id + 1):
        for border in border_list[i]:  # 특정 섬의 해안가 리스트에서 해안가셀을 하나씩 꺼냄
            for dir in range(4):
                new_x, new_y = border[0] + dx[dir], border[1] + dy[dir]  # 그 셀 기준 상하좌우 이동 시도
                bridge_length = 0
                while True:
                    if not (0 <= new_x < row_num and 0 <= new_y < col_num):  # 맵 벗어나면 해당 방향 포기
                        break
                    elif map_info[new_x][new_y] == i:  # 한번 이동했는데 기존 섬 위면 해당 방향 포기
                        break
                    elif map_info[new_x][new_y] == 0:  # 정상적으로 바다로 나왔으면 그 방향으로 더 이동, 다리길이 늘림
                        new_x, new_y = new_x + dx[dir], new_y + dy[dir]
                        bridge_length += 1
                    else:  # 위 세가지가 모두 아니면, 다른 섬에 도착함을 의미.
                        if bridge_length >= 2:
                            # 다리는 (시작점,끝점,길이)의 튜플로 저장.
                            # 시작점,끝점은 오름차순 정렬해서 (2,4,2)(4,2,2)등 사실상 같은 다리의 중복저장을 방지
                            bridge = tuple(sorted((i, map_info[new_x][new_y]))) + (bridge_length,)
                            bridges.add(bridge)
                        break


# 크루스칼 관련 메서드들
# I. find: 해당 노드(섬)이 속한 트리의 최상위 부모 노드값 리턴해줌
def find(parents, i):
    if parents[i] != i:
        parents[i] = find(parents, parents[i])  # 경로단축 알고리즘
    return parents[i]


# II.union: 두 노드(섬)의 랭크를 비교해 저랭크가 고랭크 트리에 병합되도록 함
def union(parents, ranks, x, y):
    # 두 섬이 속한 트리의 대가리 섬들 불러냄
    root_x = find(parents, x)
    root_y = find(parents, y)

    # 랭크값으로 맞짱떠서 진 대가리의 트리가 이긴 대가리의 트리에 병합됨
    if ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y
    elif ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1


def kruskal(edges):
    parents = [i for i in range(island_id + 1)]
    ranks = [0 for _ in range(island_id + 1)]
    total_length = 0

    edges = sorted(edges, key=lambda x: x[2])  # 다리 리스트를 다리의 세번째 값인 다리길이로 오름차순 정렬

    for edge in edges:
        x, y, weight = edge
        # 다리의 양 정점(섬)의 부모노드가 다르면 사이클이 형성되지 않음을 의미하므로
        if find(parents, x) != find(parents, y):
            union(parents, ranks, x, y)  # 두 섬을 같은 부모 섬을 모시도록 한 트리에 병합시키고
            total_length += weight  # 해당 다리길이를 누적한다

    root = find(parents, 1)  # 모든 병합이 끝난 뒤, 최상위 부모 섬 노드값을 구한다
    for i in range(2, island_id + 1):
        if root != find(parents, i):  # 모든 섬들을 돌면서 최상위 부모섬과 다르 부모를 모시고 있는 경우
            return -1  # 모든 섬들이 한 트리에 병합되지 않음, 즉 모든 섬이 연결되지 못했음을 의미하므로 -1 리턴

    return total_length  # 그 외에는 성공적으로 섬들이 연결된 것이므로, 그 다리길이 누적 값 리턴


# 메인 로직
row_num, col_num = map(int, input().split())
map_info = [[0] * col_num for _ in range(row_num)]
for i in range(row_num):
    map_info[i] = [int(i) for i in input().split()]

visited = [[False] * col_num for _ in range(row_num)]
island_id = 0
for i in range(row_num):
    for j in range(col_num):
        if not map_info[i][j] == 0 and not visited[i][j]:
            island_id += 1
            name_islands(i, j)

border_list = search_borders()
bridges = set()
build_bridges()
print(kruskal(bridges))
