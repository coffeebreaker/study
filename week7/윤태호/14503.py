import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[False for _ in range(m)] for _ in range(n)]
count = 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# arrow = {0: '↑', 1: '→', 2: '↓', 3: '←'}

# def print_room(room, cleaned, r, c, d):
#     for i in range(n):
#         for j in range(m):
#             if room[i][j] == 1: # 벽인 경우
#                 print('1', end=' ')
#             elif i == r and j == c: # 청소기가 있는 칸인 경우
#                 print(arrow[d], end=' ')
#             elif cleaned[i][j]: # 청소가 완료된 칸인 경우
#                 print('x', end=' ')
#             else: # 청소가 안 된 칸인 경우
#                 print('0', end=' ')
#         print() # 줄바꿈
#     print() # 방 전체 출력 후 줄바꿈


while True:
    # 1번
    if not cleaned[r][c]:
        cleaned[r][c] = True
        count += 1
    
    cannot_clean = True
    for x, y in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = r+x, c+y
        if (room[nx][ny] != 1) and (not cleaned[nx][ny]):
            cannot_clean = False
    # 2번
    if cannot_clean:
        nx, ny = r-dx[d], c-dy[d]
        if room[nx][ny] == 0:
            r, c = nx, ny
            # print_room(room, cleaned, r, c, d)
            continue
        else:
            break
    # 3번
    else:
        d = (d+3)%4
        nx, ny = r+dx[d], c+dy[d]
        if (room[nx][ny] != 1) and (not cleaned[nx][ny]):
            r, c = nx, ny
            # print_room(room, cleaned, r, c, d)
        continue

print(count)