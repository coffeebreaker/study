import sys

# 기본세팅
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 섬 및 다리 형성 관련 메서드들
def name_islands(x, y):
    if x < 0 or x >= row_num or y < 0 or y >= col_num:
        return
    if visited[x][y] or map_info[x][y] == 0:
        return
    visited[x][y] = True
    map_info[x][y] = island_id

    name_islands(x + 1, y)
    name_islands(x - 1, y)
    name_islands(x, y + 1)
    name_islands(x, y - 1)


def search_borders():
    island_borders = [set() for _ in range(island_id + 1)]
    for i in range(row_num):
        for j in range(col_num):
            if map_info[i][j] > 0:
                for dir in range(4):
                    new_x, new_y = i + dx[dir], j + dy[dir]
                    if 0 <= new_x < row_num and 0 <= new_y < col_num:
                        if map_info[new_x][new_y] == 0:
                            island_borders[map_info[i][j]].add((i, j))
    return island_borders


def build_bridges():
    for i in range(1, island_id + 1):
        for border in border_list[i]:
            for dir in range(4):
                new_x, new_y = border[0] + dx[dir], border[1] + dy[dir]
                bridge_length = 0
                while True:
                    if not (0 <= new_x < row_num and 0 <= new_y < col_num):
                        break
                    elif map_info[new_x][new_y] == i:
                        break
                    elif map_info[new_x][new_y] == 0:
                        new_x, new_y = new_x + dx[dir], new_y + dy[dir]
                        bridge_length += 1
                    else:
                        if bridge_length >= 2:
                            edge = tuple(sorted((i, map_info[new_x][new_y]))) + (bridge_length,)
                            edges.add(edge)
                        break


# 크루스칼 관련 메서드들
def find(parents, i):
    if parents[i] != i:
        parents[i] = find(parents, parents[i])
    return parents[i]


def union(parents, ranks, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)

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

    edges = sorted(edges, key=lambda x: x[2])

    for edge in edges:
        x, y, weight = edge
        if find(parents, x) != find(parents, y):
            union(parents, ranks, x, y)
            total_length += weight

    root = find(parents, 1)
    for i in range(2, island_id + 1):
        if root != find(parents, i):
            return -1

    return total_length


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
edges = set()
build_bridges()
print(kruskal(edges))
